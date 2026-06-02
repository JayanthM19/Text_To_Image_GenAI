# Stable Diffusion Pipeline Summary

## Complete Pipeline Flow

Prompt
→ Tokenization
→ CLIP Text Embeddings
→ Cross-Attention Conditioning
→ Latent Noise Initialization
→ Scheduler-Guided Denoising
→ VAE Decoding
→ Final Image

---

## Core Components

### Tokenizer
Converts text into tokens.

### CLIP Encoder
Transforms tokens into semantic embeddings.

### UNet
Performs iterative denoising in latent space.

### Scheduler
Controls denoising timestep progression.

### VAE
Encodes and decodes latent representations.

---

## Key Learnings
- Stable Diffusion operates in latent space
- Attention mechanisms guide semantic alignment
- Prompts condition denoising behavior
- Schedulers affect image quality and efficiency