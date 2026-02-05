"""
Adaptive Concept Space Navigation
Like Runge-Kutta for numerical integration, but for linguistic concept space.

Key idea: Adjust step size based on local "conceptual curvature"
- Small steps near singularities (high curvature, rapid change)
- Large steps in smooth regions (low curvature, stable concepts)

Estimates curvature linguistically by asking LLM about rate of change.
"""

from typing import List, Dict, Tuple, Optional
import time
import math
from conceptual_calculus_linguistic import LinguisticConceptualOperators


class AdaptiveConceptNavigator:
    """
    Navigate concept space with adaptive step sizing.
    """

    def __init__(
        self,
        ops: LinguisticConceptualOperators,
        min_step: float = 0.1,
        max_step: float = 1.0,
        tolerance: float = 0.3
    ):
        """
        Initialize adaptive navigator.

        Args:
            ops: LinguisticConceptualOperators instance
            min_step: Minimum step size (for high curvature regions)
            max_step: Maximum step size (for smooth regions)
            tolerance: Error tolerance for step size adjustment
        """
        self.ops = ops
        self.min_step = min_step
        self.max_step = max_step
        self.tolerance = tolerance

    # ============================================================
    # CONCEPTUAL CURVATURE ESTIMATION
    # ============================================================

    def estimate_curvature(
        self,
        concept: str,
        direction: str
    ) -> float:
        """
        Estimate conceptual curvature in a direction.

        High curvature = concept changes rapidly in this direction
        Low curvature = concept changes gradually

        Args:
            concept: Starting concept
            direction: Direction descriptor (e.g., "more abstract", "opposite", "specialized")

        Returns:
            Curvature estimate (0-1, where 1 = highest curvature)
        """
        curvature_prompt = f"""Consider the concept "{concept}".

Imagine moving in this direction: {direction}

How rapidly does the concept change as we move in this direction?
- RAPID (1.0): Concept transforms fundamentally with small movement
- MODERATE (0.5): Concept changes but maintains core structure
- GRADUAL (0.0): Concept barely changes, very stable

Respond with just a number between 0.0 and 1.0."""

        try:
            time.sleep(0.6)
            response = self.ops._call_llm(curvature_prompt, max_tokens=10).strip()
            curvature = float(response)
            return max(0.0, min(1.0, curvature))

        except:
            return 0.5  # Default moderate curvature

    def estimate_density(self, concept: str) -> float:
        """
        Estimate conceptual density (how crowded the neighborhood is).

        High density = many closely-related concepts nearby
        Low density = sparse, isolated concept

        Args:
            concept: Concept to measure

        Returns:
            Density estimate (0-1, where 1 = highest density)
        """
        density_prompt = f"""Consider the concept "{concept}".

How many closely-related but distinct concepts are in its immediate neighborhood?
- DENSE (1.0): Surrounded by many subtle variations and related concepts
- MODERATE (0.5): Some related concepts, normal conceptual space
- SPARSE (0.0): Isolated, few related concepts nearby

Respond with just a number between 0.0 and 1.0."""

        try:
            time.sleep(0.6)
            response = self.ops._call_llm(density_prompt, max_tokens=10).strip()
            density = float(response)
            return max(0.0, min(1.0, density))

        except:
            return 0.5  # Default moderate density

    def detect_singularity_proximity(self, concept: str) -> float:
        """
        Estimate how close we are to a conceptual singularity.

        Singularities have:
        - High curvature (concepts change rapidly)
        - High density (many concepts converge)
        - Tension or ambiguity (no clear canonical term)

        Args:
            concept: Concept to check

        Returns:
            Proximity score (0-1, where 1 = at singularity)
        """
        proximity_prompt = f"""Consider the concept "{concept}".

Is this concept:
- A clear, well-defined concept with a canonical name? (0.0)
- Somewhat ambiguous, multiple interpretations exist? (0.5)
- At a boundary, intersection, or gap between concepts? (1.0)

How close is this to being an "unnamed" structural pattern that people circle around?

Respond with just a number between 0.0 and 1.0."""

        try:
            time.sleep(0.6)
            response = self.ops._call_llm(proximity_prompt, max_tokens=10).strip()
            proximity = float(response)
            return max(0.0, min(1.0, proximity))

        except:
            return 0.3  # Default low proximity

    # ============================================================
    # ADAPTIVE STEP SIZE CONTROL
    # ============================================================

    def compute_step_size(
        self,
        concept: str,
        direction: str,
        current_step: float
    ) -> float:
        """
        Compute adaptive step size based on local properties.

        Like Runge-Kutta: smaller steps where curvature is high,
        larger steps where space is smooth.

        Args:
            concept: Current concept
            direction: Direction of movement
            current_step: Current step size

        Returns:
            Adjusted step size
        """
        print(f"  📏 Computing adaptive step size...")

        # Estimate local properties
        curvature = self.estimate_curvature(concept, direction)
        density = self.estimate_density(concept)
        singularity = self.detect_singularity_proximity(concept)

        print(f"     Curvature: {curvature:.2f}, Density: {density:.2f}, Singularity: {singularity:.2f}")

        # Combine factors (higher values → smaller steps)
        complexity = (0.4 * curvature + 0.3 * density + 0.3 * singularity)

        # Adaptive step: inverse relationship with complexity
        # High complexity → small step
        # Low complexity → large step
        if complexity > 0.7:
            # High complexity: reduce step size
            step = current_step * 0.5
            reason = "high complexity"
        elif complexity < 0.3:
            # Low complexity: increase step size
            step = current_step * 1.5
            reason = "low complexity"
        else:
            # Moderate: maintain step
            step = current_step
            reason = "moderate complexity"

        # Clamp to bounds
        step = max(self.min_step, min(self.max_step, step))

        print(f"     Step: {current_step:.2f} → {step:.2f} ({reason})")

        return step

    # ============================================================
    # ADAPTIVE NAVIGATION
    # ============================================================

    def navigate_direction(
        self,
        start_concept: str,
        direction: str,
        n_steps: int = 5,
        initial_step: float = 0.5
    ) -> List[Dict[str, any]]:
        """
        Navigate in a direction with adaptive step sizing.

        Args:
            start_concept: Starting point
            direction: Direction to explore (e.g., "more abstract", "opposite")
            n_steps: Maximum number of steps
            initial_step: Initial step size

        Returns:
            List of concepts visited with metadata
        """
        print(f"\n🧭 ADAPTIVE NAVIGATION")
        print(f"   Start: '{start_concept}'")
        print(f"   Direction: {direction}")
        print(f"   Initial step: {initial_step}")

        trajectory = []
        current_concept = start_concept
        current_step = initial_step

        for i in range(n_steps):
            print(f"\n  Step {i+1}/{n_steps}: '{current_concept}'")

            # Compute adaptive step size
            step_size = self.compute_step_size(current_concept, direction, current_step)

            # Take step in direction
            # Step size encoded linguistically (e.g., "small step", "large leap")
            if step_size < 0.3:
                step_descriptor = "a very small, subtle shift"
            elif step_size < 0.5:
                step_descriptor = "a small step"
            elif step_size < 0.7:
                step_descriptor = "a moderate step"
            else:
                step_descriptor = "a large leap"

            step_prompt = f"""Starting from the concept "{current_concept}", take {step_descriptor} in this direction: {direction}

What concept do you arrive at after this step?
Respond with just the concept (1-5 words), nothing else."""

            try:
                time.sleep(0.8)
                next_concept = self.ops._call_llm(step_prompt, max_tokens=30).strip()

                # Record this step
                singularity_score = self.detect_singularity_proximity(next_concept)

                step_record = {
                    'step': i + 1,
                    'concept': next_concept,
                    'step_size': step_size,
                    'singularity_score': singularity_score,
                    'previous': current_concept
                }
                trajectory.append(step_record)

                print(f"     → Arrived at: '{next_concept}'")
                print(f"     Singularity score: {singularity_score:.2f}")

                # Check if we found a singularity
                if singularity_score > 0.7:
                    print(f"     🎯 SINGULARITY DETECTED!")

                    # Verify it's unnamed
                    verification_prompt = f"""Is "{next_concept}" a well-established, widely-recognized term with a clear canonical definition?

Respond with YES or NO and brief explanation."""

                    time.sleep(0.6)
                    verification = self.ops._call_llm(verification_prompt, max_tokens=100).strip()

                    if verification.startswith("NO"):
                        print(f"     ✨ UNNAMED SINGULARITY CONFIRMED")
                        step_record['is_unnamed_singularity'] = True
                        step_record['verification'] = verification
                        break  # Stop at singularity

                # Update for next iteration
                current_concept = next_concept
                current_step = step_size

            except Exception as e:
                print(f"     ⚠️  Error: {e}")
                break

        return trajectory

    # ============================================================
    # MULTI-DIRECTION SEARCH
    # ============================================================

    def search_from_seed(
        self,
        seed: str,
        directions: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Search multiple directions from a seed concept with adaptive steps.

        Args:
            seed: Starting concept
            directions: Directions to explore (default: standard set)

        Returns:
            Search results with discovered singularities
        """
        if directions is None:
            directions = [
                "more abstract",
                "more concrete",
                "opposite",
                "generalized",
                "specialized",
            ]

        print(f"\n{'='*70}")
        print(f"ADAPTIVE SEARCH FROM: '{seed}'")
        print(f"{'='*70}")

        all_trajectories = {}
        singularities_found = []

        for direction in directions:
            print(f"\n[Direction: {direction}]")

            trajectory = self.navigate_direction(
                start_concept=seed,
                direction=direction,
                n_steps=5,
                initial_step=0.5
            )

            all_trajectories[direction] = trajectory

            # Collect singularities
            for step in trajectory:
                if step.get('is_unnamed_singularity'):
                    singularities_found.append({
                        'concept': step['concept'],
                        'direction_from_seed': direction,
                        'seed': seed,
                        'verification': step['verification'],
                        'singularity_score': step['singularity_score']
                    })

        # Summary
        print(f"\n{'='*70}")
        print(f"SEARCH COMPLETE")
        print(f"{'='*70}")
        print(f"Directions explored: {len(directions)}")
        print(f"Unnamed singularities found: {len(singularities_found)}")

        if singularities_found:
            print(f"\n🎯 DISCOVERIES:")
            for i, sing in enumerate(singularities_found, 1):
                print(f"\n{i}. '{sing['concept']}'")
                print(f"   Found: {sing['direction_from_seed']} from '{sing['seed']}'")
                print(f"   Score: {sing['singularity_score']:.2f}")

        return {
            'seed': seed,
            'trajectories': all_trajectories,
            'singularities': singularities_found
        }


def run_adaptive_discovery():
    """
    Run adaptive concept space navigation.
    """
    print("\n🎯 ADAPTIVE CONCEPT SPACE NAVIGATION")
    print("Runge-Kutta-style exploration with linguistic step sizing\n")

    # Initialize
    ops = LinguisticConceptualOperators(
        provider="anthropic",
        model="claude-sonnet-4-5-20250929"
    )

    navigator = AdaptiveConceptNavigator(
        ops,
        min_step=0.1,
        max_step=1.0,
        tolerance=0.3
    )

    # Example: Search from interesting seed concepts
    seeds = [
        "emergence",
        "boundary",
        "potential",
    ]

    all_discoveries = []

    for seed in seeds:
        results = navigator.search_from_seed(seed)
        all_discoveries.extend(results['singularities'])
        time.sleep(2)  # Rate limiting between seeds

    # Final summary
    print(f"\n{'='*70}")
    print(f"TOTAL DISCOVERIES: {len(all_discoveries)}")
    print(f"{'='*70}")

    return all_discoveries


if __name__ == "__main__":
    discoveries = run_adaptive_discovery()
