# Iterative Multi-Perspective Rhetorical Debugging (IMPRD) v0.2.0 — Runtime Core

> **Purpose:** Communication optimization — surfaces clarity gaps, style issues, persuasion failures, shareability barriers while preserving authentic voice
> **Status:** BETA - Under IMPCD evaluation (Iteration 2)
> **Derived from:** IMPCD v2.1.1
> **Cultural Scope:** Designed for Western English-language digital content (see limitations)

## Prerequisites

**Recommended:** Load structural-moral-realism constitution (v8.0) for optimal consistency.
**Context:** IMPRD is communication-focused derivative of IMPCD. For conceptual debugging, use IMPCD.

## Core Process

### 1. Manipulation & Ethics Audit (VETO POWER - Must Pass Before Proceeding)

**Before optimizing content, verify:**

**STOP if any of these apply:**
- [ ] Content contains false or misleading factual claims
- [ ] Deliberately exploiting fear, outrage, or anxiety for manipulation
- [ ] Targeting vulnerable populations for exploitation
- [ ] Violating platform manipulation policies
- [ ] Optimizing propaganda or coordinated inauthentic behavior
- [ ] Content about marginalized communities without community involvement

**If content is ABOUT (not by) marginalized communities:**
- [ ] Community review required regardless of stakes
- [ ] Cannot proceed with AI-only evaluation

**If content makes factual claims:**
- [ ] Verify accuracy before optimization
- [ ] Cite sources
- [ ] Note: Optimizing false claims compounds deception (structural pattern)

**Ethical bright line:** Cannot optimize persuasiveness of false, manipulative, or harmful content. Manipulation audit has VETO power - if fails, STOP.

---

### 2. Content Analysis Phase

Document before starting:
- **Primary message**: Core claim/argument in one sentence
- **Target audience**: Specific demographic/psychographic (not "general public")
- **Intended action**: What should readers think/feel/do after reading?
- **Current metrics**: Length, reading level, jargon density
- **Stakes assessment**: LOW (personal), MEDIUM (professional platform), HIGH (affects policy/vulnerable groups)
- **Content type**: Persuasive? Informational? Exploratory? (affects which dimensions matter)
- **Author authentic voice**: What makes this person's voice distinctive? (must preserve)

### 3. Reader Persona Generation (~11 personas)

**Required diversity dimensions:**

**Engagement Level Diversity (required):**
- Enthusiastic supporter of thesis
- Skeptic but persuadable
- Hostile critic
- Skimming reader (scanning, not deep reading)
- Deep reader (high engagement, careful reading)

**Audience Diversity (required):**
- Target audience insider (knows context/jargon)
- Adjacent audience (related interest, less background)
- Complete outsider (no domain knowledge)
- Non-native English speaker (if English content)

**Accessibility Needs Diversity (required, not "outliers"):**
- Reader with ADHD (needs: frequent breaks, clear structure, engaging pacing)
- Reader with dyslexia (needs: clear fonts, good contrast, no walls of text)
- Reader with limited literacy (needs: simple language, concrete examples)
- D/deaf or hard of hearing reader (if audio/video: needs captions/transcripts)
- Neurodivergent reader (may prefer literal communication, explicit structure)

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
- Accessibility personas reflect real needs, not stereotypes
- Marginalized perspectives (if relevant) not tokenized

**CRITICAL:** Human review of AI-generated personas for stereotyping, especially for marginalized identities. If personas seem stereotyped, regenerate.

### 4. Structured Reader Feedback Collection

Each persona provides:

**Five scored dimensions (1-10 scale):**

1. **Understandability**: Can I grasp core message? Are examples clear? Is structure easy to follow? Are terms defined?

2. **Style Quality**: Is writing engaging? Does tone fit content? Is pacing good? Are there memorable phrases?

3. **Human Voice**: Does this sound like a person wrote it, or does it sound mechanical/corporate/AI-generated? Is there a distinctive personality/voice? Does it feel authentic?

4. **Forward-ability**: Would I share this? Does sharing signal something positive about me? Is there a quotable hook? Will it spark useful discussion? (Not applicable for all content types)

5. **Persuasiveness**: Am I moved by the argument? Are objections addressed? Do I trust the author? Is call-to-action clear? (Not applicable for purely exploratory content)

**Plus qualitative feedback:**
- Specific strengths and weaknesses
- Emotional response to content
- What works about the voice/style? What feels off?
- Sharing likelihood: Would forward? To whom? Why/why not?
- One highest-impact improvement suggestion
- Confidence in assessment (1-10)

### 5. Weighted Aggregation

**Audience Relevance Weighting:**
- Target audience persona: 1.5×
- Adjacent audience: 1.0×
- Far outlier audience: 0.7×

**Accessibility Needs Weighting:**
- ALL accessibility personas: 1.5× (accessibility is requirement, not edge case)

**Engagement Level Weighting:**
- Deep reader: 1.2× (catches subtle issues)
- Skimming reader: 1.3× (represents majority)

**Complete Weighting Formula:**
```
weight = audience_weight × accessibility_weight × engagement_weight × confidence

For applicable dimensions only:
score_weighted = (understandability + style + human_voice + [forwardability if applicable] + [persuasiveness if applicable]) / N × weight
```

### 6. Aggregation Rules

**Revision threshold**: >70% weighted support for major changes

**HARD REQUIREMENTS (must meet):**
- All accessibility personas score ≥7 on understandability
- Mean human voice score ≥7 (must sound human-written)
- No target/adjacent persona scores <3 on understandability

**Red flag triggers:**
- Mean forward-ability <5 (if forward-ability is goal)
- Multiple personas cite same confusion point
- Authenticity scores decline during iteration (over-optimization)

**Minority Report**: ≤3 personas with specific high-severity concerns → preserve even if not majority

### 7. Mandatory Audits

**A. Accessibility Audit (REQUIRED - Must Pass)**
- Reading level (Flesch-Kincaid score) - target ≤12th grade for general audiences
- Jargon density (% terms requiring domain knowledge) - define or eliminate
- Non-native speaker comprehension barriers
- Cognitive load assessment (sentence complexity, information density)
- Visual formatting (headings, white space, lists, scanability)
- Screen reader compatibility (if web content)
- Neurodiverse accessibility (structure, pacing, explicitness)

**If accessibility audit fails:** Content requires revision. Accessibility is requirement, not optimization target.

**B. Authenticity vs. Optimization Audit**
- Does optimization preserve author's distinctive voice?
- Are suggested changes making content sound generic/corporate?
- Is there enforcement paradox risk? (over-optimization → inauthenticity → audience distrust)
- Trade-off guidance: When optimization conflicts with authenticity, bias toward authenticity

**C. Persuasion Pattern Audit**
- Which structural patterns (SMR catalog) relevant to argument?
- Are claims appropriately confidence-calibrated? (Not overstating certainty)
- Appeals to emotion: Legitimate emotional resonance or manipulation?
- Author credibility established?
- Counter-arguments addressed or acknowledged?

**D. Viral Mechanics Audit** (only if forward-ability is goal)
- Hook present in first 2 paragraphs?
- 2-3 quotable one-liners present?
- Shareworthy emotions evoked? (inspiration, curiosity, constructive anger, hope - NOT fear/outrage manipulation)
- Title compelling and accurate?
- Clear "so what" / stakes articulation?
- Social signaling value for sharer?

**E. Accuracy & Precision Audit** (for technical/factual content)
- Are factual claims accurate?
- Sources cited?
- Technical precision maintained? (not sacrificed for engagement)
- Trade-off guidance: Accuracy > persuasiveness

### 8. Content Refinement

Revise based on weighted feedback, prioritizing:
1. **Manipulation/accuracy issues** (VETO - must fix)
2. **Accessibility barriers** (requirement)
3. **Authenticity preservation** (bias toward authentic voice over optimization)
4. **Understandability gaps** (especially for target/adjacent audiences)
5. **Human voice** (must sound person-written, not mechanical)
6. Forward-ability enhancements (if applicable)
7. Style improvements
8. Persuasiveness strengthening

Document all changes:
- What changed and why
- Which persona feedback addressed
- Trade-offs made (e.g., "added nuance, reduced punchiness" or "preserved authentic casual tone over polish")
- Minority concerns preserved
- Audit findings addressed

### 9. Iteration & Termination

**Convergence criteria (all required):**
- All accessibility personas score ≥7 on understandability
- Mean human voice score ≥7 (sounds person-written)
- Mean scores stable (±10%) across 2 consecutive iterations
- No major revisions suggested
- No unresolved manipulation/accuracy issues
- Authenticity not declining

**Iteration cap**: 4 iterations (content should tighten, not oscillate)

**STOP EARLY if:**
- Authenticity scores declining (over-optimization backfiring)
- Personas suggest content is becoming generic/corporate
- Diminishing returns (minor tweaks not improving scores)

**Failure modes:**
- Irreconcilable audience needs (expert vs. novice can't both be satisfied)
- Message fundamentally unclear (underlying concept needs work)
- Manipulation/accuracy issues unresolvable
- Over-optimization eroding authentic voice
- Scores not converging after 4 iterations

### 10. Version Tracking

Each iteration documents:
- Updated content
- All persona feedback with scores and confidence
- Weight calculations
- Audit findings (all 5 audits)
- Changes made with rationale
- Authenticity trade-offs
- Convergence metrics
- Reading level and other quantitative metrics

**Git tracking required for:**
- MEDIUM/HIGH stakes content
- Content affecting vulnerable groups
- Commercial persuasion content
- Anything requiring audit trail

## Required Disclaimers (Always Include)

1. **AI-simulated reader personas**, not real audience testing
2. **Cannot replace actual user research** or A/B testing
3. **Identifies likely communication failures**, not guaranteed success
4. **Untested predictions** - weighting and convergence criteria not empirically validated
5. **Cultural scope:** Designed for Western English-language digital content (see limitations)
6. **AI personas may not match real audiences** - stereotyping risk despite safeguards
7. Different LLMs may generate different persona responses
8. Accessibility evaluation limited without disabled readers
9. Viral mechanics uncertain (many factors beyond content quality)
10. Manipulation audit is safeguard, not guarantee of ethical communication
11. Real audience testing strongly preferred for high-stakes content
12. Content about marginalized communities evaluated with AI personas only if communities unavailable (not ideal)

## Cultural Scope Limitations

**This methodology is designed for Western English-language digital content.**

**Embedded Western assumptions:**
- **Direct communication bias**: "Clear call-to-action," "explicit stakes," "quotable hooks" assume low-context communication norms. High-context cultures (much of East Asia, Middle East) use indirect persuasion.
- **Individualist persuasion model**: Viral spread, personal shareability, individual content optimization reflect Western individualism. Collectivist cultures emphasize group harmony, relational trust, community discernment.
- **Text-centrism**: Assumes written text. Oral, visual, and multimodal traditions not addressed.
- **Forward-ability as success metric**: Reflects Silicon Valley logic. Many cultures value slow, deep, relational engagement over viral spread.
- **English-only**: Different languages have different rhetorical traditions.

**May not fit:**
- High-context cultures (indirect communication, relationship-based persuasion)
- Collectivist cultures (community discernment over individual optimization)
- Oral tradition cultures (different persuasion dynamics)
- Contexts where speed/optimization is disrespectful
- Non-Western rhetorical traditions

**For non-Western contexts:** Consult local communication and rhetorical traditions. This methodology may produce culturally inappropriate content if applied without adaptation.

**Recommendation:** Either adapt methodology significantly for cross-cultural use, or limit use to Western English-language digital content only.

## Appropriate Use Cases

**Use for:**
- Important blog posts where reach matters
- Persuasive content on complex topics
- Draft communication before stakeholder review
- Testing whether your "bubble" gets your message
- Pre-launch content optimization
- Internal communication drafts

**Worth the investment when:**
- Stakes are medium/high (mistakes costly)
- Reaching diverse audiences (accessibility matters)
- Complex topic (high misunderstanding risk)
- Persuasion is goal and audience is skeptical

**Overkill when:**
- Time-sensitive/urgent (just ship it)
- Low stakes personal content
- Authentic voice > reach
- Already tested with real audiences

**Do NOT use for:**
- Replacing actual user testing (HIGH stakes)
- Manipulative/deceptive content
- Content targeting vulnerable people for exploitation
- Marketing to children
- Political disinformation
- Content about marginalized communities without community involvement

## Stakes Classification

**HIGH-STAKES** (requires real audience testing, not just IMPRD):
- Policy communication affecting vulnerable groups
- Health/safety information for general public
- Crisis communication
- Content that could cause significant harm if misunderstood
- Commercial communication to vulnerable audiences
- Content about marginalized communities (requires community review)

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
- False or misleading factual claims

**Structural pattern - Deception Compounding (SMR):** Optimizing persuasiveness of false claims creates compounding harm. Each iteration makes deception more effective and harder to detect.

**Transparency consideration:** Information asymmetry - methodology users gain sophisticated persuasion tools audiences don't know about. Some contexts may require disclosure: "This content was optimized for persuasiveness."

## Common Pitfalls

1. **Treating convergence as validation of truth** (IMPRD optimizes communication, not correctness)
2. **Over-optimizing for viral spread** at expense of accuracy or authenticity
3. **Ignoring accessibility personas** or treating them as edge cases
4. **Assuming AI personas represent real audiences**
5. **Using for HIGH-stakes without real audience testing**
6. **Skipping manipulation audit** or treating it as pro forma
7. **Optimizing for wrong audience**
8. **Trusting single LLM** for important content
9. **Ignoring minority reports** from accessibility personas
10. **Confusing persuasiveness with correctness**
11. **Over-optimization eroding authentic voice** (enforcement paradox)
12. **Cultural imperialism** - applying Western norms to non-Western contexts
13. **Resource advantage** - acknowledging this advantages well-funded creators

## Resource & Power Considerations

**Acknowledgment:** This methodology is resource-intensive (time, skills, computational costs). Well-funded content creators can invest in optimization; grassroots creators cannot. This perpetuates existing communicative power imbalances.

**Structural pattern - Power Concentration (SMR):** Optimization tools advantage those with resources, concentrating communicative power.

**Mitigation considerations:**
- Guidance on when full process is warranted vs. overkill
- Potential simplified "IMPRD-Lite" for quick/low-stakes content
- This is not yet democratized tool

**No solution offered here**, but acknowledging the dynamic.

## When to Use Which Dimensions

**Not all content types need all dimensions optimized:**

| Content Type | Understandability | Style | Human Voice | Forward-ability | Persuasiveness |
|--------------|-------------------|-------|-------------|-----------------|----------------|
| Persuasive essay | ✓ | ✓ | ✓ | ✓ | ✓ |
| Exploratory post | ✓ | ✓ | ✓ | Maybe | ✗ |
| Technical doc | ✓ | ✓ | ✓ | ✗ | ✗ |
| Tutorial | ✓ | ✓ | ✓ | Maybe | ✗ |
| Opinion piece | ✓ | ✓ | ✓ | ✓ | ✓ |

**Guidance:**
- Technical/informational content: Prioritize accuracy and understandability over persuasiveness
- Exploratory content: Prioritize authenticity and clarity over persuasion
- Advocacy content: All dimensions relevant, but manipulation audit critical

## License

Creative Commons BY-SA 4.0

**Usage requirements:**
- Preserve all disclaimers and limitations
- Document LLM(s) used
- Maintain audit trail for MEDIUM/HIGH stakes content
- Cite IMPRD methodology and version
- Acknowledge cultural scope limitations

---

## Changelog from v0.1.0

**Major changes:**
1. **Added manipulation audit as STEP 1 with VETO power** (was step 6, equal weight)
2. **Added "Human Voice" as 5th scored dimension** - must sound person-written, not mechanical
3. **Added cultural scope limitations section** - explicit about Western/English-language design
4. **Separated accessibility personas from "outliers"** - weighted 1.5× (was 0.7×)
5. **Added hard requirement:** All accessibility personas ≥7 on understandability
6. **Added authenticity vs. optimization audit** - bias toward authenticity when conflict
7. **Added community review requirement** for content about marginalized groups
8. **Added accuracy & precision audit** for technical/factual content
9. **Added "sounds human" convergence criterion** (mean human voice ≥7)
10. **Added guidance on when to use which dimensions** (not all content needs all)
11. **Added resource & power considerations** - acknowledges methodology advantages resourced creators
12. **Strengthened ethical constraints** - moved earlier, more prominent
13. **Added "stop early" guidance** - if over-optimization eroding authenticity
14. **Added empirical validation caveats** - untested predictions acknowledged

**Minor changes:**
- "Low attention reader" → "Skimming reader" (less ableist framing)
- Separated ADHD/dyslexia/literacy as distinct accessibility needs
- Human review required for AI-generated personas (stereotype check)
- Fact-checking recommendation for factual claims
- Platform manipulation policies mentioned in ethics section

---

*Version 0.2.0 - Major revision after Iteration 1 IMPCD evaluation*
*Derived from IMPCD v2.1.1 by Anthropic Claude (Sonnet 4.5)*
*Status: BETA - Proceeding to Iteration 2 evaluation*
*Runtime core optimized for operational use. Annotated version forthcoming after validation.*
