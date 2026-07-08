# CS336 Flashcards — Agent Instructions

This folder holds Brian's flashcard deck for **CS336: Language Models From Scratch** (Spring 2026, 17 lectures total).

## File

- `cs336_flashcards_MASTER.html` — single self-contained HTML file (no build step, no dependencies). Open it directly in a browser.

## What to do when Brian shares a new lecture PDF

1. Read the PDF and identify the lecture number and title.
2. Extract 8–15 flashcard-worthy concepts (definitions, formulas, key comparisons, "why does X matter" questions). Match the style of existing cards: concise question, structured multi-line answer (use `\n` for line breaks, `•` for bullet points).
3. Open `cs336_flashcards_MASTER.html` and edit the `<script>` block:
   - Add a new entry to the `LECTURES` array (search for `// ── ADD FUTURE LECTURES HERE ──` around line 299) in this shape:
     ```js
     {
       id: 2,
       title: "Lecture Title Here",
       cards: [
         { topic: "Topic Name", q: "Question text?", a: "Answer text with \\n line breaks." },
         // ...
       ]
     }
     ```
   - `id` must match the lecture number (1–17) and must not duplicate an existing lecture.
   - Optionally add reference links/papers to the `MATERIALS` array (search for `// ── ADD FUTURE LECTURE MATERIALS HERE ──` around line 380), using the same `lecId`.
4. Don't touch the rendering code below the `// Supporting Materials` section — everything (lecture tabs, stats, progress bar, filtering) auto-derives from `LECTURES` and `MATERIALS`, so it just needs the data added correctly.
5. Save the file in place. No build/compile step — it's ready to open as-is.

## Notes

- Lecture count is hardcoded to 17 in two spots (`renderLectureBar` and `renderLecGrid`, both loop `i <= 17`) — don't change these unless the course syllabus changes.
- Locked/greyed-out lecture buttons in the UI just mean no `LECTURES` entry exists yet for that `id`.
- A daily scheduled reminder task (`cs336-flashcard-reminder`) nudges Brian to review this deck and to share new lecture PDFs as they come up.
