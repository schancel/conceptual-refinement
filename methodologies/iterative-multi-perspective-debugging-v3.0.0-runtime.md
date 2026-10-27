# IMPCD v3.0.0: Iterative Multi-Perspective Conceptual Debugging

## 1. The idea

A concept is a point in concept space. One IMPCD iteration is an operator T that maps a concept to a refined concept. The method repeats c(n+1) = T(c(n)) until it reaches a fixed point, a concept that T no longer changes. IMPCD applies to any concept: a technical design, a theory, an argument, a product, a protocol or a policy.

Naive iteration fails in two known ways. First, an LLM revision step is not a contraction: it can overshoot, oscillate or grow the concept without bound. Second, the operator is not neutral. Each model's prior pulls the concept toward the model's own attractor, so a long run converges on what the model likes rather than on what the author meant. Agreement between models can mean only that they share a prior. IMPCD therefore adds four things to plain iteration:

- **Damping.** Steps are kept small enough to converge.
- **Step-size control.** Steps are measured and resized.
- **An anchor.** The author's intent is a fixed term that every change answers to.
- **External evidence.** A concrete counterexample counts for more than any opinion.

## 2. Representation

The concept is held in four parts.

1. **Intent.** The author writes, in a few sentences, what the concept is for and what it must not become. Only the author may change it.
2. **Completion criteria.** These are the questions a finished concept must answer. The author writes them, and the run may propose additions for the author to accept.
3. **Claim ledger.** The concept itself is a numbered list of atomic claims (rules, definitions, mechanisms, assertions). Each claim records whether it is open or locked. The distance between two concepts is the number of claims added, removed or changed in substance. Rewording does not count.
4. **Rendering.** This is the readable form (spec, essay, paper), regenerated from the ledger. It is never edited directly.

## 3. One iteration

1. **Critique.** Several perspectives each review the open claims. Three are always present:
   - the anchor, which rejects drift from the intent;
   - an adversary, which looks for counterexamples;
   - a minimalist, which proposes deletions.

   Add two to five domain perspectives chosen for the concept. Each finding cites a claim, gives a severity from 1 to 10, states its evidence class (counterexample, argument or preference) and proposes the smallest fix. Deletion is preferred to addition.
2. **Two independent revisions.** Two revisers, from different models where possible, each produce a revised ledger. A reviser may make only changes that answer a finding; an unmotivated change is discarded.
3. **Consensus step.** The iteration applies only the changes that both revisions make, or make in substantively the same way. Disputed changes go to the disputed list. This is the damping: the step moves only where independent samples agree.
4. **Step-size control.** The disagreement between the two revisions estimates the step's error.
   - If the disagreement is within tolerance, accept the consensus step and widen the next scope.
   - If it exceeds tolerance, or the consensus step is empty, reject the step and narrow the scope, down to one claim at a time if necessary.
5. **Locking.** A claim that stays unchanged across two accepted iterations is locked. A locked claim is reopened only by a counterexample. Locking is how the run converges instead of reopening settled questions.
6. **Record.** Each iteration records the ledger, the findings, both revisions, the error estimate, the decision, the scope and the locks.

## 4. Decision rules

- **Evidence order:** a counterexample outweighs an argument, and an argument outweighs a preference. A finding backed by a concrete counterexample stands without support from anyone else.
- **Votes** choose only between valid alternatives that differ in preference.
- **Minority report:** a finding of severity 8 or more that is not resolved goes into the minority report and is never averaged away.
- **Intent:** a change that conflicts with the intent is rejected, however well supported.

## 5. Stop rules

- **Converged.** The consensus step changes no claim, no finding of severity 8 or more is open, and every completion criterion is answered. That is the fixed point.
- **Oscillation.** If the ledger returns to an earlier state twice, the operator has two attractors. Stop and give the author both competing forms to choose between.
- **Growth guard.** If the ledger grows by more than 20% over two iterations without answering a new completion criterion, stop, cut back to the last accepted size, and report what was cut.
- **Cap.** Stop after a fixed number of iterations (eight by default) and report the state.

The run always reports which rule stopped it.

## 6. What the result means

The result is a fixed point of this operator applied to this concept, anchored to this intent. It is coherent, complete against its criteria and stable under critique. It is correct only as far as the counterexamples, proofs, tests and data brought into the run make it so; the persona opinions add no evidence of their own. A different starting point or intent can reach a different fixed point. For concepts that matter, the final check is outside the loop: real experts, real tests or real stakeholders.

## 7. Domain packs

Domain material lives outside the core, in optional packs: sets of perspectives, completion criteria and evidence sources for a field. A protocol pack, for example, adds an implementer, a liveness reviewer and a red team, with simulation and test results as evidence. An ethics and policy pack can carry forward stakeholder and conflict-of-interest considerations. A pack may add perspectives and criteria, but it never changes the loop.

## Changelog

**3.0.0 (MAJOR).** The core is restored to a domain-neutral refinement loop.
- **Added:** the fixed-point framing, the claim ledger with a substantive distance, independent revisions with a consensus step (damping), step-size control, claim locking, the evidence order, and the oscillation and growth stop rules.
- **Moved to packs:** v2.1.1's structural moral-pattern catalog, premiums, conflict-of-interest weights, community-involvement and stakes classification, cultural adaptation and accessibility guidance.
- **Cut:** the fixed count of eleven personas, the weighted 60% supermajority for substantive questions, the semantic-similarity convergence metric, and the sixteen mandatory disclaimers (replaced by section 6).
