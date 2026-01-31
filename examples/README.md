# Examples

This directory contains real applications and case studies demonstrating the methodologies and patterns in practice.

## What is an Example?

An example is a complete, real-world application showing:
- **Initial concept/problem**: What was being refined
- **Process followed**: Which methodology/patterns were used
- **Iterations**: How the concept evolved
- **Outcomes**: What was learned, what changed
- **Reflections**: What worked, what didn't, lessons learned

Examples help users understand how to apply the abstract methodologies to concrete situations.

## Example Structure

Each example should include:

1. **Context**: What prompted this refinement process
2. **Initial State**: The concept before refinement
3. **Process Used**: Which methodology/patterns/templates were applied
4. **Iteration Log**: Key changes across iterations (or link to git history)
5. **Final State**: The refined concept
6. **Outcomes**: Convergence metrics, minority reports, key discoveries
7. **Lessons Learned**: What worked, pitfalls encountered, advice for others
8. **Artifacts**: Links to git commits, full audit trails, etc.

## Existing Examples

### IMPCD Meta-Evaluation (4 iterations, CONVERGED)

**Files:**
- [Iteration 1](impcd-meta-evaluation-iteration-1.md) - FAILED (18.1% support)
- [Iteration 2](impcd-meta-evaluation-iteration-2.md) - PASSED (65.6% support)
- [Iteration 3](impcd-meta-evaluation-iteration-3.md) - UNANIMOUS (100% support, not yet stable)
- [Iteration 4](impcd-meta-evaluation-iteration-4.md) - CONVERGED (100% support, stable)

**Summary:**
The Iterative Multi-Perspective Conceptual Debugging methodology successfully evaluated itself, demonstrating both failure and success modes. Started with major concerns (statistical validity, cultural universality, misuse risks) and converged after addressing them through 4 iterations.

**Key Outcomes:**
- Total iterations to convergence: 4
- Final support: 100% unanimous
- All improvements incorporated into IMPCD v2.1.0
- Demonstrated methodology can identify its own limitations and iterate substantively

**What This Shows:**
- The methodology works on itself (meta-evaluation)
- Both failure mode (Iter 1) and success mode (Iter 4) documented
- Substantive improvements, not superficial compliance
- Convergence criteria all met (similarity >95%, support stable ±5%, no high-severity concerns)

## Types of Examples

We especially value:
- **Success cases**: Concepts that converged successfully
- **Failure cases**: Concepts that hit failure modes (oscillation, fragmentation, irreconcilable tensions)
- **Cross-LLM comparisons**: Same concept refined by different models
- **High-stakes applications**: Cases with real community involvement and external review
- **Domain-specific applications**: Showing how methodologies adapt to different fields

## Contributing

When adding an example:
- Maintain complete audit trails
- Include all disclaimers and limitations
- Document which LLM(s) were used
- Anonymize personal information appropriately
- Share both successes and failures (failures are valuable learning)
