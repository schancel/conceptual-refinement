# Iterative Multi-Perspective Rhetorical Debugging (IMPRD) v0.1.0 — Runtime Core

> **Purpose:** Communication optimization — surfaces clarity gaps, style issues, persuasion failures, shareability barriers
> **Status:** DRAFT - Under IMPCD evaluation (Iteration 0)
> **Derived from:** IMPCD v2.1.1

## Prerequisites

**Recommended:** Load structural-moral-realism constitution (v8.0) for optimal consistency.
**Context:** IMPRD is communication-focused derivative of IMPCD. For conceptual debugging, use IMPCD.

## Core Process

### 1. Content Analysis Phase

Document before starting:
- **Primary message**: Core claim/argument in one sentence
- **Target audience**: Specific demographic/psychographic (not "general public")
- **Intended action**: What should readers think/feel/do after reading?
- **Current metrics**: Length, reading level, jargon density
- **Stakes assessment**: LOW (personal), MEDIUM (professional platform), HIGH (affects policy/vulnerable groups)

### 2. Reader Persona Generation (~11 personas)

**Required diversity dimensions:**

**Engagement Level Diversity (required):**
- Enthusiastic supporter of thesis
- Skeptic but persuadable
- Hostile critic
- Casual scroller (low attention span)
- Deep reader (high engagement)

**Audience Diversity (required):**
- Target audience insider (knows context/jargon)
- Adjacent audience (related interest, less background)
- Complete outsider (no domain knowledge)
- Non-native English speaker (if English content)
- Accessibility needs reader (cognitive load, vision, dyslexia, ADHD)

**Social Position Diversity (required):**
- High-status sharer (influencer, thought leader)
- Everyday reader (no platform)
- Professional in relevant field
- Affected stakeholder (if content impacts specific group)

**Values/Perspective Diversity (required):**
- Ideological differences relevant to topic
- Demographic differences
- Conflicting priorities

**Diversity verification:**
- No overlap/homogenization across personas
- Personas differ across multiple axes
- Accessibility personas not stereotyped
- Marginalized perspectives (if relevant) not tokenized

### 3. Structured Reader Feedback Collection

Each persona provides:

**Four scored dimensions (1-10 scale):**

1. **Understandability**: Can I grasp core message? Are examples clear? Is structure easy to follow? Are terms defined?

2. **Style Quality**: Is writing engaging? Does tone fit content? Is pacing good? Are there memorable phrases?

3. **Forward-ability**: Would I share this? Does sharing signal something positive about me? Is there a quotable hook? Will it spark useful discussion?

4. **Persuasiveness**: Am I moved by the argument? Are objections addressed? Do I trust the author? Is call-to-action clear?

**Plus qualitative feedback:**
- Specific strengths and weaknesses
- Emotional response to content
- Sharing likelihood: Would forward? To whom? Why/why not?
- One highest-impact improvement suggestion
- Confidence in assessment (1-10)

### 4. Weighted Aggregation

**Audience Relevance Weighting:**
- Target audience persona: 1.5×
- Adjacent audience: 1.0×
- Outlier audience: 0.7× (still valuable for accessibility)

**Engagement Level Weighting:**
- Deep reader: 1.2× (catches subtle issues)
- Casual scroller: 1.3× (represents majority)
- Low attention reader: 1.4× (hardest to reach)

**Complete Weighting Formula:**
```
weight = audience_weight × engagement_weight × confidence
score_weighted = (understandability + style + forwardability + persuasiveness) / 4 × weight
```

### 5. Aggregation Rules

**Revision threshold**: >70% weighted support for major changes

**Red flag triggers:**
- Any target/adjacent persona scores <3 on understandability
- Mean forward-ability <5 across all personas
- Multiple personas cite same confusion point

**Minority Report**: ≤3 personas with specific high-severity concerns → preserve even if not majority

### 6. Mandatory Audits

**A. Accessibility Audit**
- Reading level (Flesch-Kincaid score)
- Jargon density (% terms requiring domain knowledge)
- Non-native speaker comprehension barriers
- Cognitive load assessment (sentence complexity, information density)
- Visual formatting (headings, white space, lists, scanability)
- Screen reader compatibility (if web content)

**B. Persuasion Pattern Audit**
- Which structural patterns (SMR catalog) relevant to argument?
- Are claims appropriately confidence-calibrated?
- Appeals to emotion balanced with evidence?
- Author credibility established?
- Counter-arguments addressed or acknowledged?

**C. Viral Mechanics Audit**
- Hook present in first 2 paragraphs?
- 2-3 quotable one-liners present?
- Shareworthy emotions evoked? (inspiration, curiosity, constructive anger, hope)
- Title compelling and accurate?
- Clear "so what" / stakes articulation?
- Social signaling value for sharer?

**D. Manipulation Risk Audit**
- Emotional manipulation vs. legitimate emotional appeal?
- Misleading framing or cherry-picked evidence?
- Exploiting cognitive biases inappropriately?
- Targeting vulnerable audiences?
- Deceptive persuasion tactics?

### 7. Content Refinement

Revise based on weighted feedback, prioritizing:
1. Understandability gaps (especially for target/adjacent audiences)
2. Accessibility barriers
3. Manipulation risks (ethical override)
4. Forward-ability enhancements
5. Style improvements
6. Persuasiveness strengthening

Document all changes:
- What changed and why
- Which persona feedback addressed
- Trade-offs made (e.g., "added nuance, reduced punchiness")
- Minority concerns preserved
- Audit findings addressed

### 8. Iteration & Termination

**Convergence criteria (all required):**
- All target/adjacent personas score ≥7 on understandability
- Mean forward-ability score ≥7
- No major revisions suggested across 2 consecutive iterations
- Scores stable (±10%) across iterations
- No unresolved manipulation risks

**Iteration cap**: 4 iterations (content should tighten, not oscillate)

**Failure modes:**
- Irreconcilable audience needs (expert vs. novice can't both be satisfied)
- Message fundamentally unclear (underlying concept needs work)
- Manipulation audit flags unresolvable issues
- Scores not converging after 4 iterations

### 9. Version Tracking

Each iteration documents:
- Updated content
- All persona feedback with scores and confidence
- Weight calculations
- Audit findings
- Changes made with rationale
- Convergence metrics
- Reading level and other quantitative metrics

**Git tracking required for:**
- MEDIUM/HIGH stakes content
- Content affecting vulnerable groups
- Commercial persuasion content
- Anything requiring audit trail

## Required Disclaimers (Always Include)

1. AI-simulated reader personas, not real audience testing
2. Cannot replace actual user research or A/B testing
3. Identifies likely communication failures, not guaranteed success
4. Different LLMs may generate different persona responses
5. Cultural context limitations: [specify LLM cultural biases]
6. Accessibility evaluation limited without disabled readers
7. Viral mechanics uncertain (many factors beyond content quality)
8. Not validated for [list: languages other than English, highly technical content, etc.]
9. Manipulation audit is safeguard, not guarantee of ethical communication
10. Real audience testing strongly preferred for high-stakes content

## Appropriate Use Cases

**Use for:**
- Important blog posts where reach matters
- Persuasive content on complex topics
- Draft communication before stakeholder review
- Testing whether your "bubble" gets your message
- Pre-launch content optimization
- Internal communication drafts

**Do NOT use for:**
- Replacing actual user testing (HIGH stakes)
- Manipulative/deceptive content
- Content targeting vulnerable people for exploitation
- Real-time/urgent communication (just ship it)
- Contexts where authentic voice > optimization
- Marketing to children
- Political disinformation

## Stakes Classification

**HIGH-STAKES** (requires real audience testing):
- Policy communication affecting vulnerable groups
- Health/safety information for general public
- Crisis communication
- Content that could cause significant harm if misunderstood
- Commercial communication to vulnerable audiences

**MEDIUM-STAKES** (IMPRD valuable, real testing recommended):
- Professional thought leadership
- Organizational communication
- Commercial content to general audiences
- Educational content
- Advocacy communication

**LOW-STAKES** (IMPRD sufficient):
- Personal blog posts
- Internal team communication
- Low-reach content
- Preliminary drafts before real testing

**When in doubt, classify higher and test with real audiences.**

## Ethical Constraints

**You must not use IMPRD to optimize:**
- Deliberate misinformation or disinformation
- Manipulation of vulnerable populations
- Deceptive marketing or dark patterns
- Content designed to exploit cognitive biases for harm
- Propaganda or coordinated inauthentic behavior
- Content violating platform manipulation policies

**Structural pattern**: Deception compounds (SMR). Optimizing persuasiveness of false claims creates compounding harm.

## Common Pitfalls

1. Treating convergence as validation of truth claims (IMPRD optimizes communication, not correctness)
2. Over-optimizing for viral spread at expense of accuracy
3. Ignoring accessibility personas
4. Assuming AI personas represent real audiences
5. Using for HIGH-stakes without real audience testing
6. Failing to run manipulation audit
7. Optimizing for wrong audience
8. Trusting single LLM for important content
9. Ignoring minority reports from accessibility personas
10. Confusing persuasiveness with correctness

## License

Creative Commons BY-SA 4.0

**Usage requirements:**
- Preserve all disclaimers
- Document LLM(s) used
- Maintain audit trail for MEDIUM/HIGH stakes content
- Cite IMPRD methodology and version

---

*Version 0.1.0 - Initial formulation, under IMPCD evaluation*
*Derived from IMPCD v2.1.1 by Anthropic Claude (Sonnet 4.5)*
*Runtime core optimized for operational use. Annotated version forthcoming after validation.*
