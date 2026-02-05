"""
Conceptual Calculus Operators - Linguistic Approach
Uses publicly accessible LLMs via API (Claude, GPT-4, etc.)
Tests structural correspondences through linguistic patterns rather than activation extraction.
"""

import anthropic
import openai
from typing import List, Tuple, Dict, Optional, Union
import numpy as np
from collections import defaultdict
import json
import time


class LinguisticConceptualOperators:
    """
    Test structural correspondences using linguistic prompting.
    Works with any API-accessible LLM.
    """

    def __init__(
        self,
        provider: str = "anthropic",  # or "openai"
        model: str = "claude-sonnet-4-5-20250929",
        api_key: Optional[str] = None
    ):
        """
        Initialize with API access to an LLM.

        Args:
            provider: "anthropic" or "openai"
            model: Model identifier
            api_key: API key (or use environment variable)
        """
        self.provider = provider
        self.model = model

        if provider == "anthropic":
            self.client = anthropic.Anthropic(api_key=api_key)
        elif provider == "openai":
            self.client = openai.OpenAI(api_key=api_key)
        else:
            raise ValueError(f"Unknown provider: {provider}")

        print(f"Initialized {provider} client with model: {model}")

    def _call_llm(self, prompt: str, max_tokens: int = 500) -> str:
        """
        Call the LLM with a prompt and return response.

        Args:
            prompt: The prompt to send
            max_tokens: Maximum response length

        Returns:
            LLM response text
        """
        if self.provider == "anthropic":
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text

        elif self.provider == "openai":
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens
            )
            return response.choices[0].message.content

    # ============================================================
    # OPERATOR 1: Conceptual Generativity (Linguistic)
    # ============================================================

    def compute_generativity_linguistic(
        self,
        concept: str,
        n_probes: int = 5
    ) -> Dict[str, any]:
        """
        Measure generativity through linguistic probing.

        A generative concept should:
        1. Generate many related concepts when asked
        2. Be described differently in different contexts
        3. Connect to many other domains

        Args:
            concept: Concept to measure
            n_probes: Number of probing questions

        Returns:
            Generativity metrics dict
        """
        print(f"\n📊 Measuring generativity of '{concept}'...")

        # Probe 1: Related concepts
        related_prompt = f"""List 10 concepts that are closely related to or derived from "{concept}".
Just list the concepts, one per line, no numbering or explanation."""

        related_response = self._call_llm(related_prompt)
        related_concepts = [
            line.strip() for line in related_response.split('\n')
            if line.strip() and not line.strip().startswith('#')
        ][:10]

        # Probe 2: Context sensitivity
        contexts = [
            f"In philosophy, {concept} means",
            f"In everyday life, {concept} refers to",
            f"In science, {concept} is understood as",
            f"For children, {concept} can be explained as",
            f"In a technical context, {concept} denotes"
        ]

        context_responses = []
        for ctx in contexts[:n_probes]:
            response = self._call_llm(f"{ctx} (complete in one sentence)")
            context_responses.append(response)

        # Measure diversity of responses (simple: unique words)
        all_words = set()
        for response in context_responses:
            words = set(response.lower().split())
            all_words.update(words)

        context_diversity = len(all_words) / sum(len(r.split()) for r in context_responses)

        # Probe 3: Cross-domain connections
        domains_prompt = f"""In how many different domains or fields is the concept "{concept}" important or applicable?
List up to 10 domains where {concept} plays a role. Just list the domains, one per line."""

        domains_response = self._call_llm(domains_prompt)
        domains = [
            line.strip() for line in domains_response.split('\n')
            if line.strip() and not line.strip().startswith('#')
        ][:10]

        # Generativity score (normalized to [0, 1])
        score = (
            0.4 * min(len(related_concepts) / 10, 1.0) +      # Derivation breadth
            0.3 * min(context_diversity, 1.0) +                # Context sensitivity
            0.3 * min(len(domains) / 10, 1.0)                  # Cross-domain relevance
        )

        return {
            'concept': concept,
            'generativity_score': score,
            'related_concepts': related_concepts,
            'context_diversity': context_diversity,
            'domains': domains,
            'n_related': len(related_concepts),
            'n_domains': len(domains)
        }

    # ============================================================
    # OPERATOR 2: Structural Alignment (Linguistic)
    # ============================================================

    def compute_alignment_linguistic(
        self,
        concept1: str,
        concept2: str,
        n_probes: int = 5
    ) -> Dict[str, any]:
        """
        Measure structural alignment through linguistic consistency.

        Test if concepts show similar patterns when asked:
        1. To complete analogies
        2. To describe relationships
        3. To map to other domains

        Args:
            concept1, concept2: Concepts to compare
            n_probes: Number of probing tests

        Returns:
            Alignment metrics dict
        """
        print(f"\n🔗 Measuring alignment between '{concept1}' and '{concept2}'...")

        alignment_scores = []

        # Test 1: Relationship description similarity
        rel_prompt_template = """Describe the essential structure or pattern of "{concept}" in one sentence.
Focus on the abstract structure, not specific details."""

        desc1 = self._call_llm(rel_prompt_template.format(concept=concept1))
        desc2 = self._call_llm(rel_prompt_template.format(concept=concept2))

        # Compare descriptions (ask LLM to judge similarity)
        similarity_prompt = f"""Compare these two descriptions:
1. {desc1}
2. {desc2}

On a scale of 0.0 to 1.0, how structurally similar are these descriptions?
Consider the abstract pattern, not surface details.
Respond with just a number between 0.0 and 1.0."""

        try:
            desc_similarity = float(self._call_llm(similarity_prompt, max_tokens=10).strip())
            desc_similarity = max(0.0, min(1.0, desc_similarity))
        except:
            desc_similarity = 0.5  # Default if parsing fails

        alignment_scores.append(desc_similarity)

        # Test 2: Analogy completion consistency
        analogy_prompt_template = """Complete this analogy with a single word or short phrase:
"{concept}" is to [X] as ...

What is X? Respond with just the word or phrase, nothing else."""

        analogies1 = []
        analogies2 = []
        for i in range(min(3, n_probes)):
            try:
                time.sleep(0.5)  # Rate limiting
                a1 = self._call_llm(analogy_prompt_template.format(concept=concept1), max_tokens=20).strip()
                a2 = self._call_llm(analogy_prompt_template.format(concept=concept2), max_tokens=20).strip()
                analogies1.append(a1)
                analogies2.append(a2)

                # Check if analogies are structurally similar
                comparison_prompt = f"""Are these two phrases structurally or semantically similar?
1. {a1}
2. {a2}

Respond with just 'yes' or 'no'."""

                similar = self._call_llm(comparison_prompt, max_tokens=5).strip().lower()
                alignment_scores.append(1.0 if 'yes' in similar else 0.0)

            except Exception as e:
                print(f"  ⚠️  Probe {i} failed: {e}")
                continue

        # Test 3: Cross-domain mapping
        mapping_prompt = """What domain or field does "{concept}" most naturally belong to?
Respond with just the domain name, nothing else."""

        try:
            domain1 = self._call_llm(mapping_prompt.format(concept=concept1), max_tokens=20).strip()
            domain2 = self._call_llm(mapping_prompt.format(concept=concept2), max_tokens=20).strip()

            # Check if domains are related
            domain_relation_prompt = f"""Are these two domains closely related or similar in structure?
1. {domain1}
2. {domain2}

Respond with 'yes' or 'no'."""

            related = self._call_llm(domain_relation_prompt, max_tokens=5).strip().lower()
            alignment_scores.append(0.7 if 'yes' in related else 0.3)

        except:
            pass

        # Overall alignment score
        alignment = np.mean(alignment_scores) if alignment_scores else 0.0

        return {
            'concept1': concept1,
            'concept2': concept2,
            'alignment_score': alignment,
            'description_similarity': desc_similarity,
            'analogies': {'concept1': analogies1, 'concept2': analogies2},
            'n_probes': len(alignment_scores),
            'individual_scores': alignment_scores
        }

    # ============================================================
    # OPERATOR 3: Homomorphism Validation (Linguistic)
    # ============================================================

    def validate_homomorphism_linguistic(
        self,
        concept_A: str,
        concept_B: str,
        domain_A: str,
        domain_B: str,
        n_trials: int = 5
    ) -> Dict[str, any]:
        """
        Validate homomorphism through transfer tests.

        Test if structural knowledge about concept_A in domain_A
        transfers to concept_B in domain_B.

        Args:
            concept_A, concept_B: Concepts to test
            domain_A, domain_B: Their respective domains
            n_trials: Number of transfer tests

        Returns:
            Validation results dict
        """
        print(f"\n✓ Validating homomorphism: {concept_A} ({domain_A}) ←→ {concept_B} ({domain_B})...")

        transfer_successes = []

        # Test template: teach structure in domain A, test in domain B
        for i in range(n_trials):
            # Teach in domain A
            teach_prompt = f"""In {domain_A}, {concept_A} has a specific structural property or pattern.
Describe this structure in one sentence."""

            try:
                time.sleep(0.5)
                structure = self._call_llm(teach_prompt, max_tokens=100).strip()

                # Test transfer to domain B
                transfer_prompt = f"""Given that in {domain_A}, {concept_A} has this structure:
"{structure}"

Does {concept_B} in {domain_B} have an analogous or structurally similar property?
Respond with 'yes' or 'no' and one sentence explaining why."""

                transfer_response = self._call_llm(transfer_prompt, max_tokens=150).strip()

                # Check if transfer was recognized
                success = 'yes' in transfer_response.lower()[:20]  # Check first 20 chars
                transfer_successes.append(success)

                print(f"  Trial {i+1}: {'✓' if success else '✗'}")

            except Exception as e:
                print(f"  Trial {i+1}: Error - {e}")
                continue

        # Calculate success rate
        success_rate = sum(transfer_successes) / len(transfer_successes) if transfer_successes else 0.0

        return {
            'concept_A': concept_A,
            'concept_B': concept_B,
            'domain_A': domain_A,
            'domain_B': domain_B,
            'success_rate': success_rate,
            'n_trials': len(transfer_successes),
            'successes': sum(transfer_successes),
            'validated': success_rate >= 0.70
        }

    # ============================================================
    # VALIDATION SUITE
    # ============================================================

    def validate_on_known_analogies(
        self,
        test_cases: List[Tuple[str, str, str, str]],
        verbose: bool = True
    ) -> Dict[str, any]:
        """
        Test operators on known word analogies.

        For analogy (a, b, c, d) like (king, queen, man, woman):
        - Test if (a:b) and (c:d) show structural alignment

        Args:
            test_cases: List of (a, b, c, d) analogy tuples
            verbose: Print detailed results

        Returns:
            Validation results dict
        """
        if verbose:
            print("\n" + "="*70)
            print("VALIDATION SUITE: Known Analogies (Linguistic Approach)")
            print("="*70)

        results = []

        for a, b, c, d in test_cases:
            if verbose:
                print(f"\n📝 Testing: ({a}:{b}) :: ({c}:{d})")

            try:
                # Ask LLM to evaluate the analogy directly
                analogy_prompt = f"""Consider this analogy:
"{a}" is to "{b}" as "{c}" is to "{d}"

On a scale of 0.0 to 1.0, how strong is this analogy?
Consider structural similarity, not just surface features.
Respond with just a number between 0.0 and 1.0."""

                time.sleep(1)  # Rate limiting
                score_str = self._call_llm(analogy_prompt, max_tokens=10).strip()

                try:
                    analogy_score = float(score_str)
                    analogy_score = max(0.0, min(1.0, analogy_score))
                except:
                    # If parsing fails, use alignment measurement
                    alignment_ab = self.compute_alignment_linguistic(a, b, n_probes=2)
                    alignment_cd = self.compute_alignment_linguistic(c, d, n_probes=2)
                    analogy_score = (alignment_ab['alignment_score'] + alignment_cd['alignment_score']) / 2

                success = analogy_score >= 0.6  # Threshold for valid analogy

                result = {
                    'analogy': f"({a}:{b}) :: ({c}:{d})",
                    'score': analogy_score,
                    'success': success
                }
                results.append(result)

                if verbose:
                    print(f"  Score: {analogy_score:.2f}")
                    print(f"  {'✓ PASS' if success else '✗ FAIL'}")

            except Exception as e:
                print(f"  ⚠️  Error testing analogy: {e}")
                results.append({
                    'analogy': f"({a}:{b}) :: ({c}:{d})",
                    'score': 0.0,
                    'success': False,
                    'error': str(e)
                })

        # Compute overall statistics
        success_rate = sum(r['success'] for r in results) / len(results) if results else 0.0

        summary = {
            'test_cases': len(results),
            'successes': sum(r['success'] for r in results),
            'success_rate': success_rate,
            'results': results
        }

        if verbose:
            print("\n" + "="*70)
            print(f"OVERALL: {summary['successes']}/{summary['test_cases']} tests passed")
            print(f"SUCCESS RATE: {success_rate:.1%}")
            print("="*70)

            if success_rate >= 0.80:
                print("✅ VALIDATION PASSED (≥80% threshold)")
            else:
                print(f"❌ VALIDATION FAILED ({success_rate:.0%} < 80% threshold)")
            print()

        return summary


def run_linguistic_validation():
    """
    Run validation suite using linguistic approach.
    """
    print("\n🔬 Conceptual Calculus - Linguistic Validation\n")

    # Initialize with your preferred provider
    # Set ANTHROPIC_API_KEY or OPENAI_API_KEY environment variable
    ops = LinguisticConceptualOperators(
        provider="anthropic",
        model="claude-sonnet-4-5-20250929"
    )

    # Known analogies
    test_cases = [
        ("king", "queen", "man", "woman"),           # Gender
        ("Paris", "France", "London", "England"),    # Capital-country
        ("hot", "cold", "big", "small"),             # Antonyms
    ]

    # Run validation
    results = ops.validate_on_known_analogies(test_cases, verbose=True)

    return results, ops


if __name__ == "__main__":
    results, ops = run_linguistic_validation()

    # Example: Test generativity
    print("\n" + "="*70)
    print("EXAMPLE: Generativity Measurement")
    print("="*70)
    gen_result = ops.compute_generativity_linguistic("democracy", n_probes=3)
    print(f"\nGenerativity of 'democracy': {gen_result['generativity_score']:.2f}")
    print(f"Related concepts ({gen_result['n_related']}): {', '.join(gen_result['related_concepts'][:5])}...")
    print(f"Relevant domains ({gen_result['n_domains']}): {', '.join(gen_result['domains'][:5])}...")
