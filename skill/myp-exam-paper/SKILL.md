---
name: "myp-exam-paper"
description: "Write MYP5 exam papers in the style of IB MYP eAssessment on-screen exams, built around the criteria the user gives, with a criterion-mapped markscheme. Can output a PaperSim JSON paper with equations, images, tables and exam resources (periodic table, formula sheets, data booklets). Use for any MYP mock, summative or criteria paper, or any paper to load into PaperSim."
---

# MYP5 exam paper writer

This skill writes papers the way the IB writes MYP5 on-screen examinations (eAssessment): one unifying context, stimulus-driven tasks, every question mapped to a criterion strand and an achievement band, and a markscheme that can be converted to MYP levels 0-8. The criteria the user gives are the spine of the paper. If the user pastes criteria text, that text overrides anything in this skill.

If the user wants the paper inside PaperSim (or asks for JSON, a practice/mock paper to sit on screen, or a paper "for PaperSim"), write it with this skill and output it exactly as described in section 4. Section 4 replaces the older `paper-sim` skill's format: follow section 4 wherever the two differ.

---

## 1. How real MYP5 papers are built (the patterns to copy)

**Overall shape**
- Two hours (some subjects 1h45). Externally marked, raw marks converted to a 1-7 grade.
- Always four criteria, equally weighted across the whole paper. The IB keeps any session within about 3 marks of its blueprint.
- The paper is split into 2-4 large *tasks*, not into one section per criterion. A task usually assesses 1-3 criteria; one criterion (often C or A) is spread across several tasks.
- Task sizes are unequal even though criteria are equal. Example: I&S tasks are roughly 26 / 18 / 36 marks.
- Approximate blueprints (treat as guides, not law):
  - Sciences (Bio/Chem/Phys/Integrated): 100 marks. Task 1 Knowing & understanding (A) ~25; Task 2 Investigation skills (B + C) ~50; Task 3 Applying science (D) ~25.
  - Mathematics / Extended maths: 100 marks, 25 per criterion. Task 1 Knowing & understanding (A), Task 2 Investigating patterns (B), Task 3 Applying maths in real life (D); Communicating (C) is earned across all three tasks.
  - Individuals & Societies (History, Geography, Integrated humanities): 80 marks, 20 per criterion. Tasks: Investigating (A+B, ~26), Communicating (A+C, ~18), Thinking critically (A+C+D, ~36).
  - Language & Literature: 80 marks, 20 per criterion. Task 1 unseen-text analysis incl. a short-answer block and a comparative response (A, B, D); Tasks 2-3 extended writing, one literary and one non-literary (B, C, D at ~10 each).

**Context and stimulus**
- The whole paper (or each task) hangs on one real-world scenario linked to a global context (identities & relationships, orientation in space & time, personal & cultural expression, scientific & technical innovation, globalisation & sustainability, fairness & development). Name the global context at the top of the paper.
- Questions are almost never naked recall. They sit under a stimulus: a data table, graph, diagram, photo description, short article, source extract, simulation description, map, timeline or experimental setup.
- Stimulus is short, realistic and invented but plausible (say "adapted" style is fine; never reproduce real copyrighted text). Include units, sample sizes, dates and sources for data.
- Later questions reuse earlier stimulus, so the paper feels like one investigation, not a quiz.

**Question ladder**
- Within each task, questions rise in demand: state/identify -> outline/describe -> explain/apply/interpret -> analyse/evaluate/justify/discuss.
- Top-band questions put known ideas into an *unfamiliar* situation. That is what separates a 7-8 from a 5-6.
- Mark tariffs: 1-4 marks for short items, 5-8 for structured items, 8-15 for one or two extended responses per paper.
- Every question shows its marks and uses one clear command term in bold.

**Subject-specific task patterns**
- *Sciences, Criterion A*: explain concepts, solve numerical problems, then analyse and evaluate an unfamiliar data set to make a scientifically supported judgment.
- *Sciences, Criteria B+C (investigation)*: give a scenario and research aim. Ask in order: state the problem/research question, write a hypothesis with scientific reasoning, identify independent/dependent/control variables and say how each is manipulated or controlled, design a safe method with sufficient data (range, repeats). Then hand over raw data: process it (means, uncertainties, rates), plot a graph (axes, units, line of best fit), interpret the trend with reasoning, evaluate the hypothesis, evaluate the method's validity, suggest improvements and extensions.
- *Sciences, Criterion D*: give 2-4 short sources about an application of science (e.g. a technology or policy). Ask for an extended response that explains how science addresses the problem, then discusses and evaluates implications across several factors (economic, environmental, ethical, social, political, cultural), reaches a concluding judgment, and references the provided sources.
- *Maths, Criterion B*: scaffolded pattern investigation. Complete a table -> describe the pattern in words -> write the general rule -> test it on a new case -> verify, then justify or prove why it works.
- *Maths, Criterion D*: an authentic problem (design, cost, optimisation, modelling). Identify relevant elements, choose a strategy, solve, justify degree of accuracy, judge whether the answer makes sense in context and state assumptions.
- *Maths, Criterion C*: no separate questions. Award marks for notation, labelled diagrams, moving between forms (table/graph/equation), and complete logical working, inside the other tasks.
- *I&S, Criterion B*: give an inquiry scenario. Ask for a research question with justified relevance, an action plan, methods/sources to collect data, and evaluation of the process and results.
- *I&S, Criterion D*: OPVL-style source analysis (origin, purpose, value, limitation), comparing perspectives, then a synthesising argument that uses the sources plus own knowledge.
- *I&S, Criterion C*: a communication product for a stated audience and purpose (report, article, briefing, infographic plan) with sources documented.
- *Language & Literature*: short answers on an unseen text (techniques, effect on audience), a comparative analysis of two texts, then creative/literary writing and non-literary writing tied to the session theme with a named audience, purpose and text type.

---

## 2. Criteria reference (use when the user only names the criteria)

Use the user's own criteria text if given. Otherwise use these MYP Year 5 strands.

**Sciences**
- A Knowing & understanding: explain scientific knowledge; apply knowledge to solve problems in familiar and unfamiliar situations; analyse and evaluate information to make scientifically supported judgments.
- B Inquiring & designing: explain a problem or question to test; formulate and explain a testable hypothesis with scientific reasoning; explain how to manipulate variables and collect sufficient data; design a scientific investigation.
- C Processing & evaluating: present collected and transformed data; interpret data and explain results with reasoning; evaluate validity of the hypothesis; evaluate validity of the method; explain improvements or extensions.
- D Reflecting on the impacts of science: explain how science is applied to address a problem; discuss and evaluate implications; communicate effectively; document sources.

**Mathematics / Extended mathematics**
- A Knowing & understanding: select appropriate maths; apply it successfully; solve problems correctly in a variety of contexts.
- B Investigating patterns: apply problem-solving techniques to discover complex patterns; describe patterns as general rules; prove or verify and justify rules.
- C Communicating: correct mathematical language; appropriate forms of representation; move between forms; complete, coherent, concise reasoning; logical structure.
- D Applying maths in real-life contexts: identify relevant elements; select strategies; apply them; justify the degree of accuracy; justify whether the solution makes sense.

**Individuals & Societies**
- A Knowing & understanding: terminology; knowledge of content and concepts through developed descriptions, explanations and examples.
- B Investigating: focused research question and its relevance; action plan; methods to collect relevant, varied information; evaluate process and results.
- C Communicating: style suited to audience and purpose; structure; document sources.
- D Thinking critically: discuss concepts, issues, models and theories; synthesise into well-supported arguments; analyse and evaluate sources (origin, purpose, value, limitations); interpret perspectives and implications.

**Language & Literature**
- A Analysing: content, context, language, structure, technique, style; effect of the creator's choices on audience; justify with examples and terminology; compare across texts.
- B Organizing: structures that serve context and intention; sustained, coherent, logical ideas; formatting/referencing suited to context.
- C Producing text: insight, imagination, sensitivity; deliberate stylistic choices; relevant details and examples.
- D Using language: varied vocabulary and sentence structures; register and style; grammar, syntax, punctuation; spelling.

**Language acquisition (e.g. Spanish, Marathi)**: A Listening, B Reading, C Speaking, D Writing, at the phase the user names. Scale text length and vocabulary to the phase. Listening and speaking items become scripts/prompts for a teacher or partner to read.

**Interdisciplinary, Design, others**: ask for or use the criteria text the user provides; do not guess strands.

**Achievement-level language (all subjects)**: 1-2 = state/list/limited; 3-4 = outline/familiar situations; 5-6 = describe/apply in familiar and suggest in unfamiliar/analyse; 7-8 = explain/apply in unfamiliar/analyse AND evaluate/justify. Design questions so every band is reachable.

---

## 3. Workflow

### Step 1: Inputs
Needed: subject, criteria to assess (and their strand text if the school's version differs), topics/unit, total marks, duration, and whether marks must convert to MYP levels 0-8. Optional: global context or theme, difficulty, output format (document or PaperSim JSON), and resources (periodic table, formula sheet or data booklet: the user may attach their own, or you make them; see 4.2).
If the subject, criteria and topics are given, build without asking. Defaults: 2 hours; eAssessment blueprint totals scaled to the criteria chosen (about 25 marks per science/maths criterion, 20 per I&S/L&L criterion); MYP5 end-of-year standard. Physics/chemistry: use g = 9.8 m/s² unless told otherwise.

### Step 2: Blueprint first (do not write questions yet)
Build a table: Task | Q | Criterion | Strand | Target band (1-2 / 3-4 / 5-6 / 7-8) | Command term | Marks | Stimulus used.
Rules:
- Every strand of every chosen criterion is hit at least once.
- Within each criterion, spread marks roughly 15-20% at band 1-2, 25-30% at 3-4, 25-30% at 5-6, 25-30% at 7-8. A paper with no 7-8 items cannot award a 7-8.
- Criteria are equal in marks overall (within ±3) unless the user sets weights.
- Pick one scenario and global context; list the stimuli (S1, S2...).

### Step 3: Write the stimuli
Short, precise, realistic. Data must be internally consistent and actually support the trend the questions expect (include one anomaly in investigation data for the evaluation questions). Describe images/diagrams in brackets if you can't draw them, or draw simple ones.

### Step 4: Write the questions
- Format: **Q2(b)** [4 marks] **Explain** ... Include criterion tag only in the markscheme, not on the student paper (unless the user's school prints criteria on papers).
- One command term per question, matching the band. Don't ask "explain and evaluate" in a 3-mark item.
- Extended responses state what a full answer includes (e.g. "In your answer, you should: ...") the way eAssessment prompts do, without giving answers away.
- No answers or hints leaking into later stimuli.

### Step 5: Markscheme
- Short items (1-4 marks): points-based. One mark per point, accepted alternatives, "do not accept" notes, ECF (error carried forward) rules for multi-step working, units and significant figures for calculations with full working.
- Structured and extended items (5+ marks): levelled markbands written with the criterion's band language, e.g. 0 / 1-2 / 3-4 / 5-6 / 7-8, each with indicative content.
- Criterion C (maths) and communication marks: say exactly what earns them (labelled axes, notation, logical steps, referencing).
- End with a criterion summary table: criterion | questions | total marks.
- If levels are needed, give a conversion per criterion: level = round(8 x raw / max) as a default, or the school's boundaries if supplied.

### Step 6: Check before delivering
- Mark totals add up per question, per task, per criterion and overall.
- Re-solve every calculation; check data supports the intended conclusion.
- Every strand covered; every band reachable; command terms match tariffs.
- Timing: roughly 1 mark per minute for a 2-hour/100-120 mark paper, less for 80-mark papers (about 1.5 min per mark).
- Content stays inside the topics the user listed, except deliberate unfamiliar contexts for top-band items.

### Step 7: Deliver
- Default: one document with the paper first, then the markscheme and blueprint after a clear page break, using the session's document artifact type if available; otherwise a Word/markdown file. If the user asks for PaperSim, output the PaperSim JSON described in section 4 instead.
- Reply with: title, global context, criteria and marks per criterion, duration, and one line on anything assumed.


---

## 4. PaperSim output (JSON with equations, images, tables and resources)

PaperSim is the user's on-screen exam app. It loads one JSON file per paper and renders Markdown, KaTeX maths, `\ce{}` chemistry, images, exam-style tables and a **Resources** tab on the right edge. The resources (periodic table, formula sheets, data booklets) open in a drawer beside the paper, like AssessPrep.

**Before writing PaperSim JSON, read `references/papersim-format.md`.** It is the full format guide, with every field, worked examples and the escaping rules. `references/paper.schema.json` is the machine-readable schema.

### 4.1 How the MYP paper maps onto the JSON
- One JSON question per markable part (1a, 1b, ...). `id` is the number shown to the student.
- `task`: the task heading ("Task 2: Investigation skills"). Questions with the same `task` are grouped in the navigator.
- `criterion`: "A"-"D". PaperSim totals marks per criterion in the results, so set it on every question.
- `commandTerm`: the single command term ("Explain"). `marks`: an integer, and the totals must match the blueprint.
- Stimulus goes in `context`: Markdown, `table` for data, `image`/`images` for figures. A later question that reuses earlier stimulus says so in its `context` ("Use Table 1 in question 3a.").
- `markScheme`: point-based items use one point per line, ending in "[1]". Levelled items use a Markdown table of markbands (Level | Descriptor | Indicative content), or `markSchemeTable`. Put the criterion summary and level conversion in the mark scheme of the last question of each task, or describe them in the reply.
- Multiple choice: `options` plus `correctOption` ("B").
- Diagrams you can draw: a small `data:image/svg+xml` URI with `imageAlt` and `imageCaption`. Diagrams you can't draw: describe the needed image in `imageAlt`, use `images/<name>.png`, and tell the user which file to supply.

### 4.2 Resources: what to include
Give the student what the real exam gives, nothing more:
- **Chemistry, or integrated sciences that use relative atomic masses:** include `"periodic-table"`. It is built in, with all 118 elements and IUPAC masses. Never type out a periodic table yourself.
- **Physics, or sciences papers with calculations:** a formula sheet as a content resource with only the equations the paper needs, plus constants (for example $g = 9.8\ \text{N kg}^{-1}$).
- **Mathematics:** a formula sheet of standard formulae (areas, volumes, quadratic formula, trigonometry, sequences) if the user's exam provides one. Ask if unsure.
- **Data the whole paper uses** (common ions, solubility rules, a source pack for I&S): its own resource, so it isn't repeated in every question.
- **Language & Literature, and I&S without data:** usually no resources.

**When the user provides a resource:**
- If it is pasted text, or a short PDF or image that is mostly text, formulae or tables, **transcribe it faithfully** into a content resource. Keep their headings and order, and convert formulae to LaTeX. It renders crisply and needs no extra file.
- If it is long, scanned or diagram-heavy, reference it as a file: `{"title": "Data booklet", "src": "resources/<exact-file-name>.pdf"}`. Tell the user to put the file in a `resources/` folder next to the JSON, or in the zip.
- If they say "use your own", write it yourself following the rules above.

In question text, link to a resource when it helps: `Use the [periodic table](#resource:periodic-table) …` or `#resource:<id>`. The id is the resource's `id`, or its title in lowercase with hyphens.

### 4.3 Format rules (also the ready-to-paste block for other prompts)

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

### 4.4 Check, then deliver
1. Save the paper as `<subject>-<topic>-paper.json` (lowercase, hyphens).
2. If code execution is available, run `python3 scripts/check_paper.py <file> --total <marks>`. Fix every ERROR and re-run until it prints OK. It catches single backslashes, unclosed `$`, unbalanced `\ce{`, ragged tables, duplicate ids, bad resources and wrong totals, and it lists the files the user must supply. If you can't run it, do the same checks by hand.
3. If the paper uses files (images or PDF resources), deliver a zip with the JSON, `images/` and `resources/`, so "Load paper" picks everything up in one go. Otherwise deliver the JSON alone.
4. Reply with: the title, global context, number of questions, marks per criterion, duration, the resources included, any files the user must add, and "Load it in PaperSim with Load paper." Don't paste the JSON into chat unless asked.
