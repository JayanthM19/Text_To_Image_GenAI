# Stable Diffusion Architecture

## 1. Tokenizer
Converts input text prompts into tokens understandable by the model.

Example:
"A futuristic city"

↓

["a", "futuristic", "city"]

---

## 2. CLIP Text Encoder
Transforms tokens into high-dimensional embeddings representing semantic meaning.

---

## 3. Latent Space
Instead of generating images directly in pixel space, Stable Diffusion works in compressed latent representations.

---

## 4. UNet
The core neural network responsible for iterative denoising.

It removes noise step-by-step from latent representations.

---

## 5. Scheduler
Controls how denoising progresses across timesteps.

Examples:
- Euler
- DDIM
- DPM Solver

---

## 6. Variational Autoencoder (VAE)
Decodes latent representations back into RGB images.