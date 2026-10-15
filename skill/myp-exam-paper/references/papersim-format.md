# PaperSim paper JSON: equations, images and tables

A paper is one JSON file. Each question needs only `text` and `marks`. Every text field
(`context`, `text`, `markScheme`, MCQ `options`, captions, table cells) is **Markdown with maths**.
The full schema is in [`paper.schema.json`](paper.schema.json), and a worked example is in
[`sample-rich-paper.json`](sample-rich-paper.json).

```json
{
  "title": "Chemistry: Rates of Reaction",
  "subject": "Sciences",
  "durationMinutes": 60,
  "questions": [
    {
      "id": "1a", "task": "Task 1: Equations", "criterion": "A",
      "marks": 2, "commandTerm": "Write",
      "context": "Magnesium reacts with dilute hydrochloric acid.",
      "text": "Write the balanced symbol equation, **including state symbols**.",
      "markScheme": "$\\ce{Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)}$\n\n- correct formulae [1]\n- balanced with state symbols [1]"
    }
  ]
}
```

## 1. The one rule: double every backslash

JSON uses `\` for its own escapes, so **every LaTeX backslash is written twice** inside a JSON string.

| You want (LaTeX) | Write in the JSON string |
|---|---|
| `\ce{H2O}` | `"$\\ce{H2O}$"` |
| `\frac{1}{2}` | `"$\\frac{1}{2}$"` |
| `\sqrt{2gh}` | `"$\\sqrt{2gh}$"` |
| `\times`, `\theta`, `\beta`, `\nu`, `\rightarrow` | `"\\times"`, `"\\theta"`, `"\\beta"`, `"\\nu"`, `"\\rightarrow"` |
| a line break | `"\n"` (one backslash: this is a real newline) |
| a blank line (new paragraph) | `"\n\n"` |
| a double quote | `\"` |
| a literal dollar next to maths | `"\\$"` |

A single backslash doesn't fail loudly. `"\frac"` turns into a form-feed character followed by
"rac", and `"\nu"` turns into a line break followed by "u". PaperSim repairs the cases it can
recognise safely (`\f`, `\b`, `\r`, `\t…`) and warns about the rest when the paper loads. Still,
always double the backslashes.

## 2. Equations

| Delimiter | Use |
|---|---|
| `$ ... $` | inline maths |
| `$$ ... $$` | block maths, centred on its own line (long block equations shrink to fit narrow screens) |
| `$\ce{ ... }$` | chemistry (mhchem), inline or in `$$ $$` |
| `\( \)`, `\[ \]` | still supported (older papers) |

**Chemistry (`\ce`)**

| Notation | Example | JSON |
|---|---|---|
| balanced equation | Mg + 2HCl → MgCl₂ + H₂ | `"$\\ce{Mg(s) + 2HCl(aq) -> MgCl2(aq) + H2(g)}$"` |
| subscripts | numbers after an element are subscripts automatically | `"$\\ce{H2SO4}$"` |
| charges | Fe³⁺, SO₄²⁻, Na⁺ | `"$\\ce{Fe^{3+}}$"`, `"$\\ce{SO4^{2-}}$"`, `"$\\ce{Na+}$"` |
| states | `(s) (l) (g) (aq)` | written right after the formula |
| equilibrium arrow | ⇌ | `"$$\\ce{N2 + 3H2 <=> 2NH3}$$"` |
| other arrows | | `->`, `<-`, `<->`, `->[\\text{heat}]` (with a label) |
| precipitate / gas | ↓ ↑ | `v` and `^` with spaces around them |
| hydrates | CuSO₄·5H₂O | `"$\\ce{CuSO4.5H2O}$"` |

**Physics and maths**

| Notation | JSON |
|---|---|
| fractions | `"$\\frac{\\Delta v}{\\Delta t}$"` (`\\dfrac` for full size inline) |
| roots | `"$\\sqrt{2gh}$"`, `"$\\sqrt[3]{x}$"` |
| exponents and indices | `"$x^{2}$"`, `"$R_{1}$"`, `"$3.0 \\times 10^{8}$"` |
| Greek letters | `"$\\lambda \\ \\theta \\ \\Omega \\ \\varepsilon \\ \\Delta \\ \\mu$"` |
| units (upright, thin space) | `"$9.81\\ \\text{m s}^{-2}$"`, `"$12\\ \\Omega$"` |
| vectors | `"$\\vec{F}$"`, `"$\\mathbf{v}$"` |
| degrees | `"$30^{\\circ}$"` |
| equations with words | `"$R_\\text{total} = R_1 + R_2$"` |

**Dollar signs used as money.** PaperSim reads `$...$` as maths only when the opening `$` is
followed by a non-space and the closing `$` is not followed by a digit. "US$997 billion"
therefore stays text. Write a literal `$` directly before or after maths as `\\$`.

**Bad LaTeX doesn't crash the paper.** It shows the raw text with a red wavy underline, and it is
listed when the paper loads.

## 3. Images

```json
"image": "images/circuit.png",
"imageAlt": "Series circuit with a cell, two resistors and an ammeter",
"imageCaption": "Figure 2: a series circuit"
```

- `image` / `images` takes one image or a list of images. Each one is a string or
  `{"src", "alt", "caption", "width"}`.
- `src` can be:
  - a **relative path** (`images/fig1.png`)
  - an **https URL**
  - a **data URI** (`data:image/png;base64,...` or `data:image/svg+xml,...`)
  - `javascript:` and `file:` links are refused
- `width` is optional (`300`, `"300px"` or `"60%"`). Images never exceed the column width, and in
  print they are kept at 85 mm tall or less and never split across a page.
- `imageAlt` and `imageCaption` apply to the first image. Always give alt text.
- Images in the mark scheme go in `markSchemeImage` / `markSchemeImages`, with
  `markSchemeImageAlt` / `markSchemeImageCaption`.
- Inline Markdown also works anywhere: `![Graph of v against t](images/vt.png)`.
- `"image": ""` (older papers) means no image.

**Loading papers with image files.** In *Load paper*, you can:
- drop the **folder** that holds the JSON and its `images/` folder
- drop or choose a **.zip** of that folder
- pick the JSON, then **Attach images…**

Paths are matched relative to the JSON file, and then by file name alone. Attached images are
remembered in this browser until you load another paper. Any image that can't be found is listed
when the paper loads.

## 4. Tables

**Option A: Markdown (GFM) table** inside `context`, `text` or `markScheme`. Rows are separated
by `\n`, and there must be a blank line (`\n\n`) before the table:

```json
"context": "Data booklet extract:\n\n| Quantity | Value |\n|---|---|\n| Molar gas volume at RTP | $24.0\\ \\text{dm}^{3}\\,\\text{mol}^{-1}$ |\n| $M_r$ of $\\ce{CaCO3}$ | 100.1 |"
```

Alignment works with `|:---|`, `|:---:|` and `|---:|`. A `|` inside maths (`$|x|$`) does not
split the cell.

**Option B: structured table** (best for data tables, and easier to generate without mistakes):

```json
"table": {
  "caption": "Table 1: volume of $\\ce{CO2}$ collected",
  "headers": ["Time / s", "Volume of $\\ce{CO2}$ / $\\text{cm}^{3}$"],
  "rows": [["0", "0"], ["30", "24"], ["60", "39"]]
}
```

- `table` / `tables` takes one table or a list. The tables appear under the context.
- For the mark scheme, use `markSchemeTable` / `markSchemeTables`.
- Every cell can use Markdown, `$maths$` and `\ce{}`.
- Every row should have the same number of cells as `headers`. Short rows are padded and listed
  when the paper loads.

Tables are drawn as exam-style ruled tables. They scroll sideways on a phone and print with black
borders.

---

## 5. Resources (periodic table, formula sheets, data booklets)

Resources open from the **Resources** tab on the right edge of the exam, or from the Resources
button in the toolbar. The drawer stays open beside the paper while the student answers, like the
resources panel in on-screen exams. Each resource gets its own tab in the drawer. Add them at the
top level of the paper:

```json
"resources": [
  "periodic-table",
  {
    "title": "Physics formulae",
    "content": "### Electricity\n\n| Quantity | Equation |\n|---|---|\n| Power | $P = IV = I^{2}R$ |\n| Charge | $Q = It$ |\n\nGravitational field strength $g = 9.8\\ \\text{N kg}^{-1}$"
  },
  {
    "title": "Common ions",
    "table": {"headers": ["Positive ions", "Negative ions"], "rows": [["$\\ce{Na+}$", "$\\ce{Cl-}$"]]}
  },
  { "title": "Data booklet", "src": "resources/data-booklet.pdf" }
]
```

| Kind | How to write it | Notes |
|---|---|---|
| Built-in periodic table | `"periodic-table"` | All 118 elements: atomic number, symbol and relative atomic mass (IUPAC values to 2 d.p.). Students can click an element to see its name. |
| A sheet written in the JSON | `{"title", "content", "table"/"tables", "images"}` | `content` is Markdown with `$maths$` and `\ce{}`, exactly like question text. Best for formula sheets and data tables. |
| A file you provide | `{"title", "src"}` | A **PDF** or image: a relative path (attach it when loading: folder, zip or "Attach images / PDFs…"), an https URL, or a data URI. |

- Link to a resource from a question: `"text": "Use the [periodic table](#resource:periodic-table) …"`.
  Use `#resource:<id>`, where the id is the resource's `id` or its title in lowercase with hyphens
  (for example `#resource:physics-formulae`).
- Students can also add their own file during the exam with **+ Add → PDF or image**. It is kept
  with the paper until another paper is loaded.
- Only include resources that the real exam would give. For example, MYP sciences give a periodic
  table and relevant equations, while maths papers give a formula sheet. Formula sheets list
  formulae, never answers.

## 6. Ready-to-paste block for the paper-generation prompt

```text
OUTPUT FORMAT: PaperSim JSON (follow exactly)

Output ONE valid JSON object and nothing else (no comments, no trailing commas):
{"title": str, "subject": str, "durationMinutes": number, "gradeBoundaries": {"1":0,...,"7":N} (optional),
 "resources": [...] (optional, see RESOURCES),
 "questions": [ {"id": "1a", "task": "Task 1: ...", "criterion": "A", "marks": number,
   "commandTerm": "Calculate", "context": str (optional), "text": str (required),
   "options": [str, ...] + "correctOption": "B" (multiple choice only),
   "image"/"images", "imageAlt", "imageCaption" (optional), "table"/"tables" (optional),
   "markScheme": str, "markSchemeTable"/"markSchemeImages" (optional) } ] }

TEXT: every text field is Markdown: **bold**, *italic*, "- " bullet lines, "\n" for a line break,
"\n\n" between paragraphs and before a list or table. Show marks in the mark scheme as [1].

JSON ESCAPING (most important):
- Write EVERY LaTeX backslash TWICE inside JSON strings: "$\\frac{1}{2}$", "$\\ce{H2O}$",
  "$\\times$", "$\\theta$", "$\\nu$", "$\\rightarrow$", "$\\text{m s}^{-1}$".
  A single backslash is wrong: "\frac" becomes a form feed and "\nu" becomes a newline.
- "\n" (one backslash) is ONLY for real line breaks. Escape double quotes as \".
- A literal dollar sign next to maths is "\\$". Money like "US$5 billion" can stay as it is.

EQUATIONS:
- Inline maths $...$, block maths $$...$$. Never use Unicode look-alikes (x², H₂O, →) in place of LaTeX.
- ALL chemistry goes in \ce: "$\\ce{2H2(g) + O2(g) -> 2H2O(l)}$", ions "$\\ce{Fe^{3+}}$",
  "$\\ce{SO4^{2-}}$", "$\\ce{Na+}$", equilibrium "$$\\ce{N2 + 3H2 <=> 2NH3}$$",
  state symbols (s) (l) (g) (aq) directly after the formula.
- Physics/maths: "$\\frac{a}{b}$", "$\\sqrt{x}$", "$x^{2}$", "$R_{1}$", "$3.0 \\times 10^{8}$",
  Greek "$\\lambda$", "$\\Omega$", "$\\Delta$", vectors "$\\vec{F}$", units upright with a space
  "$9.81\\ \\text{m s}^{-2}$", degrees "$30^{\\circ}$".
- After "$", the next character must not be a space. Before the closing "$" there must not be a
  space, and the closing "$" must not be followed directly by a digit.

TABLES:
- For data tables use the structured field:
  "table": {"caption": "Table 1: ...", "headers": ["Time / s", "Volume / $\\text{cm}^{3}$"],
            "rows": [["0","0"],["30","24"]]}
  Every row has exactly as many cells as headers, and every cell is a string.
- Short tables inside text may use a Markdown table preceded by "\n\n":
  "| A | B |\n|---|---|\n| 1 | 2 |"
- Mark scheme tables use "markSchemeTable" (same shape) or a Markdown table in "markScheme".

IMAGES:
- Only include an image if the question needs it. Use "image": "images/<descriptive-name>.png"
  (relative path; the file is supplied separately), an https URL, or a data:image/svg+xml URI for
  a simple diagram you draw yourself. ALWAYS add "imageAlt" (what the image shows, for a screen
  reader) and "imageCaption" ("Figure 1: ..."), and refer to it in the text ("Figure 1 shows...").
- When there is no image, leave the image fields out entirely.
- Mark-scheme images use "markSchemeImages": [{"src": "...", "alt": "...", "caption": "..."}].

RESOURCES (opened from the Resources tab beside the exam):
- Chemistry/science papers that need relative atomic masses: include "periodic-table" (built in;
  never type out a periodic table yourself).
- Formula sheets and data sheets: {"title": "Physics formulae", "content": "### Electricity\n\n| Quantity | Equation |\n|---|---|\n| Power | $P = IV$ |"}
  Markdown + LaTeX, same escaping rules. Use "table": {...} for data such as common ions or constants.
  List only what the real exam provides (formulae, constants, data), never answers or worked methods.
- A file the user gives you (PDF or image): {"title": "Data booklet", "src": "resources/<file-name>.pdf"}
  and tell the user to put that file in a resources/ folder next to the JSON (or in the zip).
  If it is short and text-based, transcribe it into "content" instead so it renders crisply.
- Link from a question when useful: "Use the [periodic table](#resource:periodic-table) ...".

Before finishing, check: the JSON parses; every backslash inside a string is doubled; every \ce{...}
and every {...} is closed; every table row has the right number of cells.
```
