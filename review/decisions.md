# How the open review questions were settled

The section reviews (m1–m9) and the app QA left judgment calls for a human. This records what was done with each. Outside facts added to the content were checked against the sources listed at the end.

## Changed

- **m1-13 replaced by m1-16.** m1-13 and m2-07 both keyed FMVSS No. 218 and shared three options. m2-07 keeps that fact. m1-16 asks how to tell a helmet meets the standard (stickers inside and out, p.9). It gets a new id because saved practice tests store option indexes.
- **m4-14 renamed m4-21.** The earlier review pass replaced m4-14 with a different question under the same id. A new id keeps any saved history from being paired with the wrong question.
- **m6-20 stem.** It no longer gives away m6-19's answer. "You have twisted a stuck throttle back and forth…" became "Your throttle is stuck, and your first attempt to free it has not worked." The distractor "Keep twisting the throttle…" was replaced for the same reason.
- **m3-07 explanation.** It now says that MSF-based courses, like the one the learner took, call the third turning step *Press*, while the manual says *Lean*.
- **m8-04 explanation.** It notes that many cities and towns have opted to lower the 30 mph thickly-settled default to 25 mph (MGL c.90 §17C), and that the manual's 30 is the figure for the test.
- **m9-04 explanation.** It notes that a lane posted as open to motorcycles, such as the I-93 Southeast Expressway HOV lane, is not restricted for a rider.
- **m9 summary, drug convictions.** The manual's 1–5 year license loss for any drug conviction now carries a note that a 2016 law ended most of those automatic suspensions.
- **Browser copies are kept per person.** QA found that progress already saved in a browser merged into whichever account opened the page there next. On a Claude artifact the browser's copy, and any paused practice test, now sits under the viewer's id, and anything done before the viewer is known joins their own copy. Leftover progress from before this change, or from a session with no identity, is never added to an account. GitHub Pages has no identity, so it keeps one shared copy per browser.
- **README.** It now says that practice tests draw from sections in proportion to the question bank, not to the manual. It gives the rule against reordering options or re-keying an existing id, and notes the capabilities the artifact must declare.

## Kept as is

- **m1-02 / m1-07 contrast** (sunrise-to-sunset permit rule vs. the 12:30–5:00 a.m. junior-operator curfew). The confusion is worth testing, as with steady vs. flashing yellow in m8.
- **The manual's answers where current law or training differs.** The test is drawn from the manual, so each such question keeps the manual's answer and its explanation says it is the manual's:
  - "J" vs. "U" restriction letter: bullet only
  - four seconds vs. MSF's three for poor conditions (m5-03)
  - three-quarters vs. 70% front-brake share (m3-12)
  - tire-failure weight shift (m6-17)
  - 45 mph highway minimum (m8-02, flagged volatile)
  - school-bus first-offense penalty (m9-33, flagged volatile; the statute now sets $250 as the minimum fine for a first offense)
  - two abreast (m9-02) next to the no-sharing-a-lane-with-a-car rule (m5-15)
- **m8-13 (red and yellow together).** The key rests on p.39's rule that you yield to pedestrians on red or red-and-yellow. The claim that this display stops all traffic could not be confirmed from an official source, so nothing was added.
- **Mild hints between paired questions** (m9-14/m9-15, m2-05/m7-01): rare in one practice test, and the wording is needed to make each question unambiguous.
- **Coverage gaps the reviewers noted** (SPIDER beyond "Decide", integrated brakes, dehydration and hypothermia): the counts per section stay as they are.

## App QA items not changed

- No reset control. Progress is per person, so someone trying the app doesn't affect anyone else's.
- Tap targets of 32–40 px on some secondary controls: above WCAG's 24 px minimum.
- Cosmetic notes: the banner timer doesn't tick on the home screen; there is wrapping in the phone header.

## Statistics coverage

The learner's spouse, who took the real test, said many of its questions asked for figures from the manual. An independent audit (stats-coverage.md) listed the manual's 198 numeric or statistical facts. The original 181 questions tested 66 of them. Adding 68 questions brings that to 134. Of the remaining 64, 40 are untestable or unlikely (phone numbers, list counts, sample signs, other license classes), and 24 are left out on purpose:

- **Junior-operator rules** beyond m10-09, m10-28 and m10-29, since the learner is an adult. The limit of three junior-operator questions set in the first review stands.
- **Moped and scooter rules** beyond their speed caps and the moped fine: the moped registration fee, the scooter fines and the scooter night rule.
- **Two figures that are out of date**: the p.9 insurance minimums and the p.10 "J" restriction letter.
- **Facts given in question stems**, so every reader meets them: the p.62 suspension triggers and the under-21 zero-tolerance age.
- **A few that appear in explanations.**

Each batch of new questions was checked against the manual by two reviewers, in three passes (stats-m1-m8.md, stats-m9-m10.md). Every REQUIRED finding and almost every OPTIONAL one was applied.

- **Section 9 split in two.** With the new questions, section 9 would have reached 60 questions, too long for one section test. Section 9 keeps pp.48 and 51–59 as "Motorcycle Laws, Turns & Right-of-Way". The new section 10, "Alcohol, Drugs & Penalties" (pp.59–64), holds the nine questions formerly m9-18 to m9-26, unchanged, as m10-01 to m10-09, plus the new ones. Progress saved on those nine starts over, because the app ignores ids that no longer exist.
- **Explanations trimmed so they don't give away new answers**: m1-01, m1-09, m2-07, m6-15, m8-02, m8-04, m9-17, m10-02, m10-03, m10-04 and m10-07. Distractor wording changed at the same index, never the key: m2-15 and m6-15.
- **Questions that share rows on purpose.** The five OUI fine-and-prison questions (m10-21, m10-32 to m10-35) take their options from the table's rows, and so do the suspension-length questions and the four fee questions. Within one section test, the last one seen can sometimes be answered by elimination. That cost was accepted so that every row is asked.
- **m1-19, moped fine.** The manual says "up to $100". The statute caps a first offense at $25 and a second at $50, so the wrong options avoid those amounts.
- **m8-30, highway default.** The statute applies the 50 mph default only to divided highways outside thickly settled districts and 40 mph to other roads there. The stem says "divided highway", and the manual's answer is unchanged.
- **m10-16, drug convictions.** It is now tested with the manual's answer (1 to 5 years), flagged volatile. The explanation says that a 2016 law ended most of these automatic suspensions.
- **m1-28, two knowledge tests.** Without a Class D license you must pass both tests. This is flagged volatile because the RMV's current permit pages don't mention it.
- **m10-31 and m10-32.** A reviewer checked these against the current statute. A third OUI offense is still a felony. For a second offense, 30 days of the term cannot be suspended, which matches the manual's 30-day minimum.
- **Practice tests** still draw from each section in proportion to its size, so they now include about four questions from section 10.
- **Numbers drill.** A home-screen button asks 20 questions marked `stat`. Like Quick 10, it puts missed questions first, then unseen ones. The 99 marked questions are the ones stats-coverage.md lists as testing a fact. Excluded are those whose answer is a rule, a name, an order or a place rather than a figure, such as "Slow, Look, Lean, Roll", "first vehicle in the intersection" and "until the out-of-state suspension is resolved".

## Sources (checked 2026-10-21)

- mass.gov, Speed limits in thickly settled or business districts: https://www.mass.gov/info-details/speed-limits-in-thickly-settled-or-business-districts
- mass.gov, Southeast Expressway HOV lane: https://www.mass.gov/info-details/southeast-expressway-hov-lane
- WBUR, March 30, 2016, Baker signs bill ending automatic license suspensions for drug offenses: https://www.wbur.org/news/2016/03/30/baker-bill-automatic-license-suspensions
- MGL c.90 §1B (motorized bicycles; fines): https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90/Section1B
- MGL c.90 §14 (school buses; first-offense fine of not less than $250): https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90/Section14
- MGL c.90 §17 (default speeds; 50 mph on divided highways outside thickly settled districts): https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90/Section17
- MGL c.90 §24 (OUI penalties): https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90/Section24
