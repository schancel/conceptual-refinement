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
/constitutions/     - AI constitutional frameworks refined using conceptual debugging
                      (e.g., structural-moral-realism-v8.0.md)
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

## Key Methodologies

### Iterative Multi-Perspective Conceptual Debugging (v2.0.0)

Located at: `/methodologies/iterative-multi-perspective-debugging.md`

This is the flagship methodology - a systematic process for stress-testing concepts through simulated diverse perspectives. Key features:

- **Purpose**: Conceptual debugging (not validation) - surfaces assumptions, conflicts, blindspots, value tensions
- **Core mechanism**: Generate ~11 diverse personas, collect structured feedback (severity × confidence scoring), apply structural pattern-based weighting
- **Versioning**: Follows Semantic Versioning 2.0.0 (MAJOR.MINOR.PATCH)
- **Evidence tiers**: Provisional / Validated / Highly Validated with corresponding premium ranges
- **Git tracking**: Each iteration must be committed with full audit trail
- **Cross-LLM validated**: Tested across Claude, ChatGPT, and Grok with convergent results

**When working with this methodology:**
- **Load Structural Moral Realism v8.0** (in `/constitutions/`) as behavioral overlay for optimal consistency
- Maintain all disclaimers and limitations sections
- Document structural patterns with evidence levels and citations
- Use the 7-element template for threshold/tipping-point documentation
- Prefer quantitative threshold estimates over qualitative when available
- Conduct all three mandatory audits (Power & Incentives, Operator Integrity, Model Bias)
- Involve real community members for culturally-sensitive or marginalized-community-affecting concepts
- The constitution provides pre-validated structural patterns to draw from during evaluation

**Version updates:**
- MAJOR: Incompatible changes or new subsystems
- MINOR: Backwards-compatible features
- PATCH: Bug fixes, clarifications

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
