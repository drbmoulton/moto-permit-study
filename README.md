# Class M Permit Prep

A study app for the Massachusetts Class M (motorcycle) learner's permit knowledge test: 25 multiple-choice questions, 18 correct to pass, 25 minutes. Every question is written from the official [Massachusetts RMV Motorcycle Manual](https://www.mass.gov/doc/motorcycle-manual/download) (2015 edition), which the test is drawn from. No AI runs in the app.

## What's in it

- **Nine study sections** that follow the manual, each with key points, the manual pages to read, and a section test that shows the answer and explanation after every question.
- **Practice tests** that match the real one: 25 questions drawn from every section in proportion to its share of the question bank, a 25-minute timer, no feedback until the end, and pass at 18. The results screen breaks the score down by section and lets you review every question.
- **Quick 10**: a short mixed set, starting with questions you got wrong and ones you haven't seen.
- **Missed questions**: everything you got wrong the last time you saw it, overall or per section.
- **The manual itself**: every answer cites its page, and the page opens inside the app.

Answers that depend on fees, fines, suspension lengths or speed figures that may have changed since 2015 carry a yellow caution note. The app teaches what the manual says, since that is what the test is based on, and points to mass.gov for current rules.

## Where progress is saved

| Where it runs | Progress |
| --- | --- |
| Claude artifact, opened by someone who can save in it (the owner, or a person invited by email as an Editor while the artifact has no public link) | Saved to that person's Claude account and synced across their devices |
| Claude artifact opened through a public link or as a Viewer | Saved in that browser only |
| GitHub Pages or any other static host | Saved in that browser only |

The footer of the home screen always says which one is active. A practice test in progress is kept in the browser, so it can be resumed after a reload; its timer keeps running.

## Layout

```
content/m1.json … m9.json   question bank, one file per section (source of truth)
src/app.html                 the app (HTML, CSS, JS); __BANK__ is replaced at build time
manual/                      the manual PDF and one image per page (pages/pNN.webp, by PDF page)
scripts/build.py             validates the bank, then builds dist/artifact.html and index.html
scripts/test_logic.js        checks scoring, question picking and progress merging
review/                      independent review notes for each section and the app; decisions.md records how open questions were settled
```

Each question looks like this:

```json
{
  "id": "m6-17",
  "q": "Question text",
  "options": ["A", "B", "C", "D"],
  "answer": 2,
  "explanation": "Why, in a sentence or two.",
  "page": 49,
  "volatile": false
}
```

`page` is the printed page number in the manual. The PDF page is that number plus 7. `answer` is the index of the correct option; options are shuffled each time a question is shown, so never write "all of the above".

## Editing questions

1. Edit the section's file in `content/`. Never reorder an existing question's options or change its `answer`: saved practice tests store the index of the option chosen. To rewrite a question substantially, remove it and add the new one under the section's next unused id; the app ignores ids that no longer exist.
2. Run `python3 scripts/build.py`. It refuses to build if a question is malformed (wrong option count, answer out of range, a page outside the section, a duplicate id) and warns about likely duplicates or answers that give themselves away by length.
3. Run `node scripts/test_logic.js`.
4. Commit `content/`, `index.html` and `dist/artifact.html`.

## Hosting

- **Claude artifact**: `dist/artifact.html` is published with the `manual/` files alongside it, declaring the `user` and `db` capabilities (without them everyone saves in the browser only).
- **GitHub Pages**: in the repository's Settings → Pages, deploy from the `main` branch, root folder. `index.html` is the complete page.

Not affiliated with the Massachusetts RMV.
