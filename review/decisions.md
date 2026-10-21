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
  - school-bus first-offense penalty: bullet only
  - two abreast (m9-02) next to the no-sharing-a-lane-with-a-car rule (m5-15)
- **m8-13 (red and yellow together).** The key rests on p.39's rule that you yield to pedestrians on red or red-and-yellow. The claim that this display stops all traffic could not be confirmed from an official source, so nothing was added.
- **Mild hints between paired questions** (m9-14/m9-15, m2-05/m7-01): rare in one practice test, and the wording is needed to make each question unambiguous.
- **Coverage gaps the reviewers noted** (SPIDER beyond "Decide", integrated brakes, dehydration and hypothermia): the counts per section stay as they are.

## App QA items not changed

- No reset control. Progress is per person, so someone trying the app doesn't affect anyone else's.
- Tap targets of 32–40 px on some secondary controls: above WCAG's 24 px minimum.
- Cosmetic notes: the banner timer doesn't tick on the home screen; there is wrapping in the phone header.

## Sources (checked 2026-10-21)

- mass.gov, Speed limits in thickly settled or business districts: https://www.mass.gov/info-details/speed-limits-in-thickly-settled-or-business-districts
- mass.gov, Southeast Expressway HOV lane: https://www.mass.gov/info-details/southeast-expressway-hov-lane
- WBUR, March 30, 2016, Baker signs bill ending automatic license suspensions for drug offenses: https://www.wbur.org/news/2016/03/30/baker-bill-automatic-license-suspensions
