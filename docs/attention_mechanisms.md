# Attention Mechanisms in Stable Diffusion

## Self-Attention
Self-attention allows tokens to interact with each other and understand contextual relationships.

Example:
In the phrase "a red car", the word "car" attends to the word "red".

---

## Cross-Attention
Cross-attention connects text embeddings with image latent representations.

This mechanism enables Stable Diffusion to generate images aligned with prompt semantics.

---

## Why Attention Matters
Attention enables:
- Prompt understanding
- Semantic consistency
- Object relationships
- Spatial alignment
- Fine-grained image control

---

## Stable Diffusion Usage
Stable Diffusion uses Transformer-based cross-attention layers inside the UNet architecture.