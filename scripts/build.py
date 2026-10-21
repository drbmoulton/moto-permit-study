#!/usr/bin/env python3
"""Validate the question bank and build the study app.

Outputs
  dist/artifact.html  page body for the Claude artifact (the artifact host adds <html> and <head>)
  index.html          complete page for GitHub Pages or any static host

Usage
  python3 scripts/build.py           validate, then build
  python3 scripts/build.py --check   validate only
  python3 scripts/build.py --check --only m4   validate one section
"""
import difflib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODULE_IDS = [f"m{i}" for i in range(1, 10)]
QUESTION_KEYS = {"id", "q", "options", "answer", "explanation", "page", "volatile"}
BANNED = re.compile(r"\b(all|none|both) of the above\b|\bboth [a-d] and [a-d]\b|\bneither [a-d] nor [a-d]\b", re.I)
FIRST_PAGE, LAST_PAGE = 1, 64  # printed page numbers in the 2015 manual


def validate(only=None):
    errors, warnings, modules = [], [], []
    seen_ids = set()
    for mid in ([only] if only else MODULE_IDS):
        path = ROOT / "content" / f"{mid}.json"
        try:
            d = json.loads(path.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            errors.append(f"{path.name}: cannot parse ({e})")
            continue
        where = path.name
        if d.get("id") != mid:
            errors.append(f"{where}: id should be {mid!r}")
        if not isinstance(d.get("title"), str) or not d["title"].strip():
            errors.append(f"{where}: missing title")
        pages = d.get("manualPages")
        if not (isinstance(pages, list) and pages and all(isinstance(p, int) and FIRST_PAGE <= p <= LAST_PAGE for p in pages)):
            errors.append(f"{where}: manualPages must list printed pages {FIRST_PAGE}-{LAST_PAGE}")
            pages = []
        summary = d.get("summary")
        if not (isinstance(summary, list) and summary and all(isinstance(s, str) and s.strip() for s in summary)):
            errors.append(f"{where}: summary must be a non-empty list of sentences")
        qs = d.get("questions")
        if not isinstance(qs, list) or not qs:
            errors.append(f"{where}: no questions")
            qs = []
        longest_tells = 0
        for q in qs:
            qid = q.get("id", "?")
            w = f"{where} {qid}"
            missing = QUESTION_KEYS - set(q)
            extra = set(q) - QUESTION_KEYS
            if missing:
                errors.append(f"{w}: missing {sorted(missing)}")
                continue
            if extra:
                warnings.append(f"{w}: unexpected keys {sorted(extra)} (dropped from the build)")
            if not re.fullmatch(rf"{mid}-\d{{2}}", str(qid)):
                errors.append(f"{w}: id should look like {mid}-01")
            if qid in seen_ids:
                errors.append(f"{w}: duplicate id")
            seen_ids.add(qid)
            if not isinstance(q["q"], str) or not q["q"].strip():
                errors.append(f"{w}: empty question")
            opts = q["options"]
            if not (isinstance(opts, list) and len(opts) == 4 and all(isinstance(o, str) and o.strip() for o in opts)):
                errors.append(f"{w}: needs exactly 4 non-empty options")
                continue
            if len({o.strip().lower() for o in opts}) != 4:
                errors.append(f"{w}: options repeat")
            for o in opts:
                if BANNED.search(o):
                    errors.append(f"{w}: option {o!r} breaks when options are shuffled")
            if not (isinstance(q["answer"], int) and 0 <= q["answer"] <= 3):
                errors.append(f"{w}: answer must be 0-3")
                continue
            if not isinstance(q["explanation"], str) or not q["explanation"].strip():
                errors.append(f"{w}: empty explanation")
            if not isinstance(q["page"], int):
                errors.append(f"{w}: page must be a printed page number")
            elif pages and q["page"] not in pages:
                errors.append(f"{w}: page {q['page']} is outside this section's manualPages")
            if not isinstance(q["volatile"], bool):
                errors.append(f"{w}: volatile must be true or false")
            lens = [len(o) for o in opts]
            if lens[q["answer"]] > 1.3 * max(l for i, l in enumerate(lens) if i != q["answer"]):
                longest_tells += 1
        if qs and longest_tells / len(qs) > 0.25:
            warnings.append(f"{where}: correct option is clearly the longest in {longest_tells} of {len(qs)} questions")
        modules.append({
            "id": mid,
            "title": d.get("title", mid),
            "manualPages": pages,
            "summary": summary or [],
            "questions": [{k: q[k] for k in ("id", "q", "options", "answer", "explanation", "page", "volatile")} for q in qs if QUESTION_KEYS <= set(q)],
        })

    flat = [(m["id"], q) for m in modules for q in m["questions"]]
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            a, b = flat[i][1], flat[j][1]
            r = difflib.SequenceMatcher(None, a["q"].lower(), b["q"].lower()).ratio()
            if r > 0.82:
                warnings.append(f"possible duplicate ({r:.2f}): {a['id']} / {b['id']}")
    return modules, errors, warnings


def build(modules):
    bank = {"source": "Massachusetts RMV Motorcycle Manual, 2015 edition", "modules": modules}
    data = json.dumps(bank, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    src = (ROOT / "src" / "app.html").read_text(encoding="utf-8")
    if src.count("__BANK__") != 1:
        sys.exit("src/app.html must contain the __BANK__ placeholder exactly once")
    page = src.replace("__BANK__", data)

    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "artifact.html").write_text(page, encoding="utf-8")

    m = re.search(r"<!--HEAD-->(.*?)<!--/HEAD-->", page, re.S)
    if not m:
        sys.exit("src/app.html must wrap its head content in <!--HEAD--> ... <!--/HEAD-->")
    head, body = m.group(1).strip(), (page[:m.start()] + page[m.end():]).strip()
    full = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
        "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
        "img{max-width:100%}[hidden]{display:none!important}</style>\n"
        f"{head}\n</head>\n<body>\n{body}\n</body>\n</html>\n"
    )
    (ROOT / "index.html").write_text(full, encoding="utf-8")
    return len(page.encode("utf-8"))


def main():
    only = None
    if "--only" in sys.argv:
        i = sys.argv.index("--only")
        only = sys.argv[i + 1] if i + 1 < len(sys.argv) else None
        if only not in MODULE_IDS:
            sys.exit(f"--only takes one of {', '.join(MODULE_IDS)}")
        if "--check" not in sys.argv:
            sys.exit("--only can only be used with --check")
    modules, errors, warnings = validate(only)
    total = sum(len(m["questions"]) for m in modules)
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    print(f"{total} questions in {len(modules)} sections; {len(errors)} errors, {len(warnings)} warnings")
    if errors:
        sys.exit(1)
    if "--check" in sys.argv:
        return
    size = build(modules)
    print(f"built dist/artifact.html and index.html ({size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
