# Persona Diversity Verification Pattern

## Name & Purpose

**Systematic Diversity Verification**: Ensure evaluator personas represent genuine, conflicting perspectives across multiple dimensions rather than collapsing into homogeneous viewpoints.

## When to Use

Use this pattern when:
- Generating simulated personas for multi-perspective evaluation
- Risk of LLM defaulting to similar/Western/stereotyped perspectives
- Need to surface genuine conflicts and tensions (not false consensus)
- Evaluating concepts that affect diverse stakeholders
- Want to catch blindspots that homogeneous groups miss

## Prerequisites

- A concept or proposal to evaluate
- Ability to generate or recruit diverse evaluators
- Understanding that diversity must span multiple dimensions simultaneously
- Acceptance that genuine diversity produces conflict (feature, not bug)

## Process

### Step 1: Define Required Diversity Dimensions

At minimum, include:

1. **Ideological/Value Diversity**
   - Different ethical frameworks (utilitarian, rights-based, care ethics, virtue ethics, etc.)
   - Different political orientations
   - Different religious/spiritual perspectives (including secular)

2. **Stakeholder Diversity**
   - Direct beneficiaries
   - Direct harmed/displaced parties
   - Implementers
   - Indirect affected parties
   - External critics

3. **Expertise Diversity**
   - Domain experts
   - Adjacent domain experts
   - Non-experts with lived experience
   - Methodological experts (different research traditions)

4. **Demographic Diversity**
   - Cultural backgrounds (emphasize non-Western perspectives)
   - Language backgrounds
   - Disability representation
   - Neurodivergence
   - Age ranges
   - Socioeconomic status

5. **Power Position Diversity**
   - Marginalized communities
   - Centered/majority communities
   - People with institutional power
   - People without institutional power

6. **Conflict-of-Interest Diversity**
   - Financially/professionally displaced by concept
   - Financially/professionally benefiting from concept
   - No direct financial/professional stake

### Step 2: Generate Initial Persona Set

Create ~11 personas. For each, document:
- Name and brief background
- Relevant identity dimensions
- Stake in the concept being evaluated
- Value framework they operate from
- Conflicts of interest (if any)
- Why this perspective matters

### Step 3: Run Automated Diversity Checks

Check for:
- **Overlap detection**: Are multiple personas essentially the same viewpoint?
- **Value framework distribution**: Are all personas using similar ethical reasoning?
- **Stakeholder coverage**: Are both winners and losers represented?
- **Geographic/cultural distribution**: Are non-Western perspectives included?
- **Conflict representation**: Are genuinely opposing views present?

### Step 4: Manual Review Against Dimensions

Create a matrix:

| Persona | Ideological | Stakeholder | Expertise | Demographic | Power | COI |
|---------|-------------|-------------|-----------|-------------|-------|-----|
| Person 1| Utilitarian | Beneficiary | Expert    | Western     | High  | Benefit |
| Person 2| Rights-based| Displaced   | Lived exp | Non-Western | Low   | Harmed |
| ...     | ...         | ...         | ...       | ...         | ...   | ...    |

**Red flags:**
- Any column with <3 distinct values
- All personas from similar cultural backgrounds
- Missing directly-affected parties
- No conflicts of interest represented
- All personas using Western ethical frameworks

### Step 5: Check for Model Bias

**Cultural bias check:**
- Do non-Western personas sound like Western thinkers?
- Are indigenous perspectives stereotyped or tokenized?
- Do marginalized personas use the same frameworks as dominant ones?

**Stereotype check:**
- Are disabled personas only talking about accessibility?
- Are non-Western personas only talking about "tradition"?
- Are marginalized personas only expressing vulnerability (not expertise/power)?

**Artificial consensus check:**
- Are personas reaching agreement too easily?
- Are conflicts being artificially resolved?
- Is diversity merely surface-level (different backgrounds, same conclusions)?

### Step 6: Add Missing Perspectives

Based on gaps identified, add or revise personas to ensure:
- Each dimension has sufficient spread
- Genuine adversaries are included (not just friendly critics)
- Conflicts of interest are represented
- Non-obvious perspectives are included

### Step 7: Verify Genuine Conflict Exists

Final check: Predict responses to the concept.
- If you expect ~80%+ agreement, diversity is likely insufficient
- Expect genuine splits, tensions, irreconcilable differences
- Multiple personas should have opposite stances for valid reasons

## Example

### Scenario
Evaluating a proposal for AI-powered hiring tools.

### Initial Persona Set (INSUFFICIENT)

1. Tech optimist (US, engineering background, employed)
2. Privacy advocate (EU, legal background, employed)
3. Fairness researcher (US, academic, employed)
4. HR professional (US, corporate, employed)

**Problems:**
- All employed, no job seekers
- All Western contexts
- All professionally invested in discourse
- No disability representation
- No one directly harmed by existing hiring bias
- Missing conflicts of interest

### Revised Persona Set (BETTER)

1. **Tech optimist** (US, engineering, employed by AI company) - **COI: Financial benefit**
2. **Privacy advocate** (EU, legal, employed by rights org)
3. **Black woman with hiring discrimination experience** (US, unemployed despite qualifications) - **Premium: Lived experience**
4. **Disability rights advocate** (UK, disabled, concerned about algorithmic bias) - **Premium: Affected community**
5. **HR professional** (Singapore, corporate, will implement system)
6. **Displaced HR recruiter** (US, job threatened by automation) - **COI: Professional harm**
7. **Global South data labeler** (Kenya, works on training data, low-wage)
8. **Indigenous hiring coordinator** (Canada, concerned about cultural fit algorithms)
9. **Neurodivergent job seeker** (Australia, harmed by standardized assessments)
10. **Hiring bias researcher** (Brazil, academic, utilitarian framework)
11. **Care ethics philosopher** (Japan, emphasizes relationship over metrics)

**Diversity achieved:**
- Ideological: Tech optimism, privacy rights, care ethics, utilitarianism, equity focus
- Stakeholder: Beneficiary, implementer, harmed by bias, displaced, data worker
- Expertise: Technical, legal, lived experience, academic, implementation
- Geographic: US, EU, UK, Singapore, Kenya, Canada, Australia, Brazil, Japan
- Power: Corporate employed, rights org, unemployed, low-wage, academic
- COI: Financial benefit, professional harm, no stake
- Intersectional: Race, disability, neurodivergence, indigenous identity, geography

**Expected conflict areas:**
- Efficiency vs. fairness vs. care
- Automation benefits vs. job displacement
- Western algorithmic assumptions vs. other cultural values
- Privacy vs. bias detection needs

## Variations

### Weighted Diversity

Not all dimensions matter equally for every concept. Prioritize:
- Dimensions most relevant to the concept
- Dimensions where blindspots cause most harm
- Dimensions representing directly affected communities

### Iterative Diversity

Start with fewer personas, check for homogenization, add targeted perspectives to fill gaps.

### Community-Sourced Diversity

For high-stakes concepts: Involve real community members in persona generation or validation.

## Pitfalls

1. **Surface diversity only**: Different backgrounds but similar viewpoints. Check for genuine conflict.

2. **Tokenization**: One representative of each group speaking in stereotyped ways. Ensure multiple people from marginalized groups with varying views.

3. **Missing adversaries**: Including only friendly critics. Explicitly generate perspectives that oppose the concept.

4. **Western framework dominance**: Non-Western personas using Western ethical frameworks. Actively prompt for indigenous/local frameworks.

5. **Expertise worship**: Overweighting credentialed experts vs. lived experience. Both matter.

6. **Conflict-of-interest avoidance**: Excluding people with stakes because "they're biased." Include them with appropriate transparency.

7. **False balance**: Treating all diversity dimensions equally when some are more relevant to the concept.

8. **Disability afterthought**: Adding disability only for accessibility issues. Disabled people have perspectives on everything.

## Related Patterns

- **Severity × Confidence Split**: Collects nuanced feedback from diverse personas
- **Conflict-of-Interest Weighting**: Handles personas with financial/professional stakes
- **Structural Pattern Weighting**: Applies premiums based on affected community status
- **Minority Report Preservation**: Ensures diverse perspectives aren't averaged away

## Source

Extracted from: Iterative Multi-Perspective Conceptual Debugging Methodology v2.0.0

Core requirement across all iterations, with explicit model bias checks added in v1.4+.
