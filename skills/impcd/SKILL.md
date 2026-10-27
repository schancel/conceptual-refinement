---
name: impcd
description: Refine concepts, designs, policies, and methodologies with IMPCD v3 using author-owned intent, a claim ledger, independent revisions, consensus changes, and evidence-ranked critique. For rhetorical or stylistic editing of settled ideas, use IMPRD instead.
---

# IMPCD — Iterative Multi-Perspective Conceptual Debugging

Before running a review, read the complete authoritative
[v3.0.0 runtime](../../methodologies/iterative-multi-perspective-debugging-v3.0.0-runtime.md).
This skill routes requests and supplies execution boundaries; the runtime defines
the method. The [migration guide](../../methodologies/IMPCD-v3-MIGRATION.md)
explains differences from v2 and settings to record before starting.

## Routing

Use IMPCD for conceptual coherence: ideas, architectures, policies, governance,
methodologies, technical standards, and product concepts. Use IMPRD for clarity,
voice, rhetoric, accessibility, or persuasion when the underlying idea is settled.
When both are needed, run IMPCD first.

## Execute v3

- Obtain author-owned intent and completion criteria from the user or supplied
  material. If absent, propose them for acceptance; do not silently treat your
  proposals as author instructions. Only the author can change intent.
- Build numbered atomic claims with open/locked status and generate the readable
  rendering from that ledger. Record the initial ledger and run settings.
- Include anchor, adversary, minimalist, and two to five domain perspectives.
  Each finding cites a claim, severity 1–10, evidence class, and smallest fix.
- Obtain two independent revisions of the same ledger and findings, using
  different models where possible. Do not let one reviser see the other's output
  before submission. If independent execution is unavailable, report the
  limitation; do not label sequential self-editing independent consensus.
- Follow the runtime's consensus step, error estimate, scope adaptation, locking,
  and stop rules. Record findings, both revisions, disputed changes, decisions,
  scopes, locks, and ledger history. Preserve unresolved severity ≥8 findings.
- Use votes only for preferences between valid alternatives. Counterexamples
  outrank arguments, which outrank preferences; intent-conflicting changes fail.
- Regenerate the rendering from the accepted ledger. Never revise it separately.

Optional packs add domain perspectives, criteria proposed for author acceptance,
and evidence sources; they do not alter the loop. The constitution, v2 weights,
fixed eleven-persona panel, audits, and sixteen disclaimers are not v3 requirements.

## Authority and reporting

A simulated perspective cannot authorize external actions. Keep writes and other
side effects within the user's requested scope. Preserve durable iteration
records where authorized; v3 does not require Git commits.

Report the actual stop rule, final ledger and rendering, completion-criterion
answers, disputed changes, minority report, and evidence used. Name the models
and independence limitations. If execution cannot proceed, describe the missing
input or capability without claiming a completed run. A fixed point demonstrates
stability under the operator, not correctness or stakeholder approval. State
which external tests, data, experts, or stakeholders actually contributed.
