# m9 / m10 review: new questions, edited explanations, bullets

Scope: new questions m9-27 to m9-35 and m10-10 to m10-29; edited explanations m9-09, m9-17, m10-02, m10-03, m10-04, m10-07; all m10 bullets; m9 bullets 5 and 8.

Method: I read every cited page as an image (printed pp.48, 51–53, 56, 58–64, which are PDF pages +7). I read the tables on pp.61–64 at 110 and 200 dpi. A script found no run of 7 or more words shared with the manual in any stem, option, explanation or bullet checked, and no key longer than 1.3 times its longest distractor. Section tests show every question in the section in shuffled order, and reveal the key and explanation after each one, so I judged cross-question hints on that basis. I checked current law at malegislature.gov (c.90 §14), on the mass.gov pages for OUI over 21, accumulated offenses and junior-operator violations, and in WBUR's March 30, 2016 report.

Result: the manual supports all 29 keys on the cited pages. No distractor can be defended as correct, and none matches current Massachusetts law where the manual differs. One change is required (m9 bullet 5). I also recommend replacing m9-29, which tests the same fact as m9-09.

## m9 new questions

- **m9-27** OK. p.51: "treat the far right lane as a slower-speed through lane, the middle lane as a faster through lane, and the far left lane as the passing lane."
- **m9-28** OK. p.51: "Remember these three steps: (1) look, (2) signal, (3) move."
- **m9-29** Replace (check 6). The key is right (p.51: "Be sure to signal your exit at least 500 feet before you reach the exit ramp."), but the fact is the same as the highway half of m9-09 (p.53: "On a highway, signal at least 500 feet before a turn."). In a section test, whichever of the two comes second is answered by the first one's revealed key. m9-29's explanation also leaves only one m9-09 option with 500 feet on a highway. Removing "the same distance used before an exit ramp" from m9-09 did not remove the overlap. The built index.html already contains m9-29, so remove it and add the replacement under a new id (README rule), or drop m9-29 with no replacement:
  - id `m9-36`, page 51, volatile false, answer 2
  - q: "You are entering a highway from an entrance ramp. What does the manual say to do with your speed as you move into the travel lane?"
  - options: "Hold it at the ramp's posted speed until you are fully in the lane" / "Slow down so drivers on the highway can make room for you" / "Increase it to match the speed of traffic already on the highway" / "Go faster than highway traffic so you can get ahead of it"
  - explanation: "Speed up as you enter the travel lane so you are moving at the same speed as the vehicles already on the highway."
  - Support, p.51: "As you approach and enter a highway travel lane, increase your speed to match that of vehicles already on the road." No question tests this yet. m5's merging question is about other drivers merging near you. Bullet 4 already says "match its speed".
- **m9-30** OK. p.52: "If you plan to ride a long distance, stop and stretch after every 2 hours or every 100 miles." Optional: add the serial comma used elsewhere in the bank, giving "the next exit, rest area, or service plaza".
- **m9-31** OK on facts. p.53: "Do not attempt a U-turn at the crest of a hill, near a curve, or at any other point at which you or other drivers cannot see from 500 feet away." Optional, for clarity: the stem "...anywhere you or other drivers can't see from at least how far away?" is hard to parse. Use "The manual says not to make a U-turn anywhere visibility, for you or for other drivers, is less than what distance?" In the explanation, change "anywhere you and other drivers have less than 500 feet of visibility" to "anywhere visibility, for you or for other drivers, is under 500 feet", because the manual says "you or other drivers".
- **m9-32** OK. p.56: "you must yield the right-of-way to vehicles driving on a divided highway or a roadway with three or more lanes." "Only vehicles ... approaching from your right" misapplies the p.55 rule, and "Only" rules it out.
- **m9-33** OK. p.56: "A first violation of this law can result in license suspension and a fine of $250." It is marked volatile, and the explanation attributes the figure to the manual. None of $50, $100 or $1,000 is the current first-offense figure: under c.90 §14 the first-offense fine is "not less than $250", and the $500–$1,000 fine and license revocation begin with a second offense. decisions.md still lists this penalty as "bullet only", so that line should now name m9-33.
- **m9-34** OK. p.58: "you must position your vehicle within 12 inches of the curb, except where angled parking is allowed."
- **m9-35** OK. p.58: "Within 20 feet of an intersection". m9-17 and m9-35 each show the other's key as a distractor, so whichever comes second loses one option. The hint is mild, and the 10-foot vs 20-foot contrast is worth testing.

## m10 new questions

- **m10-10** OK. p.59: "Even one alcoholic drink can affect your ability to ride safely."
- **m10-11** OK. p.59 lists the five factors. p.60: "Regardless of the type of alcoholic beverage consumed, the critical factor is the amount of alcohol consumed in a certain time period."
- **m10-12** OK. p.60: "1 ounce Serving of 80-Proof Liquor". No option is 1.5 oz (the US standard-drink figure), so no distractor matches the real-world figure.
- **m10-13** OK. p.60: "Any one of these drinks can increase the average person's BAC by 0.02%."
- **m10-14** OK. p.60: "If you consume more than one drink per hour, your BAC starts to rise".
- **m10-15** OK. p.60: "This new law substantially increases the penalties and administrative sanctions for OUI offenses." The distractors describe other laws.
- **m10-16** OK. p.60: "...lose operating privileges for a period of one (1) to five (5) years, depending on the conviction." The 2016 sentence matches WBUR: most automatic suspensions were repealed, and those for trafficking and drugged driving were kept. It follows the approach in decisions.md. No option says the license is unaffected, so no distractor matches current law.
- **m10-17** OK on facts. p.61, Second Offense: $600–$10,000; minimum 30 days, maximum 2½ years; 2 years. Optional (check 6): the explanation's fine and prison figures are the same as m10-21's distractor "A $600–$10,000 fine and at least 30 days in prison". Use "The manual's OUI table lists a 2-year license suspension for a second offense."
- **m10-18** OK on facts. p.61, Third Offense (Felony): $1,000–$15,000; minimum 150 days, maximum 5 years; 8 years. Optional (check 6): it has the same problem with m10-21's "$1,000–$15,000 fine and at least 150 days in prison". Use "A third offense is the first one the table lists as a felony, and it brings an 8-year license suspension." Without both trims, a learner who sees m10-17 and m10-18 first can narrow m10-21 to two options. The figures in m10-19 and m10-20 appear in no option.
- **m10-19** OK. p.61, Fourth Offense (Felony): 10 years.
- **m10-20** OK. p.61, Fifth Offense (Felony): Lifetime. When m10-18 and m10-19 come first, their keys rule out "A third offense" and "A fourth offense". That is unavoidable with five questions on one ladder. p.61 now carries seven questions (m10-07 and m10-17 to m10-22).
- **m10-21** OK. p.61, First Offense: "$500–$5,000", "Maximum 2 1/2 years".
- **m10-22** OK. p.61: "Over Age 21, 45–90 days / Under Age 21, 210 days". mass.gov gives the same figures today.
- **m10-23** OK. p.62: "Must complete driver retraining program within 90 days or license will be suspended indefinitely until course is completed", $100.
- **m10-24** OK. p.62: seven surchargeable events "within a 3-year period", 60 days, $100.
- **m10-25** OK. p.62: Habitual Traffic Offender, 4 years, $500.
- **m10-26** OK on facts. p.62: "A total of three major moving violations or any combination of twelve major or minor moving violations within a 5-year period." Optional: change volatile from true to false. The question asks for a definition, which the volatile rule puts at false, and mass.gov's current definition is the same.
- **m10-27** OK. p.62: "License has been suspended or revoked in another state." and "Until the out-of-state suspension is resolved".
- **m10-28** OK. p.64, Passenger or Night Restriction: "60 days— first offense / 180 days— second offense / One year— subsequent offenses", and "Second and subsequent offenses require a Driver Attitudinal Retraining course." The mobile-device row has the same 60-day, 180-day and one-year ladder (pp.63–64).
- **m10-29** OK on facts. p.63, Drag Racing: "One year— first offense / Three years— second or subsequent offense" and "$500-first offense / $1000-second or subsequent offense". It also says "All offenses require a new learner's permit exam and a Driver Attitudinal Retraining course." Optional, for clarity: in "along with a $500 or $1,000 reinstatement fee, retaking ..., and completing Driver Attitudinal Retraining", the reader can't tell which fee goes with which offense, and the list mixes forms. Use "A junior operator's first drag racing conviction brings a one-year suspension and a $500 reinstatement fee; a second or later one brings three years and a $1,000 fee. Every offense also means retaking the learner's permit exam and completing a Driver Attitudinal Retraining course." mass.gov now lists $500 for a license holder's second offense. The manual's $1,000 stands for the test, and the volatile flag covers the change.

## Edited explanations

- **m9-09** OK. p.53: "Signal your turn at least 100 feet before making the turn. On a highway, signal at least 500 feet before a turn." It still overlaps with m9-29 (see above).
- **m9-17** OK. p.58: "Within 10 feet of a fire hydrant or fire lane". Dropping the 20-foot contrast was right, because it gave away m9-35.
- **m10-02** OK. p.60. It no longer gives the liquor serving size (m10-12) or the 0.02% figure (m10-13).
- **m10-03** OK. p.60: "register a 0.08% BAC or higher, you are operating above the legal limit". It no longer gives away m10-10.
- **m10-04** OK. p.60: "a BAC of 0.02% is above the legal limit if you are under 21 years of age." It no longer ties 0.02% to one drink (m10-13).
- **m10-07** OK. p.61: "For your first offense, the court may allow you to complete an alcohol education course to reduce your license suspension period." It no longer gives away m10-21 or m10-22.

## Summary bullets

- **m9 bullet 5** Change required. "Change lanes in three steps (look, signal, move) after checking your blind spot" reads as though you check your blind spot before you look. p.51: "Remember these three steps: (1) look, (2) signal, (3) move. Also, check your blind spots before making your move." Use: "On a three-lane expressway, use the right lane as the slower through lane, the middle as the faster through lane, and the left for passing. Change lanes in three steps (look, signal, move), checking your blind spot before you move. On long rides, stop to stretch every 2 hours or 100 miles."
- **m9 bullet 8** OK. pp.55–56.
- **m10 bullet 1** OK. p.59.
- **m10 bullet 2** Optional. Change "what you ate beforehand" to "how much you ate beforehand". p.59: "The amount of food consumed prior to drinking alcohol". The rest is OK (p.60).
- **m10 bullet 3** OK. pp.59–60.
- **m10 bullet 4** OK. p.60.
- **m10 bullet 5** OK. p.60.
- **m10 bullet 6** Every fine, prison term, suspension and reduced suspension matches the p.61 table. Optional: change "third (a felony)" to "third (a felony, as are the fourth and fifth)", since the table marks the Third, Fourth and Fifth offenses "(Felony)".
- **m10 bullet 7** OK. p.60. The 2016 note is verified.
- **m10 bullet 8** OK. Every figure matches the p.62 table.
- **m10 bullet 9** OK. pp.63–64, first offenses: speeding 90 days; night restriction, passenger restriction and mobile device 60 days; drag racing one year.

## Other

- README still says "Nine study sections" and "content/m1.json … m9.json".
- There are three junior-operator questions (m10-09, m10-28, m10-29), which is the limit the earlier m9 review mentioned.

## Second pass

Method: both files were regenerated, so I re-read them in full. Compared with git HEAD, m9-01 to m9-17 and m10-01 to m10-09 differ only in the planned explanation edits (m9-17, m10-02, m10-03, m10-04, m10-07). m9-09 is back to its HEAD wording, and the m9 bullets other than 5 and 8 match HEAD. The validator reports 0 errors (its two warnings are both in m8). No explanation or bullet shares a run of 7 or more words with the manual, no key is the longest option by more than 1.3 times, and no new stem is near the duplicate threshold.

The first-pass fixes are applied as proposed and match the manual: m9 bullet 5, the m9-30 comma, the m9-31 stem and explanation, the m10-17 explanation, m10-26 volatile false, the m10-29 explanation, and m10 bullets 2 and 6.

### Changed or new

- **m9-29 (replaced)** The key is right. p.51: "As you approach and enter a highway travel lane, increase your speed to match that of vehicles already on the road." Optional (check 6): the added sentence "Drivers already on the highway have the right-of-way." points to m9-32's key, the only option that names a divided highway, and by analogy to m9-13's "Vehicles already in the rotary". The first sentence explains the key on its own, so drop the second.
- **m9-09** OK. Now that m9-29 is not about exit signals, "the same distance used before an exit ramp" gives nothing away. p.51: "signal your exit at least 500 feet before you reach the exit ramp."
- **m10-02, m10-12** OK. Neither mentions half an ounce now, so neither gives away m10-30.
- **m10-18** OK. Neither the stem nor the explanation mentions felony status, so it no longer gives away m10-31. p.61: Third Offense, 8 years.
- **m10-19** OK. p.61, Fourth Offense: $1,500–$25,000, minimum 1 year and maximum 5 years, 10 years. It doesn't mention felony status, and its fine and prison figures appear in no option.
- **m10-21** Option C is now an invented row, and no other question shows which row any option comes from. Optional: A and C, the two invented options, are the only ones that say "jail". The p.61 column is headed "Prison Term", so the word marks them as invented, leaving B against D. Use "A $100–$500 fine and up to 30 days in prison" and "A $250–$2,500 fine and up to 1 year in prison".
- **m10-30** OK. p.60: "Each of the following drinks contain about the same amount of alcohol (about ½ oz.)". "About 1 ounce" tests confusion with the 1-ounce liquor serving (m10-12). No option is the US standard-drink figure of 0.6 oz. volatile false is right.
- **m10-31** OK on facts. p.61 labels the third, fourth and fifth offenses "(Felony)" and the first and second have no label. Current law agrees: a third offense can bring state prison (c.90 §24(1)(a)(1)). Optional, for clarity: in "which is the first offense listed as a felony?", "first offense" collides with the table's "First Offense" row. Use "In the manual's OUI penalty table, which is the earliest offense listed as a felony?" Optional: add the serial comma, giving "the third, fourth, and fifth OUI offenses".
- **m10-32** OK. p.61, Second Offense: "Minimum 30 days / Maximum 2 1/2 years". Current law sets 60 days to 2½ years, "not ... reduced to less than thirty days" (c.90 §24(1)(a)(1)), so the manual's 30 days is the mandatory floor, and no option is 60 days. Optional: add a comma after the opening phrase, giving "For a second OUI offense, the table lists ...", as in m10-21.

### Give-aways across m10 (32 questions)

- **OUI table:** m10-07, m10-17 to m10-22, m10-31 and m10-32, nine questions on p.61. No stem or explanation states another question's answer:
  - The m10-07 and m10-22 explanations give no figures for other questions.
  - m10-17 and m10-18 give only their own suspension lengths.
  - The fines and prison terms in m10-19 and m10-20 appear in no option.
  - No stem or explanation mentions felony status.
  - m10-21's "minimum prison terms rise with each later offense" only rules out m10-32's "None", which the stem already makes unlikely.
- **Remaining overlap:** it comes from revealed keys on the suspension ladder. m10-07, m10-17, m10-18 and m10-19 each have a sibling's key as a distractor, and m10-20 offers the third and fourth offenses. Depending on order, m10-07, m10-17 and m10-20 can drop to two options. That is the cost of asking about each row, and the learner eliminates options using facts the section has just taught. No change.
- **Drink questions:** m10-02, m10-10 to m10-14 and m10-30. No explanation gives another question's answer. There are only mild links: m10-10's "haven't eaten" and m10-02's equivalence lean toward m10-11's key, and m10-12's 1-ounce key rules out m10-02's liquor option. No change.

### Still open from the first pass

- README: "Nine study sections" and "content/m1.json … m9.json".
- decisions.md: "school-bus first-offense penalty: bullet only" (m9-33 now tests it).

Source added: [MGL c.90 §24](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90/Section24).

## Third pass

Method: I re-read both files in full. Compared with git HEAD, carried-over questions still differ only in the planned explanation edits, and only m9 bullets 5 and 8 differ. The validator reports 0 errors (both warnings are in m8). No explanation or bullet shares a run of 7 or more words with the manual, no key is the longest option by more than 1.3 times, and no new stem is near the duplicate threshold (closest pair: m10-32 and m10-35 at 0.79). The second-pass fixes to m9-29, m10-21, m10-31 and m10-32 are in. README and decisions.md are not (see the end of this section).

### OUI fine and prison rows (p.61, read again at 200 dpi)

The table gives these fines and prison terms:

| Offense | Fine | Prison term |
| --- | --- | --- |
| First | $500–$5,000 | maximum 2 1/2 years |
| Second | $600–$10,000 | minimum 30 days, maximum 2 1/2 years |
| Third (Felony) | $1,000-$15,000 | minimum 150 days, maximum 5 years |
| Fourth (Felony) | $1,500–$25,000 | minimum 1 year, maximum 5 years |
| Fifth (Felony) | $2,000-$50,000 | minimum 2 years, maximum 5 years |

A script mapped all 20 options in m10-21 and m10-32 to m10-35 to these rows. Every option matches its row's figures exactly, and every key is the right row:

- **m10-21** OK. First offense. Its options are the second, first, third and fifth rows.
- **m10-32** OK. Second offense. Its options are the first, second, fourth and third rows.
- **m10-33** OK. Third offense. Its options are the second, fifth, third and fourth rows.
- **m10-34** OK. Fourth offense. Its options are the third, first, fifth and fourth rows.
- **m10-35** OK. Fifth offense. Its options are the fourth, fifth, second and third rows.

Each explanation states only its own row, and each is volatile. No option uses a current-law figure that differs from the manual: the statute's 60 and 180 days appear in no option.

### Other new or changed questions

- **m9-36** OK. p.53: "Many motor vehicle crashes are caused by improper turns." The manual recommends all three distractors: p.18 "It is recommended that a rider change gears prior to entering a turn", p.20 "keep the headlight on at all times", and p.18 "Use both brakes every time you slow down or stop." The manual's other named crash causes, speeding (m8-27) and not being seen (m4-02), are not options, so there is only one defensible answer. The explanation's six steps match p.53, and its "signal early" gives no distances, so m9-09 is not given away.
- **m9-37** OK. p.56: "Because only a few states in America have traffic rotaries (traffic circles), many drivers are unfamiliar with rotaries' right-of-way rules." The explanation does not say who has the right-of-way, so m9-13 is not given away.
- **m10-15** OK. Neither the stem nor the explanation gives the year now. p.60: "This new law substantially increases the penalties and administrative sanctions for OUI offenses."
- **m10-36** OK. p.60: "In October 2005, Massachusetts passed Melanie's Law". Neither it nor m10-15 shows the other's answer, though bullet 5 gives both, which is fine for a summary. volatile false is right.
- **m10-19, m10-20** OK. Each explanation now gives only its own suspension, so neither helps with the fine and prison questions.

### Give-aways across m10 (36 questions)

- **Fine and prison set (m10-21, m10-32 to m10-35):** no stem or explanation states another question's answer. The row-sharing cost is larger here than on the suspension ladder. Each question's three distractors are rows that are keys elsewhere in the set, so in a section test the last of the five a learner meets can always be answered by elimination alone. Each one has a 1-in-4 chance of being that free, so a section test gives away about 1.25 of the five on average and never fewer than one. Cutting to three questions (for example first, third and fifth) would end the outright give-away, at the cost of not testing the second and fourth rows. Keeping all five follows your coverage decision, so I am not recommending a change.
- **Suspension ladder and the other OUI-table questions (m10-07, m10-17 to m10-20, m10-22, m10-31):** the same as in the second pass. The fine and prison questions and the suspension questions do not leak into each other, and nothing mentions felony status outside m10-31 and bullet 6.
- **Drink questions and the rest of m10:** unchanged, with no give-aways.
- p.61 now carries 12 of the section's 36 questions.

### Still open

- README still says "Nine study sections" and "content/m1.json … m9.json".
- decisions.md still says "school-bus first-offense penalty: bullet only", although m9-33 now tests it.
