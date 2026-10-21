# Review: new questions, edited explanations and bullets in m1, m2, m6, m8

I checked everything against the 2015 manual, reading both the extracted text and the page images (pp. 2, 4–8, 12–13, 36–37, 45, 49–50). I also checked these outside sources on 2026-10-21:

- MGL c.90 §1B and §17 (malegislature.gov)
- mass.gov: the MREP page, the RMV schedule of fees, and the thickly-settled speed-limit page
- NHTSA DOT HS 812 867
- the 1971 VESC-8 record (TRID) and a description of what it covers

`python3 scripts/build.py --check` passes for m1, m2, m6 and m8, with only the two old m8 duplicate warnings. Every `page` and `volatile` value on the 18 new questions is correct. No new or edited text copies a run of 7 or more words from the manual.

## Questions

- **m1-17: OK.** p.2: "The basic rider course is approximately fifteen (15) hours, with five (5) hours of classroom instruction and ten (10) hours of on-cycle instruction." The explanation matches p.2: "attend all classroom and on-cycle sessions and pass both a multiple-choice examination and riding skills evaluation". No distractor fits the current course: mass.gov still lists 10 hours on the bike, with the classroom part online or in person. `volatile: true` is right.
- **m1-18: OK.** p.4: "Its maximum speed must be thirty (30) miles per hour (mph) or lower. Its cylinder capacity must be fifty (50) cubic centimeters or lower." Each distractor fails on speed or on cc; the 25 mph option fails on its 150 cc. This matches the MGL c.90 §1 definition. See m1-21 for a hint aimed at this question.
- **m1-19: change (required).** The key is supported. p.5: "You can be fined up to $100 for a violation of any of these rules".
  - The problem: state law (c.90 §1B) caps a first moped offense at $25 and a second at $50; only later offenses can reach $100. The stem doesn't mention the manual, and "breaking one of the rules" naturally reads as a single, first violation. Under that reading "$25" is a correct answer, and "$50" is also a real cap.
  - New stem: "According to the manual, what is the most you can be fined for breaking one of the moped riding rules?"
  - New options, in the same positions: "$10", "$200", "$500", "$100". The answer stays 3.
- **m1-20: OK.** p.6: "It can go faster than 30 mph, but not more than 40 mph." This question and m1-11 hint at each other: the vehicle tops out at 40 mph and is barred from roads above 40. Both facts sit together on p.6, so I left it.
- **m1-21: OK, optional explanation edit.** p.6: "a limited use vehicle must have all of the following: … A 17-character VIN".
  - The last sentence, "The 50 cc limit belongs to the moped definition.", narrows m1-18 to two options when m1-21 comes first in a section test.
  - Replace it with: "The manual sets no engine-size limit for a limited use vehicle."
- **m1-22: OK, optional explanation edit.** p.7: "at least sixteen and one-half (16½) years of age and who has not had a driver's license or the right to operate revoked may apply".
  - "must never have been revoked" says more than the manual does.
  - Use "must not have been revoked", the wording bullet 7 already uses.
- **m1-23: OK.** p.8 table: "Permit Application (2 Year Permit Classes B, C, D, M) … $30.00". The RMV's current fee schedule still lists $30 for 2 years, $50 for the license and $35 for the road test, so no distractor is correct today.
- **m2-17: OK, optional distractor edit.** p.12: "per vehicle mile traveled, motorcycle riders were more likely than automobile passengers to die in a traffic accident."
  - "The car passenger is more likely to die" and "The rider is less likely to die, thanks to better maneuverability" make the same claim, so a test-wise learner can rule out both at once.
  - Replace the second with: "The rider is more likely to die, but only without a helmet".
- **m2-18: OK.** p.13: "According to NHTSA, motorcycle helmet use saves the lives of hundreds of motorcyclists annually." The explanation's "thousands of injuries" matches p.12. NHTSA's estimate for 2017 is 1,872 lives, which none of the distractors matches. The stem ties the question to the figure cited in the manual, so the key holds.
- **m2-19: change (required, giveaway).** The key is supported. p.13: "A plastic shatter-resistant faceshield (VESC-8)".
  - The problem: the distractor "A three-quarter or full-face helmet" names m2-08's answer ("Three-quarter and full-face"; p.13: "the three-quarter and full faced styled helmets"). It shows in every section test and in practice tests.
  - Replace it with: "A motorcycle helmet".
  - In the real world VESC-8 covers face shields and goggles, not helmets or windshields, so no distractor is correct. See also m2-07 below.
- **m6-25: OK, optional distractor edit.** p.49: "most often attributable to improper loading, unsuitable cycle accessories, or incorrect tire pressure."
  - The distractor "Riding in the center of the lane, where oil drips build up" states the p.28 fact behind m6-01's answer, which rules out m6-01's main distractor.
  - Replace it with: "Letting the engine idle too long before you ride".
- **m6-26: OK.** p.50: "Engine seizures are most often attributable to low oil pressure."
- **m8-27: OK, optional distractor edit.** p.36: "Riding too quickly (speeding) is one of the major causes of motor vehicle crashes."
  - "It rarely causes crashes by itself" can be argued outside the manual, since crashes seldom have a single cause.
  - Replace it with: "It is only a minor cause of crashes".
- **m8-28: OK.** p.36: "Limited-access highways, like the interstate routes, have posted speed limits ranging from 50 to 65 mph".
- **m8-29: OK.** p.37: "40 mph outside a thickly settled or business district". This also matches c.90 §17: "on any other way outside a thickly settled or business district".
- **m8-30: OK, optional stem edit.** p.37: "50 mph on a highway outside a thickly settled or business district".
  - Under c.90 §17 the 50 mph figure applies only "on a divided highway". Other roads outside these districts are 40 mph, so the "40 mph" distractor is the real-world answer for an undivided highway.
  - New stem: "You are on a divided highway outside any thickly settled or business district, and no speed limit is posted. Above what speed does the manual say you would be riding unreasonably fast?" The manual's answer stays 50, and it now matches the law.
- **m8-31: OK.** p.37: "Traffic signals typically consist of three round lights: red, yellow, and green, from top to bottom."
- **m8-32: OK.** p.45: "If more than one track crosses a road, the number of tracks is posted below the crossbuck."

Grammar and clarity are fine in all 18.

## Explanations

- **m1-01: OK.** p.7: "at least sixteen (16) years of age". It no longer gives away m1-22.
- **m1-09: OK.** p.4: "Do not drive faster than 25 mph." It no longer gives away m1-18.
- **m8-02: OK.** p.36: "the minimum speed on interstate and limited access highways is 45 mph." It no longer gives away m8-28.
- **m8-04: OK.** p.37: "30 mph in a thickly settled or business district". It no longer gives away m8-29 or m8-30. The 25 mph note matches mass.gov, which describes the c.90 §17C opt-in and lists the cities and towns that have adopted it.
- **m2-07: change (required, giveaway).** This explanation was not edited in this batch.
  - The problem: its last sentence, "The manual ties VESC-8 to shatter-resistant faceshields, not to helmets.", is m2-19's answer, and it shows after m2-07 in section tests.
  - Delete that sentence, leaving: "The manual says every motorcycle helmet sold in the U.S. must meet FMVSS No. 218, the performance standard that sets a helmet's minimum level of protection."

## Bullets

- **m1:** bullet 1 OK (p.2), bullet 3 OK (pp.4–5), bullet 4 OK (p.6), bullet 13 OK (p.8 table and "All fees are subject to change at any time.").
- **m2:** bullet 5 OK (p.13 for helmet use and lives saved, p.12 for the per-mile comparison). Bullet 8 OK (p.13 "(VESC-8)").
- **m8:** bullet 1 OK (p.36), bullet 3 OK (p.37), bullet 12 OK (p.45).
- **m8 bullet 2: OK, optional wording.** It is accurate to pp.36–37.
  - The second sentence now states the 45 mph minimum as fact. The old bullet credited it to the manual, and the earlier m8 review found no general 45 mph minimum in current law.
  - New second sentence: "The manual also says interstates and other limited-access highways are posted at 50 to 65 mph with a 45 mph minimum, and smaller highways at 55 mph or less."

## Second pass

I re-read the regenerated m1, m2, m4, m6 and m8 files and diffed them against the last commit. The only changes are the ones listed for this pass. I checked the new questions against pp.8, 9, 15, 20 and 24, as text and as page images; p.20's image confirms that the brake-light paragraph and both turn-signal points are on that page. Current-law checks: mavehiclecheck.com (motorcycles get "yearly safety inspections"; the sticker runs to May 31 of the next year) and the RMV schedule of fees (endorsement on an existing license $15.00). `build.py --check` gives 0 errors and only the two old m8 warnings. No new or changed text copies 7 or more words from the manual.

New questions:

- **m1-24: OK.** p.8: "Motorcycle Endorsement (on existing license) … $15.00". The distractors are other rows in the same table: $25 duplicate license, $50 Class M license, $115 Class M out-of-state conversion. None is the current endorsement fee. `volatile: true` is right. A learner who adds the $35 road-test fee to the $15 endorsement gets $50, a distractor. The stem points to a single fee-table line, though, so I left it.
- **m1-25: OK.** p.9: "Motorcycles registered in Massachusetts must undergo an annual safety inspection and receive a passing inspection certificate." Current law is still yearly, so no distractor is true today. `volatile: false` fits: it is a standing legal requirement, like m1-12's eye-protection rule.
- **m2-20: OK.** p.15: "It is strongly recommended that you make a complete check of your motorcycle prior to each ride." The explanation matches p.15's "more frequent attention" and "mechanical defect or equipment failure". "Only before long trips" is wrong because p.15 says each ride.
- **m4-22: OK.** p.20: "A motorcycle's brake light is usually not as noticeable as the brake lights on an automobile, particularly if the motorcycle's tail light is on." The night/day distractor runs against the manual, since the taillight is on at night.
- **m4-23: OK.** p.20: "A driver traveling behind you is more likely to see a turn signal than a taillight."
- **m4-24: OK, optional explanation edit.** p.24: "Checking vehicle mirrors every few seconds will enable the rider to respond appropriately and safely when traffic conflicts or hazards arise."
  - "Check them with extra care when slowing or stopping suddenly" can read as sudden slowing only. p.24 says "when slowing the cycle or coming to a sudden stop".
  - Use: "Check them with extra care whenever you slow down or make a sudden stop."

Fixes from the first pass, all applied as proposed and checked again:

- m1-19 stem and options, m1-21 and m1-22 explanations: OK.
- m2-07 explanation, m2-17 option, m2-19 option: OK.
- m6-25 option, m8-27 option, m8-30 stem, m8 bullet 2: OK.

None of these edits creates a new give-away, a length cue or a real-world-true distractor.

Other changes:

- **m2-15 distractor: OK.** "…when the motorcycle is inspected" no longer states a frequency, so it no longer gives away m1-25. It is still plainly wrong (p.15: "Try the front and rear brake one at a time").
- **Bullets: OK.** m1 bullet 10 (pp.9–10), m1 bullet 13 (p.8) and m4 bullet 7 (pp.20–21).

Give-aways: none between the six new questions and existing ones in m1, m2 or m4. Some mild hints, all acceptable:

- m1-23's explanation rules out "$50" in m1-24, and m1-24's explanation rules out "$15, for 1 year" in m1-23.
- m2-15's stem, "During a pre-ride check", hints that checks come before riding. It does not separate "Before every ride" from "Only before long trips" in m2-20.
- m4-22 and m4-23 both compare a light with the taillight. That tests the difference between them; neither gives away the other.

No other section has a near-duplicate of any of the six new questions.

## Third pass

I re-read the regenerated m1, m6 and m8 files and diffed them against the last commit. The only changes since pass 2 are the six new questions and the three trimmed explanations, and the m4-24 wording is in. I checked the new questions against pp.7, 8, 30, 31 and 36, as text and as page images. `build.py --check` gives 0 errors and only the two old m8 warnings. No new text copies 7 or more words from the manual.

New questions:

- **m1-26: OK, but see the fee give-aways below.** p.8: "Class M (5 Year License) [Motorcycle Only] … $50.00". The RMV's current fee schedule still lists $50 for 5 years, so no distractor is correct today. `volatile: true` is right.
- **m1-27: OK, but see the fee give-aways below.** p.8: "License Application and Road Test (for all classes) … $35.00". The fee is still $35 today. `volatile: true` is right.
- **m1-28: OK, optional `volatile` change.** p.7: "If an applicant does not have a Class D license, he/she must pass both a Class D knowledge test and a Class M knowledge test."
  - Which tests a permit applicant must pass is a licensing procedure that may have changed since 2015.
  - I could not confirm the rule is still current: the RMV's permit-exam FAQ (revised 2022) and its exam overview don't mention it.
  - Set `volatile: true` so the caution note shows.
- **m6-27: OK.** p.30: "A swerve can be described as any sudden change in direction by the rider. It can be either two quick turns or a rapid shift to the side." It is distinct from m6-09, which asks how to perform a swerve.
- **m6-28: OK.** p.31: "Riders have a better chance of surviving impact with an animal as opposed to impact with a motor vehicle." See m6-15 below.
- **m8-33: OK.** p.36: "smaller highways have limits of 55 mph or lower". No distractor is logically true:
  - "45 mph or lower" is a stronger claim that the manual doesn't make.
  - "60 to 65 mph" and "At least 65 mph" contradict 55 or lower.
  - m8-33's 65 mph distractors hint mildly at m8-28's "50 to 65 mph", the only m8-28 range ending at 65. Most learners already know 65 as the interstate limit, so I left it.

Trimmed explanations, all accurate and no longer give-aways:

- **m1-23** (p.8) no longer gives away m1-26 or m1-27.
- **m6-15** (p.31) no longer gives away m6-28.
- **m8-28** (p.36) no longer gives away m8-33.

Fee give-aways (m1-23, m1-24, m1-26, m1-27). For each question, I assumed the learner had already seen the other three explanations in a section test:

- **m1-23: change (required, give-away).** All three distractors are ruled out by the other questions' answers:
  - "$15, for 1 year": m1-24's explanation says $15 is the endorsement fee.
  - "$50, for 5 years": m1-26's explanation says that is the Class M license.
  - "$35, for 6 months": m1-27's explanation says $35 is the road-test fee.

  Only the key is left, which happens whenever m1-23 comes after the other three (1 in 4 section tests). m1-23 and m1-26 also share both keys word for word ("$30, for 2 years" and "$50, for 5 years"). Replace "$50, for 5 years" with "$25, for 3 years". That leaves two candidates and one shared option.
- **m1-27: optional distractor edit.** m1-24 and m1-27 share three options word for word ($15, $25, $50), so m1-27's key, $35, is the only option not repeated from m1-24. Replace "$25" with "$40", which is not the road-test fee; it is the manual's Class A permit fee.
- With both edits, each fee question keeps at least two candidates after elimination, and no key is a question's only unshared option.
- m1-24 and m1-26 are fine: three and two candidates remain.

Other give-aways in m1, m6 and m8:

- **m6-15: optional distractor edit.** "Swerve into the next lane, since hitting the animal is the bigger danger" states the reverse of m6-28's answer. That is the hint the trimmed explanation was meant to remove. Replace it with "Swerve into the next lane to get around it", which is still plainly wrong; p.31 says to "avoid swerving into adjacent lanes of travel to avoid hitting the animal". The m6-15/m6-28 link that remains is part of the manual's own reasoning, so it is acceptable.
- The remaining hints are mild and come with paired facts: m6-09 and m6-27 (swerving), m8-28 and m8-33 (highway limits).
