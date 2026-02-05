"""
Singularity Operators - Efficient Discovery of Unnamed Concepts
Find points in concept space where multiple phrasings converge without a canonical term.

Singularity = structural pattern that:
1. Multiple people circle around with different phrases
2. Has coherent structure but no single accepted name
3. Sits at intersection or boundary of existing concepts

More efficient than Monte Carlo - directly probe for conceptual singularities.
"""

from typing import List, Dict, Tuple, Set, Optional
import time
from conceptual_calculus_linguistic import LinguisticConceptualOperators


class SingularityOperators:
    """
    Linguistic operators optimized for finding conceptual singularities.
    """

    def __init__(self, ops: LinguisticConceptualOperators):
        """
        Initialize with linguistic operators.

        Args:
            ops: LinguisticConceptualOperators instance
        """
        self.ops = ops

    # ============================================================
    # CONVERGENCE OPERATOR
    # ============================================================

    def convergence_operator(
        self,
        domains: List[str],
        prompt_seed: str
    ) -> Dict[str, any]:
        """
        Find where multiple domains converge on same structure.

        Singularities often appear at domain intersections - concepts that
        are important in multiple fields but don't have a unified name.

        Args:
            domains: List of domains to check (e.g., ["physics", "economics", "biology"])
            prompt_seed: What to look for (e.g., "equilibrium", "feedback", "boundary")

        Returns:
            Convergence point description
        """
        print(f"\n🎯 CONVERGENCE: Looking for '{prompt_seed}' across {len(domains)} domains...")

        domain_patterns = {}

        # Extract pattern from each domain
        for domain in domains:
            pattern_prompt = f"""In {domain}, what is the core structural pattern behind "{prompt_seed}"?
Describe the abstract structure in 1-2 sentences, focusing on the pattern itself.
Ignore domain-specific details - describe only the pure structure."""

            try:
                time.sleep(0.7)
                pattern = self.ops._call_llm(pattern_prompt, max_tokens=200).strip()
                domain_patterns[domain] = pattern
                print(f"  {domain}: {pattern[:60]}...")

            except Exception as e:
                print(f"  ⚠️  {domain}: Error - {e}")
                continue

        if len(domain_patterns) < 2:
            return {'converged': False, 'reason': 'insufficient_domains'}

        # Check if patterns converge
        patterns_list = list(domain_patterns.values())
        convergence_prompt = f"""Do these structural descriptions point to the same underlying pattern?

{chr(10).join(f'{i+1}. {p}' for i, p in enumerate(patterns_list))}

If YES: Describe the unified structural pattern they all share (1-2 sentences).
If NO: Explain why they're different.

Start your response with YES or NO."""

        try:
            time.sleep(0.8)
            response = self.ops._call_llm(convergence_prompt, max_tokens=300).strip()

            converged = response.startswith('YES')

            if converged:
                # Extract the unified pattern
                unified_pattern = response.replace('YES', '').strip(': ').strip()

                # Check if there's a canonical name
                naming_prompt = f"""This structural pattern appears across multiple domains:
{unified_pattern}

Is there a single, universally-accepted term for this pattern that works across all these domains?
If yes, what is it?
If no, explain why (in one sentence).

Format:
TERM: [term or "NONE"]
REASON: [explanation]"""

                time.sleep(0.7)
                naming_response = self.ops._call_llm(naming_prompt, max_tokens=150).strip()

                return {
                    'converged': True,
                    'unified_pattern': unified_pattern,
                    'domains': domains,
                    'domain_patterns': domain_patterns,
                    'naming_response': naming_response,
                    'is_singularity': 'NONE' in naming_response or 'no single' in naming_response.lower()
                }

            else:
                return {
                    'converged': False,
                    'reason': response,
                    'domains': domains,
                    'domain_patterns': domain_patterns
                }

        except Exception as e:
            return {'converged': False, 'error': str(e)}

    # ============================================================
    # TENSION OPERATOR
    # ============================================================

    def tension_operator(
        self,
        concept1: str,
        concept2: str
    ) -> Dict[str, any]:
        """
        Find the conceptual tension between similar-but-different concepts.

        Singularities often appear in the space between concepts that are
        "almost the same but not quite" - the distinction itself might be unnamed.

        Args:
            concept1, concept2: Similar but distinct concepts

        Returns:
            Tension point description
        """
        print(f"\n⚡ TENSION: Between '{concept1}' and '{concept2}'...")

        tension_prompt = f"""Consider these two concepts:
1. {concept1}
2. {concept2}

What is the key structural difference that distinguishes them?
Not superficial differences, but the core structural property that makes them distinct.

Describe this differentiating property in 1-2 sentences."""

        try:
            time.sleep(0.7)
            difference = self.ops._call_llm(tension_prompt, max_tokens=200).strip()

            print(f"  Difference: {difference[:80]}...")

            # Check if this differentiating property has a name
            naming_prompt = f"""This property distinguishes {concept1} from {concept2}:
"{difference}"

Is there a single, well-established word or phrase for this differentiating property?
If yes, what is it?
If no, why not?

Format:
TERM: [term or "NONE"]
EXPLANATION: [brief explanation]"""

            time.sleep(0.7)
            naming_response = self.ops._call_llm(naming_prompt, max_tokens=150).strip()

            is_singularity = 'NONE' in naming_response or 'no established' in naming_response.lower()

            if is_singularity:
                print(f"  🎯 SINGULARITY FOUND: Unnamed differentiating property")

            return {
                'concept1': concept1,
                'concept2': concept2,
                'tension_property': difference,
                'naming_response': naming_response,
                'is_singularity': is_singularity
            }

        except Exception as e:
            return {'error': str(e)}

    # ============================================================
    # INCOMPLETENESS OPERATOR
    # ============================================================

    def incompleteness_operator(
        self,
        category: str,
        known_members: List[str]
    ) -> Dict[str, any]:
        """
        Find gaps in conceptual coverage within a category.

        Singularities often appear as "missing" concepts - structures that
        should exist to complete a pattern but don't have names.

        Args:
            category: Conceptual category (e.g., "types of equilibrium")
            known_members: Known members of category

        Returns:
            Missing concept description
        """
        print(f"\n🕳️  INCOMPLETENESS: Gaps in '{category}'...")

        gap_prompt = f"""Consider this category: "{category}"

Known members:
{chr(10).join(f'- {m}' for m in known_members)}

Looking at the structural patterns of these members, what concepts are conspicuously missing?
What structural variants should exist but don't have well-known names?

List 2-3 missing structural variants, one per line."""

        try:
            time.sleep(0.8)
            response = self.ops._call_llm(gap_prompt, max_tokens=300).strip()

            gaps = [
                line.strip() for line in response.split('\n')
                if line.strip() and len(line.strip()) > 10
            ][:3]

            print(f"  Found {len(gaps)} potential gaps")

            # For each gap, check if it truly lacks a name
            singularities = []

            for gap in gaps:
                verification_prompt = f"""This structural variant was identified:
"{gap}"

Does this variant have a widely-accepted, standard name?
If yes, what is it?
If no, why do you think it lacks a standard name?

Format:
HAS_NAME: [yes/no]
TERM: [term if yes, or "NONE"]
EXPLANATION: [brief explanation]"""

                try:
                    time.sleep(0.7)
                    verification = self.ops._call_llm(verification_prompt, max_tokens=150).strip()

                    if 'HAS_NAME: no' in verification or 'TERM: NONE' in verification:
                        singularities.append({
                            'description': gap,
                            'verification': verification,
                            'category': category
                        })
                        print(f"    🎯 Unnamed: {gap[:60]}...")

                except Exception as e:
                    print(f"    ⚠️  Error verifying gap: {e}")
                    continue

            return {
                'category': category,
                'known_members': known_members,
                'gaps_found': gaps,
                'unnamed_gaps': singularities,
                'is_singularity': len(singularities) > 0
            }

        except Exception as e:
            return {'error': str(e)}

    # ============================================================
    # NEGATION OPERATOR
    # ============================================================

    def negation_operator(self, concept: str) -> Dict[str, any]:
        """
        Find boundary concepts: "not X, but almost X".

        Singularities often appear at concept boundaries - the property of
        being "almost but not quite" a concept may itself be unnamed.

        Args:
            concept: Concept to find boundaries of

        Returns:
            Boundary concept description
        """
        print(f"\n🚫 NEGATION: Boundary of '{concept}'...")

        boundary_prompt = f"""What is something that is NOT "{concept}", but is as close to it as possible without being it?

Describe the key structural property that makes it "almost {concept} but not quite."
Focus on the structural boundary, not specific examples.

Answer in 1-2 sentences."""

        try:
            time.sleep(0.7)
            boundary = self.ops._call_llm(boundary_prompt, max_tokens=200).strip()

            print(f"  Boundary: {boundary[:80]}...")

            # Check if this boundary property has a name
            naming_prompt = f"""This property describes the boundary of "{concept}":
"{boundary}"

Is there a standard term for this boundary property or this relationship to {concept}?
If yes, what is it?
If no, why not?

Format:
TERM: [term or "NONE"]
EXPLANATION: [brief]"""

            time.sleep(0.7)
            naming_response = self.ops._call_llm(naming_prompt, max_tokens=150).strip()

            is_singularity = 'TERM: NONE' in naming_response or 'no standard' in naming_response.lower()

            if is_singularity:
                print(f"  🎯 SINGULARITY: Unnamed boundary property")

            return {
                'concept': concept,
                'boundary_property': boundary,
                'naming_response': naming_response,
                'is_singularity': is_singularity
            }

        except Exception as e:
            return {'error': str(e)}

    # ============================================================
    # INTERSECTION OPERATOR
    # ============================================================

    def intersection_operator(
        self,
        concepts: List[str]
    ) -> Dict[str, any]:
        """
        Find the structural intersection of multiple concepts.

        Singularities often appear at intersections - the common structure
        shared by multiple concepts may lack its own name.

        Args:
            concepts: List of concepts to intersect (2-5 works best)

        Returns:
            Intersection description
        """
        print(f"\n∩ INTERSECTION: Of {len(concepts)} concepts...")

        intersection_prompt = f"""What structural property or pattern is shared by ALL of these concepts?

{chr(10).join(f'- {c}' for c in concepts)}

Describe the common structural core in 1-2 sentences.
Ignore superficial similarities - find the deep structural pattern."""

        try:
            time.sleep(0.8)
            core = self.ops._call_llm(intersection_prompt, max_tokens=200).strip()

            print(f"  Core: {core[:80]}...")

            # Check if this intersection has a name
            naming_prompt = f"""This structural pattern is the common core of {', '.join(concepts)}:
"{core}"

Is there a single, established term for this pattern?
If yes, what is it?
If no, why do you think it lacks a standard name?

Format:
TERM: [term or "NONE"]
EXPLANATION: [brief]"""

            time.sleep(0.7)
            naming_response = self.ops._call_llm(naming_prompt, max_tokens=150).strip()

            is_singularity = 'TERM: NONE' in naming_response or 'lacks' in naming_response.lower()

            if is_singularity:
                print(f"  🎯 SINGULARITY: Unnamed intersection pattern")

            return {
                'concepts': concepts,
                'intersection_pattern': core,
                'naming_response': naming_response,
                'is_singularity': is_singularity
            }

        except Exception as e:
            return {'error': str(e)}

    # ============================================================
    # DIRECTED DISCOVERY
    # ============================================================

    def find_singularities(
        self,
        strategy: str = "comprehensive",
        verbose: bool = True
    ) -> List[Dict[str, any]]:
        """
        Run multiple singularity operators to efficiently find unnamed concepts.

        Much more efficient than Monte Carlo - uses directed search.

        Args:
            strategy: "quick" (few operators), "comprehensive" (all operators)
            verbose: Print detailed progress

        Returns:
            List of discovered singularities
        """
        print("\n" + "="*70)
        print("SINGULARITY DISCOVERY - DIRECTED SEARCH")
        print("="*70)

        singularities = []

        # 1. Convergence across domains
        if strategy in ["comprehensive", "convergence"]:
            print("\n[1/5] CONVERGENCE OPERATOR")

            test_cases = [
                (["physics", "economics", "ecology"], "equilibrium"),
                (["mathematics", "biology", "computer science"], "recursion"),
                (["philosophy", "quantum mechanics", "theology"], "observer"),
            ]

            for domains, seed in test_cases:
                result = self.convergence_operator(domains, seed)
                if result.get('is_singularity'):
                    singularities.append({
                        'operator': 'convergence',
                        'seed': seed,
                        'data': result
                    })

        # 2. Tension between similar concepts
        if strategy in ["comprehensive", "tension"]:
            print("\n[2/5] TENSION OPERATOR")

            pairs = [
                ("knowledge", "wisdom"),
                ("complexity", "complication"),
                ("emergence", "aggregation"),
                ("potential", "possibility"),
            ]

            for c1, c2 in pairs:
                result = self.tension_operator(c1, c2)
                if result.get('is_singularity'):
                    singularities.append({
                        'operator': 'tension',
                        'pair': (c1, c2),
                        'data': result
                    })

        # 3. Incompleteness in categories
        if strategy in ["comprehensive", "incompleteness"]:
            print("\n[3/5] INCOMPLETENESS OPERATOR")

            categories = [
                ("types of symmetry", ["bilateral", "radial", "translational", "rotational"]),
                ("forms of causation", ["efficient", "formal", "material", "final"]),
            ]

            for category, members in categories:
                result = self.incompleteness_operator(category, members)
                if result.get('is_singularity'):
                    singularities.append({
                        'operator': 'incompleteness',
                        'category': category,
                        'data': result
                    })

        # 4. Boundaries (negation)
        if strategy in ["comprehensive", "negation"]:
            print("\n[4/5] NEGATION OPERATOR")

            boundary_concepts = ["alive", "conscious", "intelligent", "random"]

            for concept in boundary_concepts:
                result = self.negation_operator(concept)
                if result.get('is_singularity'):
                    singularities.append({
                        'operator': 'negation',
                        'concept': concept,
                        'data': result
                    })

        # 5. Intersections
        if strategy in ["comprehensive", "intersection"]:
            print("\n[5/5] INTERSECTION OPERATOR")

            intersections = [
                ["network", "organism", "ecosystem"],
                ["market", "democracy", "language"],
                ["algorithm", "recipe", "ritual"],
            ]

            for concept_set in intersections:
                result = self.intersection_operator(concept_set)
                if result.get('is_singularity'):
                    singularities.append({
                        'operator': 'intersection',
                        'concepts': concept_set,
                        'data': result
                    })

        # Summary
        print("\n" + "="*70)
        print("DISCOVERY COMPLETE")
        print("="*70)
        print(f"Singularities found: {len(singularities)}")

        for i, sing in enumerate(singularities, 1):
            print(f"\n{i}. [{sing['operator'].upper()}]")
            if 'seed' in sing:
                print(f"   Seed: {sing['seed']}")
            if 'pair' in sing:
                print(f"   Pair: {sing['pair']}")
            if 'category' in sing:
                print(f"   Category: {sing['category']}")

        return singularities


def run_singularity_discovery():
    """
    Run efficient singularity discovery.
    """
    print("\n🎯 SINGULARITY-BASED DISCOVERY")
    print("Efficient search for unnamed concepts using directed operators\n")

    # Initialize
    ops = LinguisticConceptualOperators(
        provider="anthropic",
        model="claude-sonnet-4-5-20250929"
    )

    singularity_ops = SingularityOperators(ops)

    # Run discovery (start with quick for testing)
    singularities = singularity_ops.find_singularities(
        strategy="quick",  # or "comprehensive"
        verbose=True
    )

    return singularities


if __name__ == "__main__":
    discoveries = run_singularity_discovery()
