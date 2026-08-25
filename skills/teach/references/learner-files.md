# Learner files

All session state lives in the **learner's working directory**, not in this skill repo.

```
alvar/
  LEARNER.md                 # how this mind wants to be taught
  maps/<slug>.md             # probe results for one goal
  sessions/<date>-<slug>.md  # plan + steps + quizzes
  teachings/<topic>.md       # one readable teaching正文 file per topic; append all nodes here
  visuals/<slug>-<n>.svg     # diagrams from learn-visual
```

Create `alvar/` on first use.

## LEARNER.md

If missing, run `learn-profile` or write a stub from `assets/LEARNER.md` and ask 3–5 questions to fill it. Do not invent a personality.

Read LEARNER.md at the start of every `teach` session. It controls:

- voice and density
- how they want struggle
- what they already treat as solid
- whether they want visuals, mermaid, LaTeX, or a long markdown log

## Map file

```markdown
# Map — <goal>

Updated: <ISO date>
Goal: <one sentence>

## Strands
| strand | status | evidence |
|--------|--------|----------|
| line integrals | known | Q2 correct, explained work |
| Stokes | edge | recognized statement, missed Faraday link |
| differential forms | unknown | said so |
| SR field mix | blocked | answered "I don't know" |

Status: `known` | `edge` | `unknown` | `blocked`

## Quiz log
- Q1 [line integrals] C — correct
```

## Session file

```markdown
# Session — <goal>
Date:
Model:
Goal:

## Goal mode

Primary: discovery | understanding | practice | application
Secondary: none | discovery | understanding | practice | application
Completion criteria:
- ...

## Plan
\`\`\`mermaid
graph TD
  A[covector] --> B[1-form]
  B --> C[wedge]
\`\`\`

## Log
### Node: covector
- activity: explanation | retrieval | quiz | practice | transfer | case | project | review
- taught:
- visual:
- quiz:
- result: lock-in | retry | insert-prereq
- challenge: too-easy | productive | too-hard | stalled
- signals: success/failure streak, hints, repeats, explicit feedback
- next adjustment: maintain | increase | reduce | step-back
```

## Memory item

```markdown
- item: <fact, term, or definition>
- activity: retrieval
- retrieval-round: 1/3
- last-result: correct | incorrect | hinted
- status: learning | locked | retry
```

Keep these files updated as you go. They are the persistence layer (the portable stand-in for a markdown-log / Obsidian pane).

## Teaching正文文件

Create one `alvar/teachings/<topic>.md` for each teaching topic. Append all nodes for that topic to this single file in teaching order. Do not split nodes into separate files. Use `$...$` for inline formulas and `$$...$$` for display formulas; these are the stable Obsidian MathJax forms.
