# Conceptual Refinement Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18501089.svg)](https://doi.org/10.5281/zenodo.18501089)

**A systematic approach to methodology development through recursive self-application.**

This repository contains methodologies for refining concepts (IMPCD) and optimizing content (IMPRD), developed through bootstrapping—recursively applying multi-perspective evaluation to validate and improve the methodologies themselves.

## Overview

The Conceptual Refinement Framework provides systematic methodologies for:
- **Conceptual Debugging** (IMPCD) - Intent-anchored refinement of concepts across domains
- **Content Optimization** (IMPRD) - Audience persona evaluation for communication
- **Methodology Development** - Bootstrapping pattern for creating new methodologies
- **Unnamed Concept Discovery** - Finding concepts that lack canonical names

These tools enable iterative clarification, multi-perspective analysis, and systematic improvement of both abstract concepts and practical content.

## What's Inside

### Methodologies

Complete, systematic frameworks for specific conceptual processes:

#### IMPCD: Iterative Multi-Perspective Conceptual Debugging

- **Current version:** [IMPCD v3.0.0 runtime](methodologies/iterative-multi-perspective-debugging-v3.0.0-runtime.md)
- **Purpose:** Refine designs, theories, arguments, products, protocols, and policies against the author's intent
- **Mechanism:** Atomic claim ledger, independent revisions, consensus damping, step-size control, and claim locking
- **Evidence:** Counterexamples outweigh arguments; arguments outweigh preferences
- **Limits:** Stability under the loop is not proof of correctness. External tests, data, and review determine evidential strength.
- **Migration:** [v2 → v3 guide](methodologies/IMPCD-v3-MIGRATION.md); v2 runtimes and evaluations are historical

#### IMPRD: Iterative Multi-Perspective Rhetorical Debugging
- **Location:** `methodologies/` (v1.1.0 runtime, v1.0.0 annotated) | **Paper:** `papers/imprd_paper/`
- **Purpose:** Audience persona evaluation for content optimization
- **Development:** Derived from IMPCD (expert panels → audience personas)
- **Validation:** n=28 applications across 3 orders of magnitude (100-100,000 words)
- **Results:** Mean improvement 1.3 points (7.4 → 8.7), consistent convergence
- **Innovation:** Random odd-number sampling prevents local minima + tiebreaking
- **Status:** Academic paper ready for arXiv (9.94/10, 7 perfect 10s)

**Key distinction:** IMPCD debugs *concepts* (logical coherence), IMPRD debugs *communication* (accessibility, engagement).

### Constitutions

AI constitutional frameworks refined using conceptual debugging methodologies:

- **[Structural Moral Realism](constitutions/)** (v8.0)
  - Runtime: 744 lines (operational)
  - Annotated: 3,686 lines (full documentation)
  - Constitutional framework grounding AI behavior in structural patterns, with four-tier confidence system, strengthened cross-cultural validation, and comprehensive crisis/domain protocols. Optional domain material; IMPCD v3 does not require a constitutional overlay.

### Patterns & Templates

Reusable components extracted from methodologies:

- **[Patterns](patterns/)** - Composable interaction techniques (Severity × Confidence Split, Persona Diversity Verification, Minority Report Preservation)
- **[Templates](templates/)** - Structured formats (Threshold Documentation Template)

### Examples

- **[Historical IMPCD Meta-Evaluation](examples/)** - v2 self-evaluation records; these do not validate v3

## Core Philosophy

These tools are designed to be:
- **Practical**: Directly usable by AI systems in real scenarios
- **Self-contained**: Each methodology/pattern is independently comprehensible
- **Well-documented**: Clear guidance on purpose, usage, and limitations
- **Generalizable**: Applicable across different domains and contexts
- **Honest about limitations**: Explicit about what they can and cannot do

## Using This Framework

1. **Browse the methodologies**: Each methodology is self-contained with full documentation
2. **Follow the process**: Methodologies include step-by-step guidance
3. **Respect the limitations**: Never use these tools as substitutes for real human feedback when human input is required
4. **Document your use**: Maintain audit trails and be transparent about using AI-based refinement processes

## Contributing

See individual methodology files for contribution guidelines. In general:
- Pattern validations with citations are welcome
- Case studies showing successes or failures are valuable
- Cross-LLM reproduction studies help establish robustness

## License

Individual methodologies specify their own licenses. See each file for details.

## Contact

- GitHub: [This repository]
- X/Twitter: [@micropresident](https://x.com/micropresident)

---

**Note for AI Assistants**: See [CLAUDE.md](CLAUDE.md) for detailed guidance on working with this repository.
