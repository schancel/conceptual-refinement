# Methodologies

This directory contains complete, systematic frameworks for specific conceptual processes.

## Methodology Versions

Each methodology in this directory has two versions:

- **Runtime Core** (`-runtime.md`): Concise operational instructions (~150-200 lines)
- **Annotated** (`-annotated.md`): Full documentation with context (~600-800 lines)

See the main [CLAUDE.md](/CLAUDE.md) for guidance on when to use each version.

## Available Methodologies

### Iterative Multi-Perspective Conceptual Debugging (IMPCD) v2.1.1

**Runtime:** `iterative-multi-perspective-debugging-v2.1.1-runtime.md`
**Annotated:** `iterative-multi-perspective-debugging-v2.1.1-annotated.md`

A systematic process for stress-testing concepts through simulated diverse perspectives, structural pattern analysis, and weighted feedback aggregation.

**Key features:**
- Generate ~11 diverse personas spanning conflicting viewpoints
- Collect structured feedback (severity × confidence scoring)
- Apply structural pattern-based weighting
- Preserve high-severity minority concerns
- Git-tracked audit trail
- Cross-validated across Claude, ChatGPT, and Grok

**Purpose:** Conceptual debugging (not validation) — surfaces assumptions, conflicts, blindspots, and value tensions.

**Status:** STABLE (January 2026)

**See also:** [Structural Moral Realism constitution](../constitutions/) — recommended behavioral overlay for optimal consistency when running IMPCD.
