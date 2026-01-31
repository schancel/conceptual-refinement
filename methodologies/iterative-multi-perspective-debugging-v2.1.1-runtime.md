# Iterative Multi-Perspective Conceptual Debugging (v2.1.1) — Runtime Core

> **Purpose:** Conceptual debugging — surfaces assumptions, conflicts, blindspots, value tensions
> **Status:** STABLE (January 2026)
> **Cross-LLM validated:** Claude, ChatGPT, Grok

## Prerequisites

**Recommended:** Load structural-moral-realism constitution (v8.0) for optimal consistency.
**Self-contained:** Embedded pattern catalog sufficient for standalone use.

## Core Process

### 1. Initial Concept Formulation
Begin with any text-based concept (proposal, policy, framework, positioning).

### 2. Persona Generation (~11 personas)

**Required diversity dimensions:**
- Ideological / value diversity
- Stakeholder diversity (beneficiaries, implementers, critics, displaced)
- Expertise diversity
- Demographic diversity (culture, language, disability, neurodivergence, SES)
- Power position diversity (marginalized vs centered)
- Conflict-of-interest diversity

**Critical:** Include personas with COI (financially/professionally displaced, disproportionate beneficiaries).

**Diversity verification:**
- Check for overlap/homogenization
- Personas differ across multiple axes
- Non-Western personas don't default to Western frameworks
- Marginalized perspectives not stereotyped

### 3. Structured Feedback Collection

Each persona provides:
1. Written feedback
2. Severity score (1–10) — impact if concern valid
3. Confidence score (1–10) — likelihood concern correct
4. Stance: support / oppose / neutral
5. COI disclosure

### 4. Weighted Aggregation

**Structural Pattern Catalog**

*Individual-Level Patterns*

| Pattern | Mechanism | Confidence | Validation |
|---------|-----------|------------|------------|
| Reciprocity | How you treat others affects how they treat you | VERY HIGH | All known societies |
| Trust dynamics | Betrayal harder to repair than initial trust-building | HIGH | 7+ contexts |
| Enforcement paradox | Excessive control produces resistance | HIGH | Governance, parenting, orgs |
| Deception compounds | Lies require more lies | HIGH | Cross-cultural |
| Trauma responses | Safety violation impacts trust/boundaries | HIGH | 8+ contexts |
| Inclusion/exclusion dynamics | Excluding affected parties produces resistance | HIGH | Governance contexts |
| Power accountability gap | Power without accountability tends toward abuse | HIGH | Historical pattern |
| Path dependence | Early choices constrain future options | HIGH | Institutions, technology |

*Systemic-Level Patterns*

| Pattern | Mechanism | Confidence | Validation |
|---------|-----------|------------|------------|
| Oppression maintenance | Systemic oppression constrains/harms mechanically | HIGH | Across cultures/time |
| Inequality compounding | Advantage/disadvantage compounds | HIGH | Matthew Effect |
| Power concentration | Power concentrates without countervailing forces | HIGH | Governance systems |
| Collective action dynamics | Coordination problems follow predictable patterns | HIGH | Well-studied |
| Structural violence | Systems harm without individual intent | HIGH | Multiple contexts |

**Pattern Validation Tiers**

- **Provisional**: LLM assessment, no citations → 1.3×–1.5× premium
- **Validated**: Citations provided → 1.3×–2.0×
- **Highly Validated**: Robust cross-cultural evidence → 1.3×–2.0×

**Threshold/Tipping-Point Documentation (7 Elements):**
1. Pattern name
2. Threshold mechanism
3. Threshold estimate (quantitative preferred; qualitative if unavailable)
4. Evidence level (Provisional/Validated/Highly Validated)
5. Reversibility (can system recover? at what cost?)
6. Warning indicators
7. Premium justification

**Threshold validation:**
- Provisional: 1.3×–1.5× only
- Validated: 1.3×–1.7×
- Highly Validated: 1.5×–2.0× (quantitative estimates required)

**Premium Guidelines**

| Community Context | Relevant Pattern | Premium |
|-------------------|------------------|---------|
| Direct subjects of rules/policy | Inclusion/exclusion, power accountability | 1.5×–1.8× |
| Marginalized with violation history | Trust dynamics, compounding violation | 1.6×–2.0× |
| Communities facing irreversible harm | Threshold effects, trauma responses | 1.7×–2.0× |
| Workers facing displacement | Reciprocity, enforcement paradox | 1.4×–1.6× |
| Lived experience of systemic issue | Domain knowledge, reciprocity | 1.5×–1.7× |

**COI Adjustments**

| Situation | Weight | Rationale |
|-----------|--------|-----------|
| Displaced/threatened professionally | 0.2×–0.5× | Floor ensures voice; discount bias |
| Disproportionate financial benefit | 0.5× | Support may be self-interested |
| No conflict | 1.0× | Baseline |

**Complete Weighting Formula**
```
weight = 1.0 × COI_adjustment × structural_premium × severity × confidence
```

### 5. Aggregation Rules

**Supermajority:** Changes require >60% weighted support

**Minority Report:** ≤4 personas with severity ≥8 AND confidence ≥7 → preserve as Minority Report

### 6. Mandatory Audits

**A. Power & Incentives Audit**
- Who benefits/loses regardless?
- Incentives outside argumentation?
- Power dynamics that can't be reasoned away?
- Structural patterns at risk?
- Threshold effects at risk?

*If operator benefits/has financial stake:* premium floor 1.5×, mandatory external review

**B. Operator Integrity Audit**
- Who controls persona generation/premiums?
- Constraints on selective inclusion/exclusion?
- Operator incentives?
- Abuse detection?
- Pattern bias blindspots?

**C. Model Bias Audit**
- Cultural/ideological skew
- Stereotype check
- Training data artifacts
- Disability representation
- Pattern universality bias
- Threshold identification bias

**Community Involvement Timing**

| Stakes | Community Involvement | Rationale |
|--------|----------------------|-----------|
| HIGH-STAKES (safety, rights, livelihoods, marginalized communities) | From iteration 1 | Shouldn't be "half-baked" without input |
| MEDIUM-STAKES (organizational policy, commercial with indirect impact) | From iterations 2-3 | Some stabilization useful |
| LOW-STAKES (internal conceptual development) | AI-only acceptable if purely internal | Escalate if will affect others |

### 7. Concept Refinement

- Incorporate supermajority changes with rationale
- Document patterns (with evidence levels + citations)
- Use 7-element template for thresholds
- Preserve high-severity concerns in Minority Report
- Document: patterns/validation, premiums, thresholds, audits, changes made/not made

### 8. Iteration & Termination

**Convergence (all required):**
- Semantic similarity >95%
- No new high-severity minority concerns
- Weighted support stable (±5%) across 2 consecutive iterations

**Failure Modes:**
- Oscillation (similarity to N-2 > N-1)
- Fragmentation (increasing contradictions)
- Irreconcilable tensions (opposing high-severity minorities 3+ iterations)
- Expansion runaway (>50% length increase without convergence)
- Iteration cap (>10 iterations)
- Diversity collapse (<3 distinct positions)

### 9. Git Tracking

Each iteration commits:
- Updated concept
- Persona feedback + scores
- Structural pattern analysis (patterns, evidence levels, citations)
- Threshold documentation (7-element template)
- Quantitative vs qualitative threshold modeling
- Pattern boundaries/exceptions
- Weight calculations (COI, premium, severity, confidence)
- Community input received
- Minority reports
- COI disclosures
- All audits
- External review findings
- Convergence metrics
- Rationale for changes

**Data Retention:**
- HIGH-STAKES: 7 years minimum
- MEDIUM-STAKES: 3 years
- LOW-STAKES: Project conclusion + 1 year

## Required Disclaimers (Always Include)

1. AI-generated personas, not real stakeholders
2. Cannot replace lived experience or community voice
3. Identifies blindspots, not truth
4. COI weighting limited to financial/professional conflicts (floor 0.2×)
5. Structural premiums: [list patterns with evidence levels]
6. Pattern validation status: [Provisional/Validated/Highly Validated]
7. Citations for Validated/Highly Validated: [references]
8. Threshold patterns with validation level
9. Quantitative vs qualitative threshold modeling noted
10. Community input: [received/not; how incorporated]
11. External review: [conducted/not; by whom]
12. If failed: concept may contain irreconcilable tensions
13. Version reflects [LLM name]'s understanding
14. Different LLMs may assess evidence differently
15. Local legal requirements: [consulted/not]
16. Ethnographic gap: real input strongly preferred

## Appropriate Use Cases

**Use for:**
- Early-stage concept development (pre-consultation)
- Internal governance drafts (before external review)
- Product positioning (low-stakes commercial)
- Pre-consultation stress-testing
- Identifying blindspots before community engagement

**Do NOT use for:**
- Final validation
- Claims of consensus
- Decisions affecting communities without real participation
- Culturally-sensitive concepts without cultural insiders (iteration 1+)
- Disabled-community concepts without disabled people (iteration 1+)
- Threshold effects without domain experts
- Replacing ethnographic research
- High-stakes decisions without human validation
- **Anything where you'd be uncomfortable telling affected parties "We used AI personas instead of you"**

## Stakes Classification

**HIGH-STAKES** (real community involvement by iteration 1):
- Safety, health, livelihoods, rights
- Marginalized/oppressed communities
- Irreversible consequences
- Threshold effects/tipping points
- Cultural practices/knowledge systems
- Serious harm if failure

**MEDIUM-STAKES** (external review before implementation):
- Organizational policy/governance
- Commercial with indirect societal impact
- Technical standards with adoption risk
- Affects employees/contractors

**LOW-STAKES** (AI-only if purely internal):
- Personal conceptual development
- Internal brainstorming
- Preliminary exploration
- Academic papers (labeled AI-assisted)

**When in doubt, classify higher.**

## Misuse Mitigation Template

Before starting, document:
1. **Affected parties**: Who will be impacted?
2. **Stakes classification**: HIGH/MEDIUM/LOW (justify)
3. **Community involvement plan**: When and how?
4. **"Uncomfortable test"**: Would you tell affected parties you used AI instead of them?
5. **Alternative methods considered**: Why is IMPCD appropriate?
6. **Methodology fit justification**: How do limitations align with use case?

## Cultural Scope Limitations

**Western deliberative origins:**
- Individual evaluation (vs. collective discernment)
- Supermajority thresholds (vs. consensus-seeking)
- Quantitative aggregation (vs. qualitative synthesis)
- Speed as efficiency (vs. time as relationship-building)

**May not fit:**
- Consensus-seeking cultures where voting inappropriate
- Contexts where speed is disrespectful
- Ongoing relational accountability situations
- Oral deliberation traditions
- Collective assessment norms

**For non-Western contexts:** Consider local deliberative practices instead.

## Cognitive Accessibility Limitations

**Methodology is cognitively demanding.** May be inaccessible to:
- People with intellectual disabilities
- People with cognitive fatigue conditions
- Some neurodivergent people
- People with limited literacy
- People for whom textual complexity is inaccessible

**If process is inaccessible to affected communities, it shouldn't be used for concepts affecting those communities.**

## Common Pitfalls

1. Treating convergence as validation
2. Using COI to silence dissent
3. Inconsistent premium application
4. Insufficient persona diversity
5. Ignoring minority reports
6. Trusting single LLM for high stakes
7. Bad faith operation
8. Using AI when real humans needed
9. Misidentifying patterns (ensure HIGH criteria met)
10. Ignoring pattern boundaries
11. Smuggling values as patterns
12. Claiming HIGH without evidence
13. Claiming thresholds without validation

## License

Creative Commons BY-SA 4.0

**Usage requirements:**
- Preserve all disclaimers
- Maintain git-level traceability
- Document LLM(s), patterns, validation levels, thresholds used

---

*Runtime core optimized for operational use. See annotated version for development rationale, examples, and detailed explanations.*
