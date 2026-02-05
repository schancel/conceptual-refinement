"""
Conceptual Calculus Operators - Implementation
Validates methodology on known analogies, then discovers unnamed concepts.
"""

import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer
from scipy.stats import entropy
from scipy.spatial.distance import cosine
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Tuple, Dict, Optional
import warnings
warnings.filterwarnings('ignore')


class ConceptualCalculusOperators:
    """
    Implementation of conceptual calculus operators for discovering
    cross-domain structural correspondences in LLM activation space.
    """

    def __init__(
        self,
        model_name: str = "gpt2",
        layer: Optional[int] = None,
        n_contexts: int = 20,
        device: str = "cpu"
    ):
        """
        Initialize operators with a transformer model.

        Args:
            model_name: HuggingFace model identifier
            layer: Target layer (None = auto-select middle layer)
            n_contexts: Number of contexts for multi-context averaging
            device: "cuda" or "cpu"
        """
        print(f"Loading model: {model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(
            model_name,
            output_hidden_states=True,
            output_attentions=True
        ).to(device)
        self.model.eval()

        self.device = device
        self.n_contexts = n_contexts

        # Auto-select middle layer if not specified
        self.n_layers = self.model.config.n_layer
        self.layer = layer if layer is not None else self.n_layers // 2

        print(f"Using layer {self.layer} of {self.n_layers} total layers")

        # Add padding token if missing
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

    def _get_activation(self, text: str, layer: Optional[int] = None) -> np.ndarray:
        """
        Extract activation vector for text at specified layer.

        Args:
            text: Input text
            layer: Layer to extract (default: self.layer)

        Returns:
            Activation vector (mean pooled across tokens)
        """
        layer = layer if layer is not None else self.layer

        # Tokenize
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        ).to(self.device)

        # Forward pass
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Extract hidden states at target layer
        hidden_states = outputs.hidden_states[layer]  # (batch, seq_len, hidden_dim)

        # Mean pool across tokens (excluding padding)
        attention_mask = inputs['attention_mask'].unsqueeze(-1)  # (batch, seq_len, 1)
        masked_hidden = hidden_states * attention_mask
        pooled = masked_hidden.sum(dim=1) / attention_mask.sum(dim=1)  # (batch, hidden_dim)

        return pooled.cpu().numpy().squeeze()

    def _get_attention(self, text: str, layer: Optional[int] = None) -> np.ndarray:
        """
        Extract attention patterns for text at specified layer.

        Args:
            text: Input text
            layer: Layer to extract (default: self.layer)

        Returns:
            Attention matrix (averaged across heads)
        """
        layer = layer if layer is not None else self.layer

        # Tokenize
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=512
        ).to(self.device)

        # Forward pass
        with torch.no_grad():
            outputs = self.model(**inputs)

        # Extract attention at target layer
        attention = outputs.attentions[layer]  # (batch, n_heads, seq_len, seq_len)

        # Average across heads
        avg_attention = attention.mean(dim=1).squeeze()  # (seq_len, seq_len)

        return avg_attention.cpu().numpy()

    def _generate_contexts(self, concept: str, n: int) -> List[str]:
        """
        Generate diverse contexts for a concept.

        Args:
            concept: The concept to contextualize
            n: Number of contexts to generate

        Returns:
            List of context strings
        """
        # Template-based context generation
        templates = [
            f"The concept of {concept}",
            f"Understanding {concept}",
            f"When we think about {concept}",
            f"The meaning of {concept}",
            f"What is {concept}",
            f"Consider the idea of {concept}",
            f"Regarding {concept}",
            f"In relation to {concept}",
            f"The notion of {concept}",
            f"Thinking about {concept}",
            f"{concept} is important because",
            f"{concept} can be understood as",
            f"The essence of {concept}",
            f"Looking at {concept}",
            f"{concept} involves",
            f"We can describe {concept} as",
            f"The idea behind {concept}",
            f"{concept} relates to",
            f"Exploring {concept}",
            f"The nature of {concept}",
        ]

        # Cycle through templates to reach n contexts
        contexts = []
        for i in range(n):
            contexts.append(templates[i % len(templates)])

        return contexts[:n]

    # ============================================================
    # OPERATOR 1: Generativity Score
    # ============================================================

    def compute_generativity(
        self,
        concept: str,
        alpha: float = 0.4,
        beta: float = 0.3,
        gamma: float = 0.3
    ) -> Tuple[float, Dict[str, float]]:
        """
        Compute generativity score for a concept.

        Generativity = α·attention_entropy + β·representation_drift + γ·context_variance

        Args:
            concept: Concept to measure
            alpha, beta, gamma: Component weights

        Returns:
            (score, components_dict)
        """
        # 1. Attention entropy
        attn_matrix = self._get_attention(concept, self.layer)
        attn_probs = attn_matrix.mean(axis=0)  # Average attention distribution
        attn_probs = attn_probs / attn_probs.sum()  # Normalize
        attn_entropy = entropy(attn_probs)

        # Normalize to [0, 1] (max entropy = log(n))
        max_entropy = np.log(len(attn_probs))
        attn_entropy_norm = attn_entropy / max_entropy if max_entropy > 0 else 0

        # 2. Representation drift (layer L to L+1)
        if self.layer < self.n_layers - 1:
            h_L = self._get_activation(concept, self.layer)
            h_L_plus_1 = self._get_activation(concept, self.layer + 1)
            drift = cosine(h_L, h_L_plus_1)  # Cosine distance
        else:
            drift = 0.0  # Last layer, no drift

        # 3. Context variance
        contexts = self._generate_contexts(concept, self.n_contexts)
        activations = [self._get_activation(ctx, self.layer) for ctx in contexts]

        # Compute pairwise cosine distances
        distances = []
        base_activation = activations[0]
        for act in activations[1:]:
            distances.append(cosine(base_activation, act))

        variance = np.var(distances) if distances else 0.0

        # Combine with weights
        score = alpha * attn_entropy_norm + beta * drift + gamma * variance

        components = {
            'attention_entropy': attn_entropy_norm,
            'representation_drift': drift,
            'context_variance': variance,
            'final_score': score
        }

        return score, components

    # ============================================================
    # OPERATOR 2: Structural Alignment Score (CKA)
    # ============================================================

    def compute_cka(self, X: np.ndarray, Y: np.ndarray) -> float:
        """
        Compute Centered Kernel Alignment between two activation matrices.

        CKA(X, Y) = ||X'Y||²_F / (||X'X||_F · ||Y'Y||_F)

        Args:
            X: (n_contexts, hidden_dim) activation matrix
            Y: (n_contexts, hidden_dim) activation matrix

        Returns:
            CKA score in [0, 1]
        """
        # Center the matrices
        X_centered = X - X.mean(axis=0, keepdims=True)
        Y_centered = Y - Y.mean(axis=0, keepdims=True)

        # Compute kernel matrices
        XY = X_centered.T @ Y_centered
        XX = X_centered.T @ X_centered
        YY = Y_centered.T @ Y_centered

        # CKA formula
        numerator = np.linalg.norm(XY, 'fro') ** 2
        denominator = np.linalg.norm(XX, 'fro') * np.linalg.norm(YY, 'fro')

        if denominator == 0:
            return 0.0

        return numerator / denominator

    def compute_alignment(
        self,
        concept1: str,
        concept2: str
    ) -> Tuple[float, Dict[str, float]]:
        """
        Compute structural alignment between two concepts.

        Args:
            concept1, concept2: Concepts to compare

        Returns:
            (cka_score, components_dict)
        """
        # Generate contexts
        contexts1 = self._generate_contexts(concept1, self.n_contexts)
        contexts2 = self._generate_contexts(concept2, self.n_contexts)

        # Get activation matrices
        C1 = np.array([self._get_activation(ctx, self.layer) for ctx in contexts1])
        C2 = np.array([self._get_activation(ctx, self.layer) for ctx in contexts2])

        # Compute CKA
        cka_score = self.compute_cka(C1, C2)

        # Additional component analysis
        components = {
            'cka': cka_score,
            'mean_cosine_similarity': cosine_similarity(
                C1.mean(axis=0, keepdims=True),
                C2.mean(axis=0, keepdims=True)
            )[0, 0]
        }

        return cka_score, components

    # ============================================================
    # OPERATOR 3: Causal Validation (Simplified)
    # ============================================================

    def validate_homomorphism_simple(
        self,
        concept_A: str,
        concept_B: str,
        n_contexts: int = 10
    ) -> Tuple[float, List[float]]:
        """
        Simplified validation: test if activations are consistently similar
        across multiple contexts.

        Full causal intervention requires model-specific intervention code.
        This simplified version measures consistency of alignment across contexts.

        Args:
            concept_A, concept_B: Concepts to validate
            n_contexts: Number of context pairs to test

        Returns:
            (consistency_score, individual_similarities)
        """
        contexts_A = self._generate_contexts(concept_A, n_contexts)
        contexts_B = self._generate_contexts(concept_B, n_contexts)

        similarities = []
        for ctx_A, ctx_B in zip(contexts_A, contexts_B):
            act_A = self._get_activation(ctx_A, self.layer)
            act_B = self._get_activation(ctx_B, self.layer)

            # Cosine similarity
            sim = 1 - cosine(act_A, act_B)  # Convert distance to similarity
            similarities.append(sim)

        # Consistency = mean similarity (high = consistent mapping)
        consistency_score = np.mean(similarities)

        return consistency_score, similarities

    # ============================================================
    # VALIDATION SUITE
    # ============================================================

    def validate_on_known_analogies(
        self,
        test_cases: List[Tuple[str, str, str, str]],
        verbose: bool = True
    ) -> Dict[str, any]:
        """
        Test operators on known word analogies (Level 1 validation).

        For analogy (a, b, c, d) like (king, queen, man, woman):
        - Should find structural similarity between (a:b) and (c:d)

        Args:
            test_cases: List of (a, b, c, d) analogy tuples
            verbose: Print detailed results

        Returns:
            Validation results dict
        """
        results = []

        if verbose:
            print("\n" + "="*70)
            print("VALIDATION SUITE: Known Analogies")
            print("="*70)

        for a, b, c, d in test_cases:
            if verbose:
                print(f"\nTesting: ({a}:{b}) :: ({c}:{d})")

            # Compute alignments
            cka_ab, _ = self.compute_alignment(a, b)
            cka_cd, _ = self.compute_alignment(c, d)

            # Also compute cross-pair alignments (should be lower)
            cka_ac, _ = self.compute_alignment(a, c)
            cka_bd, _ = self.compute_alignment(b, d)

            # Success if within-pair alignments > cross-pair alignments
            within_pair_avg = (cka_ab + cka_cd) / 2
            cross_pair_avg = (cka_ac + cka_bd) / 2

            success = within_pair_avg > cross_pair_avg

            result = {
                'analogy': f"({a}:{b}) :: ({c}:{d})",
                'cka_ab': cka_ab,
                'cka_cd': cka_cd,
                'cka_ac': cka_ac,
                'cka_bd': cka_bd,
                'within_pair_avg': within_pair_avg,
                'cross_pair_avg': cross_pair_avg,
                'success': success
            }
            results.append(result)

            if verbose:
                print(f"  CKA({a}:{b}) = {cka_ab:.3f}")
                print(f"  CKA({c}:{d}) = {cka_cd:.3f}")
                print(f"  Cross-pair avg = {cross_pair_avg:.3f}")
                print(f"  ✓ PASS" if success else "  ✗ FAIL")

        # Compute overall statistics
        success_rate = sum(r['success'] for r in results) / len(results)

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
                print(f"❌ VALIDATION FAILED (< 80% threshold)")

        return summary


def run_validation():
    """
    Run complete validation suite on known analogies.
    """
    # Initialize operators
    ops = ConceptualCalculusOperators(
        model_name="gpt2",  # Start with GPT-2 (fast, public)
        n_contexts=10,      # Use fewer contexts for speed
        device="cpu"
    )

    # Known analogies from word2vec research
    test_cases = [
        ("king", "queen", "man", "woman"),           # Gender
        ("Paris", "France", "London", "England"),    # Capital-country
        ("dog", "puppy", "cat", "kitten"),           # Adult-young
        ("big", "bigger", "small", "smaller"),       # Comparative
        ("good", "better", "bad", "worse"),          # Irregular comparative
    ]

    # Run validation
    results = ops.validate_on_known_analogies(test_cases, verbose=True)

    return results, ops


if __name__ == "__main__":
    print("\n🔬 Conceptual Calculus Operators - Validation Suite\n")
    results, ops = run_validation()
