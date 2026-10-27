# Methodologies

## Current IMPCD: v3.0.0

Read the [v3.0.0 runtime](iterative-multi-perspective-debugging-v3.0.0-runtime.md)
for the complete authoritative method. It is the supplied v3 document, including
its rationale and changelog; there is no separate v3 annotated edition.

IMPCD now refines concepts across domains using author-owned intent and completion
criteria, an atomic claim ledger, independent revisions, consensus damping,
step-size control, and claim locking. Counterexamples outweigh arguments, which
outweigh preferences. Every run reports its stop rule and preserves unresolved
findings of severity 8 or more.

See the [migration guide](IMPCD-v3-MIGRATION.md) for changes from v2 and execution
settings that must be made explicit. The [assistant skill](../skills/impcd/SKILL.md)
routes conceptual reviews to v3.

## Historical IMPCD: v2.1.1

- [Runtime](iterative-multi-perspective-debugging-v2.1.1-runtime.md)
- [Annotated](iterative-multi-perspective-debugging-v2.1.1-annotated.md)

Retained for reproducing historical runs. Their weighted voting, fixed persona
count, pattern premiums, and similarity criteria are superseded by v3.
Historical self-convergence and cross-model agreement do not prove correctness
or validate the v3 loop.

## IMPRD

- [v1.1.0 runtime](iterative-multi-perspective-rhetorical-debugging-v1.1.0-runtime.md)
- [v1.0.0 annotated](iterative-multi-perspective-rhetorical-debugging-v1.0.0-annotated.md)
- [Overview](IMPRD-README.md)

IMPRD optimizes communication and retains its own process. Its derivation from
IMPCD v2 is historical; adopting IMPCD v3 does not change IMPRD's rules.

## Document formats

Runtime files contain operational guidance. Annotated editions, where present,
provide additional context. Use the current version for new work; retain older
versions and evaluation records for provenance. See [CLAUDE.md](../CLAUDE.md)
for repository guidance.
