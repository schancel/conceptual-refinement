"""
Unnamed Concept Discovery - Linguistic Approach
Navigate concept space linguistically to find structural patterns that lack canonical names.

The algorithm:
1. Seed random points in concept space (start with concept combinations)
2. Use linguistic operators to explore structure
3. Cluster by structural similarity (LLM judges similarity)
4. When a cluster exists without a canonical term → unnamed concept found!
5. Generate a name for it
"""

from typing import List, Dict, Tuple, Set, Optional
import random
import time
from collections import defaultdict
from conceptual_calculus_linguistic import LinguisticConceptualOperators


class UnnamedConceptDiscovery:
    """
    Discover concepts that exist structurally but lack canonical names.
    """

    def __init__(self, ops: LinguisticConceptualOperators):
        """
        Initialize with linguistic operators.

        Args:
            ops: LinguisticConceptualOperators instance
        """
        self.ops = ops
        self.explored_concepts = set()
        self.concept_clusters = []

    # ============================================================
    # CONCEPT SPACE NAVIGATION
    # ============================================================

    def generate_concept_seeds(self, n_seeds: int = 20) -> List[str]:
        """
        Generate random starting points in concept space.

        Strategy: Combine basic concepts in unexpected ways to find
        structural patterns that might not have names.

        Args:
            n_seeds: Number of seeds to generate

        Returns:
            List of concept descriptions (seeds)
        """
        print(f"\n🌱 Generating {n_seeds} concept seeds...")

        # Base concepts from different domains
        base_concepts = [
            # Abstract
            "pattern", "structure", "relationship", "transformation", "balance",
            "emergence", "constraint", "potential", "boundary", "flow",
            # Concrete
            "network", "cycle", "hierarchy", "symmetry", "resonance",
            "feedback", "threshold", "gradient", "interface", "medium",
        ]

        # Modifiers and contexts
        modifiers = [
            "recursive", "distributed", "dynamic", "latent", "nested",
            "emergent", "implicit", "collective", "transitional", "marginal",
        ]

        connectors = [
            "in", "between", "across", "through", "without",
            "despite", "beyond", "within", "from", "toward"
        ]

        seeds = []

        for i in range(n_seeds):
            # Strategy 1: Modified concept
            if random.random() < 0.4:
                mod = random.choice(modifiers)
                concept = random.choice(base_concepts)
                seed = f"{mod} {concept}"

            # Strategy 2: Relational concept
            elif random.random() < 0.7:
                concept1 = random.choice(base_concepts)
                concept2 = random.choice(base_concepts)
                conn = random.choice(connectors)
                seed = f"{concept1} {conn} {concept2}"

            # Strategy 3: Compound description
            else:
                mod = random.choice(modifiers)
                concept1 = random.choice(base_concepts)
                concept2 = random.choice(base_concepts)
                seed = f"{mod} {concept1} of {concept2}"

            seeds.append(seed)

        return seeds

    def explore_concept_neighborhood(
        self,
        seed: str,
        depth: int = 2
    ) -> List[Dict[str, any]]:
        """
        Explore the neighborhood around a concept seed.

        Use linguistic operators to generate related concepts and
        understand their structural properties.

        Args:
            seed: Starting concept description
            depth: How many hops to explore

        Returns:
            List of concept records with structure descriptions
        """
        print(f"\n🔍 Exploring neighborhood of: '{seed}'")

        concepts = []
        to_explore = [(seed, 0)]  # (concept, depth)
        explored = set()

        while to_explore and len(concepts) < 10:  # Limit exploration
            current, current_depth = to_explore.pop(0)

            if current in explored or current_depth >= depth:
                continue

            explored.add(current)

            # Ask LLM to describe the structural pattern
            structure_prompt = f"""What is the core structural pattern or principle behind this concept?
Concept: "{current}"

Describe the abstract structure in 1-2 sentences, focusing on the pattern itself, not examples."""

            try:
                time.sleep(0.7)  # Rate limiting
                structure = self.ops._call_llm(structure_prompt, max_tokens=200).strip()

                # Ask LLM to generate related structural concepts
                related_prompt = f"""Given this structural pattern:
"{structure}"

List 3 other concepts (potentially unnamed or unfamiliar) that share this same structural pattern.
List one per line, just the concept descriptions."""

                time.sleep(0.7)
                related_response = self.ops._call_llm(related_prompt, max_tokens=200).strip()
                related = [
                    line.strip() for line in related_response.split('\n')
                    if line.strip() and len(line.strip()) > 5
                ][:3]

                # Record this concept
                concepts.append({
                    'description': current,
                    'structure': structure,
                    'depth': current_depth,
                    'related': related
                })

                # Add related concepts to exploration queue
                for r in related:
                    if r not in explored:
                        to_explore.append((r, current_depth + 1))

                print(f"  Depth {current_depth}: Found {len(related)} related concepts")

            except Exception as e:
                print(f"  ⚠️  Error exploring '{current}': {e}")
                continue

        return concepts

    # ============================================================
    # CLUSTERING & UNNAMED CONCEPT DETECTION
    # ============================================================

    def cluster_by_structure(
        self,
        concepts: List[Dict[str, any]],
        similarity_threshold: float = 0.7
    ) -> List[List[Dict[str, any]]]:
        """
        Cluster concepts by structural similarity.

        Use LLM to judge if structures are similar.

        Args:
            concepts: List of concept records
            similarity_threshold: Threshold for clustering

        Returns:
            List of clusters (each cluster is list of concept records)
        """
        print(f"\n🔗 Clustering {len(concepts)} concepts by structural similarity...")

        clusters = []

        for concept in concepts:
            placed = False

            # Try to place in existing cluster
            for cluster in clusters:
                # Compare with cluster representative (first element)
                rep = cluster[0]

                similarity_prompt = f"""Compare these two structural descriptions:
1. {concept['structure']}
2. {rep['structure']}

Are these describing the same or very similar structural patterns?
Respond with just 'yes' or 'no'."""

                try:
                    time.sleep(0.5)
                    similar = self.ops._call_llm(similarity_prompt, max_tokens=10).strip().lower()

                    if 'yes' in similar:
                        cluster.append(concept)
                        placed = True
                        break

                except:
                    continue

            # Create new cluster if not placed
            if not placed:
                clusters.append([concept])

        print(f"  Found {len(clusters)} structural clusters")
        return clusters

    def check_if_unnamed(self, cluster: List[Dict[str, any]]) -> Tuple[bool, str]:
        """
        Check if a cluster represents an unnamed concept.

        A concept is "unnamed" if:
        1. Multiple descriptions point to same structure
        2. No single canonical term captures it
        3. People circle around it with different phrases

        Args:
            cluster: Cluster of structurally similar concepts

        Returns:
            (is_unnamed, canonical_term_or_reason)
        """
        if len(cluster) < 2:
            return False, "cluster too small"

        # Gather all descriptions
        descriptions = [c['description'] for c in cluster]
        structures = [c['structure'] for c in cluster]

        # Ask LLM if there's a canonical term
        canonical_prompt = f"""These descriptions all point to a similar structural pattern:
{chr(10).join(f'{i+1}. {d}' for i, d in enumerate(descriptions[:5]))}

Is there a single, widely-recognized word or short phrase that captures this pattern?
If yes, respond with the word/phrase.
If no, respond with "UNNAMED" and explain why in one sentence."""

        try:
            time.sleep(0.8)
            response = self.ops._call_llm(canonical_prompt, max_tokens=100).strip()

            is_unnamed = response.startswith("UNNAMED") or "no single" in response.lower()

            return is_unnamed, response

        except Exception as e:
            return False, f"error: {e}"

    def generate_name(self, cluster: List[Dict[str, any]]) -> Dict[str, any]:
        """
        Generate a name for an unnamed concept.

        Args:
            cluster: Cluster representing the unnamed concept

        Returns:
            Dictionary with proposed name and explanation
        """
        print(f"\n✨ Generating name for unnamed concept...")

        # Synthesize the pattern
        descriptions = [c['description'] for c in cluster]
        structures = [c['structure'] for c in cluster]

        synthesis_prompt = f"""These descriptions all point to the same structural pattern:
{chr(10).join(f'- {d}' for d in descriptions[:5])}

Structural pattern:
{structures[0]}

This pattern doesn't have a widely-recognized name yet. Propose a concise term (1-3 words) that captures this pattern.
Also provide a brief definition (1-2 sentences).

Format:
TERM: [proposed name]
DEFINITION: [definition]"""

        try:
            time.sleep(0.8)
            response = self.ops._call_llm(synthesis_prompt, max_tokens=200).strip()

            # Parse response
            lines = response.split('\n')
            term = "unnamed"
            definition = "structural pattern without canonical name"

            for line in lines:
                if line.startswith("TERM:"):
                    term = line.replace("TERM:", "").strip()
                elif line.startswith("DEFINITION:"):
                    definition = line.replace("DEFINITION:", "").strip()

            return {
                'proposed_term': term,
                'definition': definition,
                'examples': descriptions[:5],
                'structure': structures[0],
                'cluster_size': len(cluster)
            }

        except Exception as e:
            return {
                'proposed_term': 'unnamed_concept',
                'definition': f'Error generating name: {e}',
                'examples': descriptions[:5],
                'structure': structures[0] if structures else 'unknown',
                'cluster_size': len(cluster)
            }

    # ============================================================
    # MAIN DISCOVERY PIPELINE
    # ============================================================

    def discover_unnamed_concepts(
        self,
        n_seeds: int = 10,
        exploration_depth: int = 2,
        min_cluster_size: int = 2
    ) -> List[Dict[str, any]]:
        """
        Run the full unnamed concept discovery pipeline.

        1. Generate concept seeds (random points in concept space)
        2. Explore neighborhoods around each seed
        3. Cluster concepts by structural similarity
        4. Identify clusters without canonical names
        5. Generate names for unnamed concepts

        Args:
            n_seeds: Number of random starting points
            exploration_depth: How deep to explore around each seed
            min_cluster_size: Minimum size for unnamed concept candidacy

        Returns:
            List of unnamed concept discoveries
        """
        print("\n" + "="*70)
        print("UNNAMED CONCEPT DISCOVERY PIPELINE")
        print("="*70)

        # Phase 1: Generate seeds
        seeds = self.generate_concept_seeds(n_seeds)

        # Phase 2: Explore neighborhoods
        all_concepts = []
        for i, seed in enumerate(seeds[:n_seeds], 1):
            print(f"\n[{i}/{n_seeds}] Exploring seed: '{seed}'")
            try:
                neighborhood = self.explore_concept_neighborhood(seed, exploration_depth)
                all_concepts.extend(neighborhood)
                time.sleep(1)  # Rate limiting between seeds
            except Exception as e:
                print(f"  ⚠️  Error with seed '{seed}': {e}")
                continue

        print(f"\n📊 Explored {len(all_concepts)} concepts total")

        # Phase 3: Cluster by structure
        clusters = self.cluster_by_structure(all_concepts)

        # Phase 4: Identify unnamed concepts
        unnamed_concepts = []

        for i, cluster in enumerate(clusters, 1):
            if len(cluster) >= min_cluster_size:
                print(f"\n🔍 Checking cluster {i} (size: {len(cluster)})")

                is_unnamed, explanation = self.check_if_unnamed(cluster)

                if is_unnamed:
                    print(f"  ✨ UNNAMED CONCEPT FOUND!")
                    print(f"  Reason: {explanation}")

                    # Generate name
                    named_concept = self.generate_name(cluster)
                    unnamed_concepts.append(named_concept)

                    print(f"  📛 Proposed name: '{named_concept['proposed_term']}'")
                    print(f"  📝 Definition: {named_concept['definition']}")

                else:
                    print(f"  ✓ Has canonical term: {explanation}")

        # Final report
        print("\n" + "="*70)
        print(f"DISCOVERY COMPLETE")
        print("="*70)
        print(f"Seeds explored: {n_seeds}")
        print(f"Concepts found: {len(all_concepts)}")
        print(f"Structural clusters: {len(clusters)}")
        print(f"Unnamed concepts discovered: {len(unnamed_concepts)}")
        print("="*70)

        return unnamed_concepts


def run_discovery(n_seeds: int = 5):
    """
    Run unnamed concept discovery.

    Args:
        n_seeds: Number of random starting points (start small for testing)
    """
    print("\n🔬 UNNAMED CONCEPT DISCOVERY")
    print("Finding structural patterns that lack canonical names...\n")

    # Initialize operators
    ops = LinguisticConceptualOperators(
        provider="anthropic",
        model="claude-sonnet-4-5-20250929"
    )

    # Initialize discovery engine
    discovery = UnnamedConceptDiscovery(ops)

    # Run discovery
    unnamed_concepts = discovery.discover_unnamed_concepts(
        n_seeds=n_seeds,
        exploration_depth=2,
        min_cluster_size=2
    )

    # Display results
    if unnamed_concepts:
        print("\n" + "="*70)
        print("🎉 UNNAMED CONCEPTS DISCOVERED")
        print("="*70)

        for i, concept in enumerate(unnamed_concepts, 1):
            print(f"\n{i}. {concept['proposed_term'].upper()}")
            print(f"   Definition: {concept['definition']}")
            print(f"   Cluster size: {concept['cluster_size']}")
            print(f"   Examples:")
            for j, ex in enumerate(concept['examples'][:3], 1):
                print(f"     {j}. {ex}")
            print(f"   Structure: {concept['structure'][:100]}...")

    else:
        print("\n❌ No unnamed concepts discovered in this run.")
        print("Try increasing n_seeds or adjusting cluster parameters.")

    return unnamed_concepts


if __name__ == "__main__":
    # Run with small number of seeds for testing
    # Increase for more thorough exploration
    discoveries = run_discovery(n_seeds=5)
