# PaperSim

A timed practice-exam simulator in the style of MYP on-screen examinations. One HTML file, no build step, no backend, no API keys.

## Use it
1. Download or clone this repo.
2. Double-click `index.html` (Chrome, Edge or Opera).
3. Click **Load paper** and choose a paper JSON (try `sample-paper.json` or `sample-rich-paper.json`), then **Start examination**.

## Features
- Countdown timer with 30- and 10-minute warnings; answers lock at zero.
- Autosave to your browser (localStorage). Refreshing or closing the tab keeps your answers, and the timer keeps running.
- Text answers with inline maths (MathLive): Ctrl+M or type `\` to start an equation.
- Question navigator, flags, highlighter, notepad, Desmos scientific/graphing calculator.
- Submit to reveal the mark scheme, self-mark each question, see totals per criterion.
- Export a clean printable record (save as PDF).

## Paper format
See [PAPER-FORMAT.md](PAPER-FORMAT.md) and [paper.schema.json](paper.schema.json). `skill/` contains a Claude skill for generating papers in this format.

## Privacy
Everything stays in your browser. The only network requests are MathLive (jsDelivr CDN) and the Desmos calculator page.

Not affiliated with the IB or AssessPrep. MIT licensed.
