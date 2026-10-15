#!/usr/bin/env python3
"""Check a PaperSim paper JSON before handing it over.

    python3 scripts/check_paper.py paper.json [--total 100]

Errors (exit code 1): invalid JSON, missing text/marks, LaTeX backslashes lost to JSON escaping
("\\frac" written with one backslash), unbalanced $ or \\ce{ braces, ragged tables, bad resources.
Then prints a summary: questions, marks per criterion/task, resources, and the files to supply.
"""
import json
import re
import sys
from collections import Counter

CONTROL = {"\f": "\\f (e.g. \\frac)", "\b": "\\b (e.g. \\beta)", "\r": "\\r (e.g. \\rightarrow, \\rho)"}
TAB_CMDS = r"(?:imes|ext|extbf|extrm|heta|au|an|anh|frac|ilde|o|op|riangle|herefore)(?![a-zA-Z])"
NL_CMDS = r"(?:u|eq|abla|ot|eg|leq|geq|ewline)(?![a-zA-Z])"
BUILTINS = {"periodic-table"}
errors, warnings = [], []


def check_text(where, s):
    if not isinstance(s, str) or not s:
        return
    for ch, name in CONTROL.items():
        if re.search(re.escape(ch) + "[a-zA-Z]", s):
            errors.append(f"{where}: a LaTeX command lost its backslash ({name}). Write two backslashes in JSON.")
    if re.search("\t" + TAB_CMDS, s):
        errors.append(f"{where}: a LaTeX command lost its backslash (\\t, e.g. \\times / \\text / \\theta).")
    body = re.sub(r"\\\$", "", s)
    for m in re.finditer(r"\$\$(.+?)\$\$|\$([^$]+)\$", body, re.S):
        tex = m.group(1) or m.group(2)
        if re.search("\n" + NL_CMDS, tex):
            errors.append(f"{where}: a line break inside maths where \\nu / \\neq was meant. Write \"\\\\nu\".")
        if tex.count("{") != tex.count("}"):
            errors.append(f"{where}: unbalanced {{ }} in ${tex[:40]}$")
    rest = re.sub(r"\$\$.+?\$\$", "", body, flags=re.S)
    rest = re.sub(r"(?<![A-Za-z0-9])(?:[A-Z]{1,3})?\$(?=\d[\d,.]*(?:[\s)]|$))(?![^$]*[\\^_{}=])", "", rest)  # money: US$997, $5
    singles = rest.count("$")
    if singles % 2:
        warnings.append(f"{where}: odd number of $ signs. Unclosed maths? (A money sign next to maths is \\\\$.)")


def check_table(where, t):
    if not isinstance(t, dict) or not isinstance(t.get("rows"), list) or not t["rows"]:
        errors.append(f"{where}: a table needs \"rows\": [[...], ...]")
        return
    width = max([len(t.get("headers") or [])] + [len(r) for r in t["rows"] if isinstance(r, list)])
    for i, r in enumerate(t["rows"], 1):
        if not isinstance(r, list):
            errors.append(f"{where}: row {i} is not a list")
        elif len(r) != width:
            errors.append(f"{where}: row {i} has {len(r)} cells, the table is {width} wide")
        else:
            for c in r:
                check_text(f"{where} cell", c if isinstance(c, str) else "")
    for h in t.get("headers") or []:
        check_text(f"{where} header", h if isinstance(h, str) else "")
    check_text(f"{where} caption", t.get("caption"))


def as_list(v):
    return [] if v in (None, "") else v if isinstance(v, list) else [v]


def image_srcs(v):
    for im in as_list(v):
        src = im if isinstance(im, str) else (im or {}).get("src", "")
        if src and not re.match(r"^(data:|https?:)", src):
            yield src


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    path, total = args[0], None
    if "--total" in args:
        total = float(args[args.index("--total") + 1])
    try:
        paper = json.load(open(path, encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit(f"ERROR invalid JSON: {e.msg} at line {e.lineno}, column {e.colno}")
    qs = paper.get("questions")
    if not isinstance(qs, list) or not qs:
        sys.exit('ERROR "questions" must be a non-empty list')

    files, ids = set(), Counter()
    by_crit, by_task, marks_total = Counter(), Counter(), 0
    md_img = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+)")
    for i, q in enumerate(qs, 1):
        qid = str(q.get("id", i))
        where = f"Q{qid}"
        ids[qid] += 1
        if not isinstance(q.get("text"), str) or not q["text"].strip():
            errors.append(f"{where}: missing \"text\"")
        if not isinstance(q.get("marks"), (int, float)) or q["marks"] < 0:
            errors.append(f"{where}: \"marks\" must be a number")
        else:
            marks_total += q["marks"]
            by_crit[q.get("criterion") or "-"] += q["marks"]
            by_task[q.get("task") or "-"] += q["marks"]
        for f in ("context", "text", "markScheme", "imageCaption"):
            check_text(f"{where} {f}", q.get(f))
            files.update(m for m in md_img.findall(q.get(f) or "") if not m.startswith(("data:", "http")))
        for k, o in enumerate(q.get("options") or []):
            check_text(f"{where} option {chr(65 + k)}", o)
        if q.get("options") and q.get("correctOption") is not None:
            c = q["correctOption"]
            n = c if isinstance(c, int) else "ABCDEFGHIJ".find(str(c).upper())
            if not 0 <= n < len(q["options"]):
                errors.append(f"{where}: correctOption {c!r} is not one of the options")
        for key in ("table", "tables", "markSchemeTable", "markSchemeTables"):
            for t in as_list(q.get(key)):
                check_table(f"{where} {key}", t)
        for key in ("image", "images", "markSchemeImage", "markSchemeImages"):
            files.update(image_srcs(q.get(key)))
            for im in as_list(q.get(key)):
                if isinstance(im, dict) and not im.get("alt"):
                    warnings.append(f"{where} {key}: image without \"alt\" text")
        if q.get("image") and not q.get("imageAlt") and isinstance(q.get("image"), str):
            warnings.append(f"{where}: image without \"imageAlt\"")
    for qid, n in ids.items():
        if n > 1:
            errors.append(f"id \"{qid}\" is used {n} times")

    res_names = []
    for k, r in enumerate(as_list(paper.get("resources")), 1):
        where = f"Resource {k}"
        if isinstance(r, str):
            r = {"builtin": r} if r.strip().lower() in BUILTINS else {"src": r}
        if not isinstance(r, dict):
            errors.append(f"{where}: must be \"periodic-table\", a file path or an object")
            continue
        if "builtin" in r:
            if r["builtin"] not in BUILTINS:
                errors.append(f"{where}: unknown built-in {r['builtin']!r} (available: {', '.join(BUILTINS)})")
            else:
                res_names.append(r.get("title") or "Periodic table")
        elif r.get("src"):
            if not re.match(r"^(data:|https?:)", r["src"]):
                files.add(r["src"])
            res_names.append(r.get("title") or r["src"])
        elif any(r.get(x) for x in ("content", "table", "tables", "images", "image")):
            check_text(f"{where} content", r.get("content"))
            for t in as_list(r.get("table")) + as_list(r.get("tables")):
                check_table(f"{where} table", t)
            files.update(image_srcs(r.get("images") or r.get("image")))
            res_names.append(r.get("title") or where)
        else:
            errors.append(f"{where}: needs \"builtin\", \"src\" or \"content\"")
    if total is not None and abs(marks_total - total) > 1e-9:
        errors.append(f"marks add up to {marks_total:g}, expected {total:g}")

    print(f"{paper.get('title', '(no title)')}: {len(qs)} questions, {marks_total:g} marks, "
          f"{paper.get('durationMinutes', 120)} min")
    if len(by_crit) > 1 or "-" not in by_crit:
        print("  by criterion: " + ", ".join(f"{c} {m:g}" for c, m in sorted(by_crit.items())))
    if len(by_task) > 1:
        print("  by task: " + "; ".join(f"{t} {m:g}" for t, m in by_task.items()))
    print("  resources: " + (", ".join(res_names) or "none"))
    if files:
        print("  files the user must supply next to the JSON (or in the zip): " + ", ".join(sorted(files)))
    for w in warnings:
        print("WARNING " + w)
    for e in errors:
        print("ERROR " + e)
    print("OK" if not errors else f"{len(errors)} error(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
