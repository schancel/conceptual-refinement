# Patterns

This directory contains smaller, composable interaction patterns that can be used independently or combined.

## What is a Pattern?

A pattern is a focused, reusable technique for a specific aspect of AI reasoning or interaction. Patterns are:
- **Narrower in scope** than full methodologies
- **Composable** - can be combined with other patterns
- **Immediately applicable** - can be used without extensive setup

## Pattern Structure

Each pattern should include:

1. **Name & Purpose**: What the pattern does
2. **When to Use**: Situations where this pattern applies
3. **Prerequisites**: What you need before using this pattern
4. **Process**: Step-by-step application
5. **Example**: Concrete demonstration
6. **Variations**: Alternative approaches or adaptations
7. **Pitfalls**: Common mistakes to avoid
8. **Related Patterns**: Complementary or alternative patterns

## Existing Patterns

### Core Feedback Collection Patterns

- **[Severity × Confidence Split](severity-confidence-split.md)** - Separate harm magnitude from likelihood to reduce bias and gaming in evaluation systems

- **[Persona Diversity Verification](persona-diversity-verification.md)** - Ensure evaluators represent genuine conflicting perspectives across ideological, stakeholder, expertise, demographic, power, and conflict-of-interest dimensions

- **[Minority Report Preservation](minority-report-preservation.md)** - Protect high-severity dissenting views (≤4 evaluators, severity ≥8, confidence ≥7) from being averaged away by majority consensus

## Contributing

When adding a new pattern:
- Use descriptive, verb-oriented filenames (e.g., `assumption-extraction.md`)
- Ensure it's genuinely reusable across contexts
- Cross-reference related patterns
- Include at least one concrete example
