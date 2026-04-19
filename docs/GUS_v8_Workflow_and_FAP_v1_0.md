# GUS v8 Governance Interface — Workflow and FAP v1.1

## Purpose

Build the professional interface layer for the proven GUS v7 Governance Integrity Vehicle (GIV).

v8 is presentation authority only.  
Backend truth remains in v7.

---

## Core Doctrine

- Advisory only
- No execution authority
- Human sovereignty preserved
- Deterministic outputs
- Fail-closed behavior
- Transparent presentation
- No fabricated results

---

## Repo Workflow Lock

### Bootstrap Exception (Completed)

Initial direct push to `main` allowed only for repo initialization.

### From Now On

- Never build on `main`
- Create PR branch first
- One objective per branch
- Merge by PR
- Sync `main` after merge

---

## Seal Discipline Lock (NON-NEGOTIABLE)

UI phases are **not exempt** from sign/seal workflow.

The same integrity discipline used in v7 applies to v8.

### Pre-Merge Order

1. Commit real feature change
2. Snapshot HEAD
3. Sign seal
4. Commit seal files
5. Strict verify
6. Push PR branch
7. Create PR
8. Merge PR

### Post-Merge Canonicalization Order

1. Sync `main`
2. Verify feature exists in `main`
3. Snapshot HEAD
4. Sign seal
5. Commit seal files
6. Strict verify
7. Push `main`

### Repair Rule

If any phase is merged without required seal/sign discipline:

- STOP feature progression
- open repair branch
- restore workflow authority
- execute missing seal discipline from corrected state
- only then continue normal phase work

---

## UI Boundary Law

UI may:

- collect structured inputs
- display verdicts
- show explanations
- show trust state
- show metrics

UI may NOT:

- alter backend truth
- invent verdicts
- bypass rules
- gain hidden authority
- mutate canonical records

---

## Phase Roadmap

### Phase 01 — Repo Initialization ✅

### Phase 02 — Design System ✅

Theme, spacing, typography, trust styling.

### Phase 03 — Home Dashboard ✅

### Phase 04 — Case Input

### Phase 05 — Verdict Screen

### Phase 06 — Explanation Panel

### Phase 07 — Trust Panel

### Phase 08 — Metrics Dashboard

### Phase 09 — UI Hardening + Closure

---

## Validation Minimum

- py_compile
- targeted tests
- integration tests
- clean git status

---

## Final Truth

v7 is the engine.  
v8 is the doorway humans use.
