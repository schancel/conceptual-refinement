# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a conceptual refinement framework and reusable conceptual tools designed for AI use. The framework covers:

- **Iterative Clarification**: Processes for progressively refining understanding of concepts
- **Prompt Engineering Patterns**: Reusable patterns for structuring AI prompts and interactions
- **Knowledge Structuring**: Methods for organizing and representing conceptual knowledge

The project is primarily composed of markdown documents and prompt templates that AIs can use directly.

## Repository Structure

```
/methodologies/     - Complete methodological frameworks for specific processes
                      (e.g., iterative-multi-perspective-debugging.md)
/papers/            - Academic papers documenting methodologies (e.g., IMPRD paper)
/constitutions/     - AI constitutional frameworks refined using conceptual debugging
                      (e.g., structural-moral-realism-v8.0-runtime.md)
/patterns/          - Smaller, composable interaction patterns
/templates/         - Prompt templates and scaffolds
/examples/          - Example applications and case studies
```

## Terminology

- **Methodology**: A comprehensive, systematic process with multiple steps, validation criteria, and governance requirements (e.g., the Iterative Multi-Perspective Debugging methodology)
- **Pattern**: A smaller, reusable interaction pattern or technique that can be composed with others
- **Template**: A fill-in-the-blank scaffold for specific use cases
- **Skill**: In AI assistant terminology, refers to invocable tools (like /commit). This repository documents *methodologies* that AIs follow, not skills they invoke.

## Repository Philosophy

This is a living collection of reusable patterns for AI interactions. Patterns should be:
- **Practical**: Directly usable by AIs in real scenarios
- **Self-contained**: Each pattern should be understandable on its own
- **Well-documented**: Include context, usage examples, and expected outcomes
- **Generalizable**: Applicable across different domains and use cases

## Versioning Conventions

**For Methodologies** (comprehensive frameworks):
- Follow Semantic Versioning 2.0.0 (vMAJOR.MINOR.PATCH)
- Include version in filename for major versions (e.g., `debugging-v2.0.0.md`) or maintain version header in stable files
- Maintain changelog within the document
- Document cross-LLM testing and iteration count

**For Patterns and Templates** (smaller components):
- Versioning optional unless they undergo significant iteration
- Date-stamp major revisions if needed

## Adding New Content

### For Methodologies

When creating a comprehensive methodology:

1. **Structure**: Include these sections
   - Overview & value proposition
   - Core process (step-by-step)
   - Explicit limitations
   - Required disclaimers
   - Appropriate use cases
   - Common pitfalls
   - License & contribution guidelines
   - Meta-reflection (if iteratively developed)

2. **Documentation requirements**:
   - Version number if iteratively developed
   - Evidence basis for claims
   - Validation across multiple LLMs (if applicable)
   - Failure modes and convergence criteria

3. **Naming**: Use descriptive, process-oriented names (e.g., "iterative-multi-perspective-debugging.md")

### For Patterns

When creating smaller patterns:

1. **Structure**: Create clear sections for:
   - Purpose/Intent
   - When to Use
   - How to Use
   - Examples
   - Expected Outcomes
   - Variations/Adaptations

2. **Naming**: Use descriptive, verb-oriented names that indicate the pattern's function (e.g., "progressive-clarification.md", "assumption-extraction.md")

3. **Cross-referencing**: Link related patterns and indicate when patterns work well together

4. **Meta-documentation**: Update this CLAUDE.md if new organizational patterns emerge

## Runtime Core vs. Annotated Versions

Some methodologies and constitutions have paired runtime and annotated editions.
IMPCD v3 is a single self-contained runtime with rationale and changelog; do not
create a second edition just to satisfy the older paired-file convention.

**Runtime Core (`-runtime.md` suffix):**
- Operational instructions only
- Stripped of explanatory content, rationale, examples
- Optimized for token efficiency when loading into LLMs
- Self-contained and immediately usable
- Typically 150-250 lines for methodologies, 700-800 for constitutions

**Annotated (`-annotated.md` suffix):**
- Complete documentation with context
- Includes: development history, design rationale, examples, edge cases
- For learning, iteration, and creating similar frameworks
- Typically 3-5x larger than runtime core

**When to use which:**
- Use **runtime core** when: Loading into LLM for actual execution, token cost matters, familiar with methodology
- Use **annotated** when: Learning methodology, iterating on design, understanding rationale, training others

**Maintaining sync:**
When updating either version:
1. Update version number in both files
2. Add changelog entry to annotated version
3. Ensure operational instructions match between versions
4. Annotated can have extended explanations, but core instructions must be identical

## Key Methodologies

### Iterative Multi-Perspective Conceptual Debugging - IMPCD (v3.0.0)

**Authoritative runtime:** [v3.0.0](methodologies/iterative-multi-perspective-debugging-v3.0.0-runtime.md)
**Migration:** [v2 → v3](methodologies/IMPCD-v3-MIGRATION.md)

Use the domain-neutral v3 loop for new conceptual reviews:

- Preserve author-owned intent and completion criteria. Propose additions for the author to accept.
- Hold the concept in an atomic claim ledger; regenerate readable output from it.
- Include anchor, adversary, minimalist, and two to five domain perspectives.
- Produce two independent revisions and apply only their substantive consensus.
- Record disagreement, tolerance, scope, decisions, locks, and disputed changes.
- Rank counterexamples above arguments above preferences. Preserve unresolved severity ≥8 findings.
- Report convergence, oscillation, growth guard, or iteration cap as the stop reason.
- Treat domain packs and constitutional material as optional. Packs cannot change the core loop.

The v2.1.1 runtime, annotated edition, and evaluations are historical. Do not
carry their weighted supermajority, fixed eleven-persona panel, mandatory audits,
pattern premiums, or semantic-similarity convergence into v3. Self-convergence
and persona agreement are not evidence of correctness. Do not claim independent
or cross-model testing that did not occur.

### Iterative Multi-Perspective Rhetorical Debugging - IMPRD (v1.0)

**Location:** `/papers/imprd_paper/` (academic paper + implementations)
**Paper:** 16 pages, 9.94/10 IMPRD-optimized score
**Status:** Ready for arXiv publication

IMPRD extends IMPCD from expert panels (conceptual debugging) to audience personas (content optimization). Key features:

- **Purpose**: Content optimization through structured multi-persona evaluation
- **Innovation**: Random odd-number persona sampling prevents local minima + enables tiebreaking
- **Validation**: n=28 applications across 3 orders of magnitude (100-100,000 words)
- **Results**: Mean improvement of 1.3 points (7.4 → 8.7), consistent convergence
- **Cost**: $0.50-$100 per content piece vs. $50-$1000 for professional editing

**Key distinction from IMPCD:**
- IMPCD debugs *concepts* (logical coherence, philosophical precision)
- IMPRD debugs *communication* (accessibility, engagement, rhetorical effectiveness)

**Convergence criteria:**
- Target score (e.g., ≥9.0/10)
- Floor constraints (no persona below threshold)
- Diminishing returns threshold (< 0.1 improvement)
- **Decline detection**: Stop when score decreases (signals over-optimization)

**Development history:**
The IMPRD paper itself was optimized using IMPRD:

1. Historical IMPCD v2 runs reported self-convergence under v2 criteria
2. IMPRD was derived from IMPCD v2
3. The IMPRD paper was optimized using IMPRD

These are development records, not independent validation of correctness or of IMPCD v3.

**When working with IMPRD:**
- Use random sampling of odd-number personas (7 or 9 from larger pool)
- Document all iteration scores to detect convergence or decline
- Back out changes that decrease scores
- Maintain audit trail with all evaluation scripts
- See `/papers/imprd_paper/FINAL_CONVERGED.md` for complete convergence trajectory example

## Working with This Repository

Since this is a documentation-based project, there are no build or test commands. The primary workflow is:

- Read existing methodologies to understand the framework's scope and style
- Create or refine methodologies/patterns based on observed reusable AI interaction patterns
- Ensure new content fits within the overall conceptual framework
- Keep patterns modular and composable
- Follow Semantic Versioning for methodologies that undergo iteration

## Conceptual Refinement

The core "conceptual refinement" pattern refers to the iterative process of:
1. Starting with a vague or partial concept
2. Systematically exploring dimensions and boundaries
3. Identifying ambiguities and edge cases
4. Progressively building a more precise understanding
5. Validating the refined concept through examples and counter-examples

Future patterns should either implement this core process or provide complementary tools for AI reasoning and interaction.
