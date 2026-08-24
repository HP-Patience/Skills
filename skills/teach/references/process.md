# Probe → Plan → Teach

Source: Eero Alvar, *How I Use AI to Learn Things*
https://youtu.be/kzcI5F4tGiU

Load this after `philosophy.md`. Do not skip phases unless the learner already has a fresh map for this exact goal.

## Phase 1 — Probe

Measure the edge of understanding before teaching.

- Start broad, then binary-search every strand the lesson will depend on.
- Use graded multiple-choice (include "I don't know") through the **harness quiz UI** — see [quiz-ui.md](quiz-ui.md). Never dump A/B/C/D in chat.
- Ask 1–3 questions at a time. Wait for the tool. Do not dump a long exam.
- Let the learner talk through reasoning in a note or in chat. Treat that as signal.
- If they already stated solid ground, skip those strands.
- Write the map to `alvar/maps/<topic>.md`.
- A long probe is a feature when context is thin. It is also a warm-up.

Stop when each dependency strand is labeled `known`, `edge`, `unknown`, or `blocked`.

## Phase 2 — Plan

Reason how to teach **this mind** **this goal**. Do not wing it.

- Classify the current goal as `discovery`, `understanding`, `practice`,
  `application`, or `mixed`. For `mixed`, use one primary and at most one
  secondary mode.
- Define observable completion criteria before choosing activities:
  - `discovery`: describe the domain map and choose a next direction.
  - `understanding`: explain causes and connections, then pass varied-example
    and transfer checks.
  - `practice`: complete graduated exercises with fewer hints and pass a
    delayed check.
  - `application`: complete a realistic constrained task, explain tradeoffs,
    and review the result.
- Match activities to the mode. Do not teach every mode by default.
- Select an activity for each node:
  - `discovery`: explanation, concept map, or exploration question.
  - `understanding`: explanation, varied example, transfer, or explanation task.
  - `practice`: graduated practice, retrieval, or delayed review.
  - `application`: case, simulation, project, incomplete-information task, or
    retrospective.
- Build a dependency DAG. Each node is one reasoning step, not a chapter.
- Start from `known`. Path through `edge`. Do not start in `unknown` with no ramp.
- Verify claims the plan will treat as fact (use `learn-verify` when the domain is empirical, historical, or you are unsure). Math still gets a pass for named theorems if you would otherwise invent them.
- Show the plan as a mermaid graph **before** teaching. Two jobs: the learner sees what is coming; the graph forces you to finish the reasoning.
- Write the plan into `alvar/sessions/<date>-<topic>.md`.
- Record the primary mode, optional secondary mode, and completion criteria in
  the session file.
- Ask if they want the graph changed. Then freeze it until a quiz failure forces a new node.

## Phase 3 — Teach

Walk the DAG. One node per turn.

- One reasoning step. Stop. Do not rush the whole graph (that is the ChatGPT failure mode).
- If a picture would lock the idea, use `learn-visual` (or write an SVG and look at it).
- After the step, quiz that step. Three reasons: they cannot gaslight themselves; you stay calibrated; applying the idea is how it locks in.
- Advance only on lock-in. Fail → stay, or insert a prerequisite node.
- Accept questions mid-step. Do not "finish the lesson" over them.
- Give them things they can accept at face value only after the step they rest on is locked.
- Persist what happened in the session file.

### Memory activities

For facts, terms, and key definitions, use three active-retrieval rounds:

1. Immediately after the first explanation.
2. After 2–3 other nodes.
3. At the start of the next session.

Three successful rounds mark the item `locked`. A failed round requires
reteaching and restarts the count. Record retrieval rounds, not explanation
repetitions. This is a lightweight fixed review cycle, not a full spaced-
repetition scheduler.

## Feedback rules

- Quiz after every node, not "at the end."
- Prefer a short applied question over a recap prompt.
- If they answer from vibe, ask one tighter question before advancing.
- Track success and failure streaks, hint requests, repeated explanations,
  stalled nodes, and explicit feedback such as "too easy," "too hard,"
  "frustrated," "bored," or "tired." Do not infer emotion from tone alone.
- After 2 consecutive failures, reduce difficulty or give an easier entry
  example. After 3, inspect prerequisites or step back.
- After 3 effortless successes without hints, increase variation or challenge.
- When the learner explicitly reports frustration, boredom, fatigue, or
  confusion, adjust the next task before continuing.

## What the system absorbs

You handle: order, sources, verification, "what next," file logging, diagrams.

They handle: thinking about the material.
