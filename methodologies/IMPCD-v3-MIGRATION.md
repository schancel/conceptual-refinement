# Migrating IMPCD v2.1.1 to v3.0.0

## Current source

The [v3.0.0 runtime](iterative-multi-perspective-debugging-v3.0.0-runtime.md)
is an unchanged import of the supplied `IMPCD-v3.0.0.md`. It replaces v2 for new
reviews. This is a version replacement, not a claim that a v3 self-review ran or
converged. No independent revision experiment or external validation accompanied
this import.

## Changes

| v2 | v3 |
| --- | --- |
| Philosophical and moral-pattern framing | Domain-neutral core; optional domain packs |
| About eleven personas | Anchor, adversary, minimalist, plus two to five domain perspectives |
| Severity × confidence, premiums, COI weights | Severity 1–10 and evidence class: counterexample, argument, preference |
| Weighted 60% supermajority for substantive changes | Two independent revisions; apply only substantively shared changes |
| Directly revised prose | Atomic open/locked claim ledger; readable rendering regenerated from it |
| Semantic similarity and support stability | Substantive claim distance, disagreement, scope control, and locking |
| Minority size and confidence cutoffs | Every unresolved severity ≥8 finding remains in the minority report |
| Mandatory domain audits and disclaimers | Core limitations in section 6; relevant domain material outside the core |
| Historical convergence rules | Convergence, oscillation, growth guard, or iteration cap (eight by default) |

Author intent anchors every change. Only the author may change it; proposed
completion criteria require author acceptance. Counterexamples outrank arguments,
which outrank preferences. Consensus is a damping mechanism, not new evidence.

## Before executing a run

Record the author-supplied intent and completion criteria, initial numbered
ledger and rendering, perspectives, revisers, initial scope, disagreement measure,
tolerance, scope-resizing policy, and iteration cap. Keep independent revisers
from seeing each other's proposals before submission. Disclose use of the same
model or lack of independent execution.

The supplied core leaves the numerical tolerance, disagreement calculation,
scope increments, and handling of claim splits/merges unspecified. Choose and
record these as run settings before evaluating a step, rather than silently
presenting them as v3 defaults. Keep claim identities stable and count substantive
changes, not wording edits.

An empty consensus rejects the step under section 3. It can also terminate the
run under section 5 only when every completion criterion is answered and no
severity ≥8 finding remains open. Otherwise narrow scope and continue until a
stop rule applies. Record accepted iterations separately from rejected attempts
so only accepted iterations advance the two-iteration locking condition. Do not
label a capped or interrupted run converged.

Retain ledger history to detect recurrence and growth, record which claims were
cut on a growth stop, and preserve disputed changes and minority findings.
Report the actual stop rule and the evidence that supports the result.

## Historical material and optional packs

The v2 runtime, annotated edition, and existing evaluations remain in place for
provenance. They do not validate v3. IMPRD retains its own versioned rules and its
historical derivation from v2.

The standalone patterns, threshold template, and Structural Moral Realism
constitution remain available as domain resources. They are not automatically
loaded or treated as mandatory v3 rules. The v3 changelog's move to packs is an
architectural separation; this import does not claim that complete replacement
packs have been authored. Packs may add perspectives, author-approved criteria,
and evidence sources, but cannot restore weights or votes that override the loop.
