# Severity × Confidence Split Pattern

## Name & Purpose

**Two-Axis Signal Collection**: Separate the magnitude of potential harm (severity) from the likelihood that the concern is valid (confidence) to reduce cultural variance, emotional inflation, and gaming in feedback systems.

## When to Use

Use this pattern when:
- Collecting evaluative feedback on concepts, proposals, or decisions
- You need to distinguish between "this would be catastrophic *if* true" vs "this is definitely problematic"
- Different cultural contexts may have different norms around expressing concern
- You want to prevent both false positives (emotional inflation) and false negatives (self-censorship)
- You need to identify high-severity-but-low-confidence concerns that merit investigation

## Prerequisites

- A concept or proposal to evaluate
- Evaluators who can assess both dimensions independently
- Understanding that severity measures *impact if concern is valid*, confidence measures *likelihood concern is correct*

## Process

### Step 1: Frame the Two Axes Clearly

Explain to evaluators:

**Severity (1-10):** "If this concern turns out to be valid, how significant would the impact be?"
- 1-3: Minor inconvenience or easily fixable
- 4-6: Moderate impact requiring attention
- 7-8: Serious harm or major failure mode
- 9-10: Catastrophic or irreversible harm

**Confidence (1-10):** "How certain are you that this concern is valid?"
- 1-3: Speculation or weak hunch
- 4-6: Reasonable possibility based on patterns
- 7-8: Strong evidence or clear mechanism
- 9-10: Near-certain based on direct evidence

### Step 2: Collect Both Scores Independently

For each feedback item, require:
1. Written description of the concern
2. Severity score (1-10)
3. Confidence score (1-10)
4. Brief justification for each score

### Step 3: Calculate Weighted Signal

```
signal_strength = severity × confidence
```

This produces a combined metric where:
- High severity + high confidence = maximum signal (e.g., 9 × 9 = 81)
- High severity + low confidence = moderate signal (e.g., 9 × 3 = 27)
- Low severity + high confidence = moderate signal (e.g., 3 × 9 = 27)
- Low severity + low confidence = minimal signal (e.g., 3 × 3 = 9)

### Step 4: Identify Key Patterns

Look for:
- **High-severity, low-confidence concerns**: May need investigation to increase confidence
- **High-confidence, low-severity concerns**: Can be addressed but not urgent
- **High-severity, high-confidence concerns**: Immediate priority
- **Low-confidence patterns**: May indicate knowledge gaps or need for expert input

## Example

### Scenario
Evaluating a proposal to implement mandatory overtime for software developers during crunch periods.

### Feedback with Severity × Confidence

**Evaluator 1 (Developer):**
- Concern: "This will cause burnout and turnover"
- Severity: 8 (serious long-term harm to team)
- Confidence: 9 (have seen this pattern repeatedly)
- Signal: 72

**Evaluator 2 (Manager):**
- Concern: "May violate labor laws in some jurisdictions"
- Severity: 9 (legal liability, potential fines)
- Confidence: 4 (not sure about legal specifics)
- Signal: 36

**Evaluator 3 (HR Professional):**
- Concern: "Could undermine trust in leadership"
- Severity: 7 (affects organizational culture)
- Confidence: 8 (consistent with trust research)
- Signal: 56

**Evaluator 4 (Executive):**
- Concern: "Might impact project deadlines if people quit"
- Severity: 6 (moderate business impact)
- Confidence: 5 (depends on how it's implemented)
- Signal: 30

### Analysis

1. **Highest signal (72)**: Developer's burnout concern - both high severity and high confidence
2. **High-severity, low-confidence (36)**: Legal concern needs investigation - bring in legal expert
3. **Moderate-high signal (56)**: Trust concern well-supported by research
4. **Lower signal (30)**: Executive concern is speculative, less urgent

**Action priorities:**
1. Address burnout concern immediately (developer lived experience + high confidence)
2. Investigate legal requirements (high severity warrants verification despite low confidence)
3. Consider trust dynamics in implementation (well-supported concern)
4. Monitor for executive's concern but lower priority

## Variations

### With Additional Context

Add a third dimension:
- **Reversibility**: Can the harm be undone? (Yes/No/Partial)

This helps prioritize irreversible harms even when confidence is moderate.

### With Affected Party Weighting

Combine with structural premiums:
```
final_weight = severity × confidence × affected_party_premium
```

Where affected_party_premium ranges from 1.0× (neutral party) to 2.0× (directly affected with lived experience).

### Threshold for Action

Set minimum thresholds:
- Signal ≥ 40: Investigate or address
- Signal ≥ 60: High priority
- Severity ≥ 8 regardless of confidence: Flag for review

## Pitfalls

1. **Conflating severity and confidence**: Evaluators may rate high severity when they mean high confidence or vice versa. Provide clear definitions and examples.

2. **Cultural variance in confidence expression**: Some cultures express certainty more readily. Consider cultural context when interpreting confidence scores.

3. **Expertise mismatch**: Low confidence may signal lack of expertise rather than weak evidence. Cross-reference with evaluator expertise.

4. **Gaming**: Evaluators may inflate both scores strategically. Require written justifications and look for patterns of inflation.

5. **Ignoring low-confidence, high-severity concerns**: These may be early warnings. Don't dismiss them - investigate to raise or lower confidence.

6. **Averaging away important signals**: Don't average severity and confidence scores across evaluators - each evaluator's signal should be calculated individually first.

## Related Patterns

- **Minority Report Preservation**: Captures high-severity concerns even when not majority view
- **Structural Pattern Weighting**: Adds evidence-based premiums to severity × confidence
- **Diversity Verification**: Ensures evaluators represent different perspectives and knowledge bases
- **Power & Incentives Audit**: Identifies whose confidence/severity ratings might be biased by conflicts of interest

## Source

Extracted from: Iterative Multi-Perspective Conceptual Debugging Methodology v2.0.0

Originally contributed by ChatGPT during cross-LLM refinement iterations.
