# Minority Report Preservation Pattern

## Name & Purpose

**High-Severity Minority Protection**: Preserve dissenting perspectives that identify serious concerns, even when they don't have majority support, to prevent averaging away critical early warnings.

## When to Use

Use this pattern when:
- Aggregating feedback from multiple evaluators
- Risk of majority drowning out important concerns
- Need to preserve signals about serious potential harms
- Making decisions that could have irreversible consequences
- Want to maintain epistemic humility about what the majority might miss

## Prerequisites

- Multiple perspectives collected with severity and confidence scores
- A mechanism for preserving dissenting views alongside the main synthesis
- Willingness to maintain unresolved tensions rather than forcing false consensus

## Process

### Step 1: Define High-Severity Minority Criteria

Standard threshold:
**≤4 evaluators with severity ≥8 AND confidence ≥7**

This identifies:
- Small number of evaluators (minority view)
- Who see serious potential harm (severity ≥8)
- With strong conviction (confidence ≥7)

### Step 2: Collect All Feedback

For each evaluator, capture:
- Written concern/feedback
- Severity score (1-10)
- Confidence score (1-10)
- Overall stance (support/oppose/neutral)
- Relevant expertise or lived experience
- Any conflicts of interest

### Step 3: Calculate Majority Position

Using whatever aggregation method you're using:
- Weighted voting
- Consensus building
- Supermajority threshold (e.g., >60%)

Determine what the dominant synthesis or decision would be.

### Step 4: Identify Minority Reports

Scan for evaluators/positions meeting the criteria:
- Small number of evaluators (≤4)
- Severity ≥8
- Confidence ≥7
- Disagreeing with majority synthesis

### Step 5: Document Each Minority Report

For each qualifying minority concern, create a dedicated section:

**Minority Report: [Brief Title]**

- **Concern**: [Full description of the concern]
- **Severity**: [Score and justification]
- **Confidence**: [Score and justification]
- **Number of evaluators**: [Count]
- **Evaluator backgrounds**: [Expertise, lived experience, stake]
- **Why this matters**: [Why this concern deserves attention despite minority status]
- **Majority response**: [How the majority position addresses or doesn't address this]
- **Status**: [Unresolved / Partially addressed / Requires investigation]

### Step 6: Integrate into Final Output

Place Minority Reports in a dedicated section, clearly marked:
- After the main synthesis
- Before the conclusion
- With equal prominence to the majority position

Make clear:
- These are not dismissed
- They represent serious concerns from informed evaluators
- They may be early warnings or edge cases the majority missed
- Future iterations should revisit these

### Step 7: Revisit in Future Iterations

In subsequent iterations:
- Check if minority concerns were validated or refuted
- Update status: resolved / still unresolved / escalated
- Track whether evidence shifts toward or away from minority position

## Example

### Scenario
Evaluating a proposal for open-plan offices to increase collaboration.

### Majority Position (8/11 evaluators)
"Open-plan offices increase spontaneous collaboration and reduce communication barriers. Benefits outweigh costs. Support with minor modifications."

### Minority Report 1: Neurodivergent Accessibility

**Concern**: "Open-plan environments create sensory overload and cognitive fragmentation for neurodivergent workers, effectively excluding them from productive work."

- **Severity**: 9 (serious harm, potential disability discrimination)
- **Confidence**: 9 (extensive research and lived experience)
- **Number of evaluators**: 2
- **Evaluator backgrounds**:
  - Neurodivergent software developer with 10 years experience
  - Occupational therapist specializing in workplace accommodations
- **Why this matters**: Affects ability of neurodivergent employees to perform their jobs; creates accessibility barrier; may violate ADA/disability discrimination laws; expertise gap in majority view
- **Majority response**: Suggests "quiet zones" and "focus rooms" as compromise, but doesn't address that base environment becomes inaccessible
- **Status**: UNRESOLVED - requires investigation of legal requirements and accommodation efficacy

### Minority Report 2: Deep Work Impossibility

**Concern**: "Software development, writing, and analysis work require sustained focus blocks of 2-4 hours. Open-plan interruptions make this impossible, severely reducing quality and velocity despite increased 'collaboration'."

- **Severity**: 8 (significant productivity and quality impact)
- **Confidence**: 8 (research on deep work + industry experience)
- **Number of evaluators**: 3
- **Evaluator backgrounds**:
  - Senior software engineer
  - Academic researcher studying workplace productivity
  - Technical writer
- **Why this matters**: Core work activities become substantially harder; "collaboration" gains may come at cost of individual productivity; assumption that interruption-driven work is net positive may be wrong for this work type
- **Majority response**: Claims collaboration benefits outweigh focus costs, but hasn't quantified either
- **Status**: UNRESOLVED - requires measurement of actual productivity impact before/after

### Integration in Final Document

```markdown
## Synthesis

[Main synthesis from majority position...]

## Minority Reports

The following serious concerns were raised by minority evaluators with high severity and confidence scores. While they did not achieve majority support, they warrant careful consideration:

### Minority Report 1: Neurodivergent Accessibility
[Full content as above]

### Minority Report 2: Deep Work Impossibility
[Full content as above]

## Recommended Actions

1. Implement majority synthesis with modifications
2. Conduct legal review of accessibility concerns (Minority Report 1)
3. Pilot test with productivity metrics before full rollout (Minority Report 2)
4. Provide genuine alternatives (not just compromises) for affected workers
5. Revisit decision in 6 months with empirical data
```

## Variations

### Graded Minority Reports

Not all minority concerns are equal. Create tiers:

- **Critical Minority Reports**: Severity ≥9, confidence ≥8, irreversible harm, requires immediate investigation
- **Important Minority Reports**: Severity ≥8, confidence ≥7, standard preservation
- **Notable Dissent**: Severity ≥7 or confidence ≥7 but not both, document but lower priority

### Threshold Pattern Minority Reports

For concerns involving threshold effects:
- Lower the criteria to ≤6 evaluators (tipping points harder to see)
- Require additional investigation even with moderate confidence
- Premium weight due to irreversibility

### Structural Pattern Minority Reports

When minority reports invoke structural patterns (reciprocity, trust dynamics, power accountability):
- Require explicit engagement from majority position
- Must address the structural mechanism, not just dismiss the concern
- Consider pattern validation tier in determining weight

### Evolving Minority Reports

Track across iterations:
- **Strengthening**: More evidence emerges supporting minority view
- **Weakening**: Evidence contradicts minority view
- **Splitting**: Minority view fragments into sub-concerns
- **Converting**: Minority becomes majority
- **Persistent**: Remains minority but unrefuted

## Pitfalls

1. **Dismissing minorities as "just dissent"**: The pattern exists because minorities are often right about edge cases, underrepresented harms, and early warnings.

2. **False equivalence**: Not all minority views are equal. Use severity × confidence to distinguish serious concerns from personal preferences.

3. **Paralysis**: Preserving minority reports doesn't mean implementing all of them. It means not forgetting them.

4. **Averaging away**: Never average severity/confidence scores across minority and majority - maintain separate signals.

5. **Status quo bias**: Minorities challenging the status quo may face higher burdens of proof. Apply structural pattern premiums (e.g., affected communities) to counterbalance.

6. **Cherry-picking**: Only preserving minority reports that align with operator's preferences. Use systematic criteria.

7. **Burying in footnotes**: Minority reports should have equal prominence to majority synthesis.

8. **Never revisiting**: If minority reports are never checked in subsequent iterations, the pattern is performative.

## Related Patterns

- **Severity × Confidence Split**: Provides the metrics to identify high-severity minorities
- **Persona Diversity Verification**: Ensures minorities represent genuine different perspectives, not homogenization
- **Structural Pattern Weighting**: May elevate minority concerns when structural patterns are at stake
- **Threshold Documentation**: Threshold effects often identified by minorities before becoming consensus

## Research Foundation

This pattern draws on:
- **Wisdom of dissent** research: Minorities improve decision quality by forcing deeper consideration (Nemeth 1986)
- **Premature consensus failures**: Groupthink and false consensus lead to preventable disasters (Janis 1972)
- **Early warning signals**: Outliers often detect threshold effects before majority (Scheffer et al. 2009)
- **Minority influence**: Persistent minorities eventually validated in 30-40% of cases (Moscovici 1976)

## Source

Extracted from: Iterative Multi-Perspective Conceptual Debugging Methodology v2.0.0

Core mechanism since v1.0, strengthened with severity × confidence integration in v1.5+.
