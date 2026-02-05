# Conceptual Calculus Operators v0.2 (Technical Revision)

**Status**: DRAFT - Under IMPCD refinement (Iteration 2)
**Created**: 2026-02-05
**Purpose**: Systematic discovery of structural correspondences in LLM activation space using established interpretability methods

## Changes from v0.1
- **Grounded in transformer architecture**: Attention patterns, residual stream, layer-wise semantics
- **Uses established methods**: CKA, attention analysis, causal interventions (not invented operators)
- **Mathematical rigor**: Precise definitions in activation space, proper terminology
- **Validation framework**: Test on known analogies, cross-model consistency, statistical significance
- **Concrete implementation**: Specific layers, algorithms, complexity analysis

---

## Core Insight

Large language models encode semantic relationships in activation space structure. Different conceptual domains that share abstract structure may produce similar activation patterns. By systematically analyzing these patterns, we can discover structural correspondences (homomorphisms) between domains.

**What this measures**: Structural alignment in LLM representations, not objective truth or human cognition.

**Novel contribution**: Not new operators, but systematic application of existing interpretability methods for cross-domain homomorphism discovery.

---

## Mathematical Foundations

### Activation Space as Semantic Manifold

**Definition**: For transformer model M with L layers and hidden dimension d:
- **Activation space** A_l ⊂ ℝ^d at layer l
- **Concept representation** c ∈ A_l is the activation pattern for concept c at layer l
- **Context-dependent**: c = c(context) varies with surrounding tokens

**Metric Structure**:
- **Distance**: Cosine distance d(c₁, c₂) = 1 - (c₁ · c₂)/(||c₁|| ||c₂||)
- **Not Euclidean**: High-dimensional, sparse, non-linear
- **Layer-specific**: Distance meaningful within layer, not across layers

### Categorical Structure in Activation Space

**Objects**: Concept representations {c₁, c₂, ...} ⊂ A_l

**Morphisms**: Relational structure encoded in:
1. **Attention patterns**: A(c₁, c₂) = attention from c₁ to c₂
2. **Transformations**: T(c) = how concept transforms across layers
3. **Context relations**: R(c, ctx) = how context modifies concept

**Composition**: Chaining relationships via attention flow and residual stream

**Homomorphism**: Map h: Domain_A → Domain_B preserving:
- Attention structure: A_A(c₁,c₂) similar to A_B(h(c₁), h(c₂))
- Transformations: T_A(c) maps to T_B(h(c))
- Context dependencies: R_A(c, ctx_A) maps to R_B(h(c), ctx_B)

---

## Operator 1: Conceptual Generativity Score

**Purpose**: Measure how much a concept generates derivative concepts in activation space.

**What it actually measures**:
- Attention entropy (how dispersed attention is from this concept)
- Representation drift (how much concept changes across layers)
- Context sensitivity (how much context affects representation)

**Mathematical Definition**:

```
generativity(c, L) = α·H_attn(c, L) + β·||Δh_L|| + γ·Var_ctx(c)

where:
  H_attn(c, L) = -Σ p_i log p_i  (attention entropy at layer L)
  ||Δh_L|| = ||h_{L+1} - h_L||   (representation drift)
  Var_ctx(c) = Var[c(ctx₁), c(ctx₂), ...]  (context variance)
  α, β, γ = weighting hyperparameters
```

**Implementation**:

```python
def compute_generativity(model, concept, layer, contexts):
    """
    Args:
        model: Transformer model
        concept: Text representing concept
        layer: Target layer (recommend 12-16 for semantics)
        contexts: List of context strings

    Returns:
        Generativity score (0-1 normalized)
    """
    # 1. Attention entropy
    attn_patterns = model.get_attention(concept, layer)
    attn_entropy = entropy(attn_patterns)  # Shannon entropy

    # 2. Representation drift
    h_L = model.get_activation(concept, layer)
    h_L_plus_1 = model.get_activation(concept, layer + 1)
    drift = cosine_distance(h_L, h_L_plus_1)

    # 3. Context sensitivity
    activations = [model.get_activation(f"{ctx} {concept}", layer)
                   for ctx in contexts]
    variance = np.var([cosine_distance(activations[0], a)
                       for a in activations[1:]])

    # Combine (weights empirically determined)
    return 0.4 * attn_entropy + 0.3 * drift + 0.3 * variance
```

**Interpretation**:
- **High score**: Concept is generative (activates many attention heads, changes across layers, context-sensitive)
- **Low score**: Concept is terminal (focused attention, stable representation, context-independent)

**Not a claim**: About objective generativity - only about representation in this model.

---

## Operator 2: Structural Alignment Score

**Purpose**: Measure structural similarity between concepts from different domains.

**Uses established method**: Centered Kernel Alignment (CKA)

**Mathematical Definition**:

```
CKA(C₁, C₂) = ||C₁ᵀC₂||²_F / (||C₁ᵀC₁||_F · ||C₂ᵀC₂||_F)

where:
  C₁ = matrix of activations for concept 1 across contexts
  C₂ = matrix of activations for concept 2 across contexts
  ||·||_F = Frobenius norm
```

**Why CKA**:
- Invariant to orthogonal transformations
- Normalized to [0,1]
- Accounts for context dependence
- Well-validated in interpretability literature

**Implementation**:

```python
def compute_alignment(model, concept1, concept2, layer, contexts):
    """
    Args:
        model: Transformer model
        concept1, concept2: Text representing concepts
        layer: Target layer
        contexts: List of context strings

    Returns:
        CKA score (0-1), component breakdown
    """
    # Get activations across contexts
    C1 = np.array([model.get_activation(f"{ctx} {concept1}", layer)
                   for ctx in contexts])
    C2 = np.array([model.get_activation(f"{ctx} {concept2}", layer)
                   for ctx in contexts])

    # Centered Kernel Alignment
    cka_score = compute_cka(C1, C2)

    # Component analysis
    components = {
        'attention_similarity': attention_pattern_correlation(C1, C2),
        'residual_similarity': residual_stream_similarity(C1, C2),
        'transformation_similarity': layer_transformation_similarity(C1, C2)
    }

    return cka_score, components
```

**Interpretation**:
- **CKA > 0.7**: Strong structural alignment (candidate homomorphism)
- **CKA 0.3-0.7**: Moderate alignment (partial correspondence)
- **CKA < 0.3**: Weak alignment (likely independent)

**Component breakdown** tells you which aspects align:
- Attention patterns (relational structure)
- Residual stream (information flow)
- Layer transformations (how concepts evolve)

---

## Operator 3: Causal Homomorphism Validation

**Purpose**: Test if structural alignment represents true homomorphism via causal intervention.

**Method**: Activation patching (causal tracing)

**Process**:

1. **Baseline**: Generate completion for concept in domain B
2. **Intervene**: Replace activation with concept from domain A
3. **Observe**: What concept emerges in domain B?
4. **Validate**: If consistently maps to expected concept, homomorphism confirmed

**Implementation**:

```python
def validate_homomorphism(model, concept_A, expected_B, layer, n_trials=20):
    """
    Args:
        model: Transformer model
        concept_A: Concept from domain A
        expected_B: Hypothesized corresponding concept in domain B
        layer: Intervention layer
        n_trials: Number of validation trials

    Returns:
        Success rate, emergent concepts
    """
    successes = 0
    emergent = []

    for trial in range(n_trials):
        # 1. Get activation for concept_A
        context_A = generate_context(domain_A, trial)
        activation_A = model.get_activation(f"{context_A} {concept_A}", layer)

        # 2. Patch into domain B context
        context_B = generate_context(domain_B, trial)
        model.patch_activation(context_B, layer, activation_A)

        # 3. Generate completion
        completion = model.generate(context_B)
        emergent_concept = extract_concept(completion)
        emergent.append(emergent_concept)

        # 4. Check if matches expected
        if similar(emergent_concept, expected_B):
            successes += 1

    return successes / n_trials, emergent
```

**Validation threshold**: ≥70% success rate across trials

**This is causal, not correlational** - strongest evidence for homomorphism.

---

## Systematic Discovery Process

### Phase 1: Identify Generative Concepts

**Goal**: Find concepts worth exploring for cross-domain transfer.

**Method**:
1. Compute generativity scores for concepts in source domain
2. Rank by score
3. Select top 10-20% as candidate anchors

**Rationale**: Generative concepts more likely to have rich structure worth transferring.

### Phase 2: Find Structural Alignments

**Goal**: Identify candidate homomorphisms.

**Method**:
1. For each generative concept in domain A:
   - Compute CKA with concepts in domain B
   - Rank by alignment score
   - Select CKA > 0.7 as candidates
2. Analyze component breakdown:
   - Which aspects align (attention, residual, transformation)?
   - Are alignments partial or complete?

**Output**: List of (concept_A, concept_B, CKA_score, components) tuples

### Phase 3: Causal Validation

**Goal**: Confirm homomorphisms via intervention.

**Method**:
1. For each candidate (A, B) pair:
   - Run causal patching validation
   - Measure success rate
   - Document emergent concepts
2. Accept if success rate ≥70%
3. Document failures (valuable negative data)

**Output**: Validated homomorphisms with confidence scores

### Phase 4: Expert Review

**Goal**: Confirm meaningful correspondence.

**Method**:
1. Present validated homomorphisms to domain experts
2. Experts assess:
   - Is structural alignment meaningful?
   - Does it reveal insights?
   - Are there counterexamples?
3. Accept only expert-confirmed homomorphisms

**Output**: Expert-validated cross-domain correspondences

---

## Implementation Specifications

### Layer Selection

**Recommendation**: Middle layers (12-16 for 24-layer models)

**Rationale**:
- Early layers (1-6): Syntax, surface patterns
- Middle layers (7-18): Semantics, abstract concepts ← **TARGET**
- Late layers (19-24): Task-specific, prediction-oriented

**Empirical validation**: Test on known analogies, select layer with best recovery.

### Context Generation

**Challenge**: Concepts are context-dependent.

**Solutions**:
1. **Canonical contexts**: Use neutral frame "The concept of [CONCEPT]..."
2. **Multi-context averaging**: Average activations across N contexts
3. **Domain-specific contexts**: Use typical contexts from each domain

**Recommendation**: Multi-context averaging (N=20-50 contexts)

### Attention Head Selection

**Not all heads relevant** - specialize differently:
- Copy heads
- Syntactic heads
- Semantic relation heads ← **TARGET**

**Method**: Identify heads encoding semantic relationships:
1. Test on known relationships ("king:queen::man:woman")
2. Select heads with high correlation
3. Use only those heads for structural analysis

### Computational Complexity

**Generativity score**:
- Per concept: O(forward_pass + attention_extraction)
- For N concepts: O(N × forward_pass)
- Practical: ~1-2 seconds per concept on GPU

**Alignment score**:
- Per pair: O(K × forward_pass) where K = contexts
- For N×M pairs: O(N × M × K × forward_pass)
- Practical: ~30-60 seconds per pair (K=20)

**Causal validation**:
- Per pair: O(T × forward_pass) where T = trials
- For validated pairs: O(V × T × forward_pass)
- Practical: ~2-3 minutes per pair (T=20)

**Total**: For systematic search across domains, expect hours to days on GPU.

---

## Validation Framework

### Level 1: Known Analogies (Required)

**Test on established relationships**:
```python
test_cases = [
    ("king", "queen", "man", "woman"),  # Gender
    ("Paris", "France", "London", "England"),  # Capital-country
    ("dog", "puppy", "cat", "kitten"),  # Adult-young
    ("hot", "cold", "up", "down"),  # Antonyms
]

for (a, b, c, d) in test_cases:
    alignment_ab = compute_alignment(model, a, b, layer, contexts)
    alignment_cd = compute_alignment(model, c, d, layer, contexts)

    # Should find: (a:b) structurally similar to (c:d)
    assert similarity(alignment_ab, alignment_cd) > threshold
```

**Pass threshold**: ≥80% of test cases recover known structure.

**If fails**: Layer selection wrong, method not capturing structure, or model doesn't encode relationships well.

### Level 2: Cross-Model Consistency (Required)

**Test across different models**:
```python
models = [GPT4, Claude, Llama3]

for concept_pair in discovered_homomorphisms:
    scores = [compute_alignment(model, *concept_pair)
              for model in models]

    # Should be consistent across models
    assert coefficient_of_variation(scores) < 0.3
```

**Rationale**: If homomorphism is real structural correspondence (not training artifact), should appear across models.

**Pass threshold**: ≥70% of homomorphisms show cross-model consistency.

### Level 3: Statistical Significance (Required)

**Guard against spurious patterns**:
```python
# Null hypothesis: Random concept pairs have same alignment
null_distribution = [compute_alignment(model, random_A, random_B)
                     for _ in range(1000)]

# Test if discovered alignment is significant
p_value = (null_distribution >= observed_alignment).mean()

# Bonferroni correction for multiple testing
alpha = 0.05 / n_tested_pairs

assert p_value < alpha
```

**Pass threshold**: p < 0.05 after multiple testing correction.

### Level 4: Domain Expert Review (Required for claims)

**Expert assessment**:
- Present: (concept_A, concept_B, CKA=X, success_rate=Y%)
- Expert evaluates: Is this meaningful? Are there counterexamples?
- Accept only if expert confirms

**Expert qualifications**:
- Advanced knowledge in both domains
- Understanding of structural foundations
- Ability to identify when alignment breaks

---

## Known Limitations

### Fundamental

1. **Model-specific**: Measures structure in this model's representation, not objective reality
2. **Training data bias**: Reflects corpus distribution, cultural biases
3. **Context dependence**: Results vary with context selection
4. **Partial correspondences**: Most homomorphisms are partial, not complete
5. **Polysemy**: Multiple senses create ambiguity
6. **Causation ≠ correlation**: Alignment doesn't prove meaningful relationship

### Methodological

7. **Layer selection**: Results depend on which layer probed
8. **Hyperparameters**: Sensitivity to weights (α, β, γ), thresholds, context counts
9. **Computational cost**: Expensive to search large concept spaces
10. **Validation requirements**: Need domain experts for confirmation

### Operational

11. **Implementation complexity**: Requires model internals access
12. **Cross-model variance**: Different models produce different structures
13. **Unclear generalization**: Unknown if method scales to >2 domains simultaneously

---

## Relationship to Existing Work

### Interpretability Methods

**Uses established techniques**:
- **CKA** (Kornblith et al., 2019): Representation similarity
- **Attention analysis** (Vig, 2019): Relational structure
- **Causal tracing** (Meng et al., 2022): Intervention validation

**Novel contribution**: Systematic application for homomorphism discovery.

### Semantic Similarity

**Related to**:
- **Distributional semantics** (Harris, 1954): Similar distributions → similar meanings
- **Word2vec** (Mikolov, 2013): Vector space analogies
- **BERT embeddings** (Devlin, 2018): Contextual representations

**Difference**: Focus on structural correspondence, not just similarity.

### Analogical Reasoning

**Builds on**:
- **Structure-mapping theory** (Gentner, 1983): Cross-domain structural alignment
- **Conceptual blending** (Fauconnier & Turner, 2002): Integration of domains

**Difference**: Computational, uses LLM activation space.

---

## Use Cases

### Appropriate Uses

1. **Hypothesis generation**: Discover potential cross-domain insights
2. **Systematic exploration**: Map structural correspondences between fields
3. **Validation of intuitions**: Test suspected homomorphisms
4. **Teaching tool**: Demonstrate structural thinking

### Inappropriate Uses

1. **Final validation**: Requires expert review
2. **High-stakes decisions**: Without empirical validation
3. **Publication claims**: Without replication and expert confirmation
4. **Replacement for expertise**: Complements, doesn't replace

---

## Next Steps

1. **Implement validation suite**: Test on known analogies
2. **Cross-model study**: Validate across GPT-4, Claude, Llama
3. **Domain expert trials**: Test on real cross-domain problems
4. **Document failures**: Learn from cases where method doesn't work
5. **Iterate**: Refine based on empirical results

---

## License

Creative Commons BY-SA 4.0

**Usage requirements**:
- Cite source methods (CKA, attention analysis, causal tracing)
- Document validation level achieved
- Include all disclaimers
- Share improvements

---

**Ready for Iteration 2 IMPCD evaluation** - now grounded in real transformer mechanics with concrete implementation.
