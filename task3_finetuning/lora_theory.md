# LoRA Fine-Tuning Theory

## What is LoRA?
LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique.

Instead of updating all model weights:
- original weights are frozen
- small adapter matrices are trained

---

## Why LoRA Matters
LoRA reduces:
- VRAM requirements
- training time
- storage costs

while preserving strong fine-tuning quality.

---

## Stable Diffusion + LoRA
LoRA enables:
- style adaptation
- character fine-tuning
- artistic personalization
- domain-specific image generation

without retraining the entire diffusion model.