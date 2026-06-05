# LoRA Training Pipeline

1. Load image-caption pairs

2. Tokenize captions

3. Encode images into latent space

4. Freeze Stable Diffusion base model

5. Attach LoRA adapters

6. Train adapter parameters

7. Save LoRA checkpoints

8. Generate fine-tuned outputs