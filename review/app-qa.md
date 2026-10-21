# App QA: Class M Permit Prep

Independent test of the app itself (`src/app.html`), not the question content. Tested on 2026-10-21 against the built `index.html` in headless Chromium (Playwright). Phone was 390×844 with touch and laptop was 1366×768, each in light and dark. I also spot-checked 360 px and 320 px widths. The scripts are in `/tmp/claude-0/qa/v2/`, outside the repo; the real web fonts were served locally so screenshots are faithful. On the final build: about 5,700 checks, no failures, no console errors and no unhandled rejections.

## What I tested

- **Every screen in all four configurations** (home, section, question, feedback, manual viewer and zoom, section results, practice test, confirm sheet, practice results and review). Nothing overflows and nothing scrolls sideways at 390, 360 or 320 px. Text is legible in both color schemes.
- **Grading with shuffled options.** All 181 questions were answered right once and wrong once: taps on the first pass, keys 1–4 / a–d / A–D on the second. For each one I checked:
  - the verdict, and which option was marked correct or wrong
  - that the explanation matches the bank
  - that the yellow caution note appears exactly on `volatile` questions
  - the cited-page chip, the end score, the missed list and what was stored.
  The correct answer landed evenly across A–D (85/95/90/92).
- **Manual citations.** All 181 cited pages and all 66 section page chips open the right image (PDF page = printed + 7). Printed p.49 shows "Mechanical Problems" and p.16 shows "Body Position & Posture". The cover, contents and back-cover labels are right, prev/next stop at the ends, and a missing image shows the fallback message.
- **Practice test:**
  - exactly 25 questions, allocated 2/2/3/3/2/3/2/4/4 across sections (sums to 25 and matches the code), no repeats, and the next test draws questions not yet seen
  - the timer starts at 25:00 and counts down, with no feedback during the test
  - 18 right is "Passed" and 17 is "Didn't pass"; blank answers go through the confirm sheet and count as wrong
  - the by-section table and the review (Missed/All, Blank/Yours/Answer, caution notes) are correct
  - time-out, using Playwright's clock: low-time styling in the last minute, "Time ran out", answered questions are scored
  - reloading mid-test brings back the same questions, option order and answers, and the timer keeps running; a test that expires while the page is closed is scored on the next load; discarding works.
- **Quick 10 and Missed questions.** Quick 10 serves missed questions first, then unseen ones, then the weakest. Retrying missed questions works overall and per section. Progress survives reloads, and corrupt saved data starts fresh instead of breaking the page. There is no reset control (see suggestions).
- **Storage blocked three ways** (the methods throw, the `localStorage` getter throws, quota is zero). The app still works and the footer says progress can't be saved.
- **Account sync.** I tested against an in-memory mock built from `claude.d.ts`, `user.d.ts` and `db.d.ts`. It follows the contract: frozen namespaces and snapshots, `TypeError` on bad paths, `{code, message}` rejections, pending-write echoes, detection of overlapping writes, and a store that persists across reloads. Verified:
  - progress is written to `data/users/<id>/progress`
  - local and remote progress merge (the newer answer wins, tests are unioned, the section best is kept), and nothing is written when nothing changed
  - `can('data.write')` false, `use('user')` or `use('db')` null, `id()` null, or no `use` at all each leave it in browser mode with "saved in this browser only"; `can()` null still uses the account, as the contract says
  - `invalid_argument`, `revoked` and `quota_exceeded` fall back cleanly; `unavailable` is retried
  - changes from another device show up live; if the subscription dies, saving still works
  - pending changes are flushed when the page is hidden, and writes to the document never overlap
  - full progress (all questions plus 30 tests) is a 22 KB document.
- **Keyboard only:** visible focus on every stop, answering and moving on with keys, exam keys and arrows plus the question grid, and both dialogs.
- **Tap targets** surveyed on the phone, and `dist/artifact.html` smoke-tested inside a host-style wrapper.

## Bugs found and fixed

All fixes are in `src/app.html` (rebuilt; `scripts/test_logic.js` passes).

1. **Time ran out under the "Finish with N blank?" sheet, and the sheet stayed open over the results.** "Finish and score" then did nothing. Fix: `finishExam` closes an open sheet.
2. **"Take another practice test" silently discarded a test in progress.** To reach it: pause a test, tap "Review your last practice test", then tap the button. Fix: while a test is in progress, that results page offers "Resume practice test", as the home screen already does.
3. **Two open tabs overwrote each other's progress (browser-only mode).** Each tab saved its own in-memory copy over localStorage. In testing, one answer in the second tab erased three answers from the first. This is plausible on a phone when the link is tapped again. Fix: every save first merges the stored copy (`mergeStates`), and a `storage` listener refreshes the other tab's screens.
4. **Tab moved focus out of the open manual viewer and the confirm sheet** onto controls hidden behind them. Enter could then press "Next question" behind the viewer, or a question number behind the sheet. Fix: `#app` is `inert` while either is open.
5. **Focus fell to the page when the viewer's focused Next/Prev button became disabled** at the last or first page. Fix: focus moves to the other button.
6. **A sync re-render dropped keyboard focus to the top of the page.** This happens when the account connects after load, or when another device saves while she is on the home or section screen. Fix: `refreshPassive` puts focus back on the same control.
7. **Retry button copy** read "Retry the 4 ones you missed" and, with one miss, "Retry the 1 one you missed". It now reads "Retry the 4 you missed" and "Retry the one you missed".
8. **Sync error handling didn't match `db.d.ts`:**
   - An unknown error code dropped the visit to browser-only mode. The contract says to treat unknown codes as `unavailable`, so they are now retried (the initial `get()` too). The terminal codes are listed explicitly: `invalid_argument`, `quota_exceeded`, `revoked`, `not_granted`, `capability_*` and `transform_error`.
   - `resource_exhausted`, and repeated `unavailable`, were retried every 1.5 s forever, where the contract says to slow down. Retries now back off (3 s, 6 s, 12 s … up to 60 s) and reset after a successful save.

New checks in `test_logic.js`:
- merging with nothing stored leaves progress unchanged
- a second tab's save keeps the first tab's answers
- recording progress after merging frozen account data never writes into that data.

## Open issues and suggestions (not changed)

- **The practice-test mix follows the size of each section's question bank, not the manual.** The README says "in proportion to the manual's sections". Section 1 (10 manual pages) gets 2 questions while Section 3 (4 pages) gets 3, and the mix shifts whenever questions are added or removed. Either reword the README or allocate by manual pages.
- **There is no way to reset progress.** If one is added, it needs a marker so other devices' merges don't bring the old progress back.
- **Stored practice tests record the index of the chosen option.** If a question's options are later reordered, or its `answer` changes, old reviews will pair the wrong texts. The current content edits keep every index stable (69 questions reworded, none reordered or re-keyed). Suggest adding to the README: never reorder options or change `answer` on an existing id; give a substantially rewritten question a new id.
- **Publishing:** the artifact must declare `capabilities: { user: {}, db: {} }`. Without it, `id()` is null and everyone stays in browser mode. Note also that `can('data.write')` describes shared documents. With the default rules it matches the viewer's own `data/users/<id>/` subtree, but a custom rule set (root `write: "admin"` with `data/users/{self}` at `interact`) would put Contributors in browser mode needlessly.
- **Sync edge cases, by design or minor:**
  - when two devices save in the same instant, the account copy can miss one device's latest answers until its next answer or reload (the contract forbids writing back from the snapshot callback)
  - a subscription the platform kills isn't reopened (saving still works)
  - two failed initial reads leave that visit in browser mode
  - progress already in a browser merges into whichever account opens the page there.
- **The home banner's "M:SS left" doesn't count down.** A test that runs out while she is on another screen, or with the page closed, is scored without a message.
- **Phone tap targets** below the 44 px guideline, though above WCAG's 24 px minimum: page chips 36 px, question-grid buttons 40×36, the review filter 33 px, and "Review your last practice test" 32 px.
- **Cosmetic:**
  - on phones the sign's legend wraps, and "25 minutes" starts its line with a divider bar
  - the Overpass "·" sits tight against the next word ("Section test ·15 questions"); the source has normal spaces, so this is the glyph's spacing
  - on the laptop the manual page is capped at 680 px wide, so a full page needs scrolling.
