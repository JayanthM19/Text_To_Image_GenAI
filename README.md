# Stable Diffusion ElevanceSkills Project

## Overview
This repository contains my Generative AI  project focused on text-to-image generation using Stable Diffusion and related generative AI techniques.

The project will progressively include:
- Text-to-image pipeline implementation
- Attention mechanism analysis
- Text embeddings using HuggingFace Transformers
- Fine-tuning pretrained diffusion models
- Dataset analysis and visualization
- Conditional GAN experiments

## Project Structure

- notebooks/ → Jupyter notebooks and experiments
- task1_pipeline/ → Baseline text-to-image pipeline
- task2_attention/ → Attention mechanism experiments
- task3_finetuning/ → LoRA and fine-tuning
- task4_dataset_analysis/ → Dataset exploration and visualizations
- task5_embeddings/ → CLIP embeddings and tokenizer experiments
- task6_cgan/ → Conditional GAN experiments
- reports/ → Daily internship reports
- outputs/ → Generated images and outputs

## Tech Stack
- Python
- PyTorch
- HuggingFace Diffusers
- Stable Diffusion
- Transformers

## Current Progress
Day 1: Environment setup and repository initialization completed.

## Stable Diffusion Pipeline

The Stable Diffusion pipeline converts a text prompt into an image through several stages:

1. Text tokenization
2. CLIP text embedding generation
3. Latent noise initialization
4. Iterative denoising using UNet
5. Scheduler-guided diffusion process
6. VAE decoding to generate final image

### Core Components
- Tokenizer
- CLIP Text Encoder
- UNet
- Scheduler
- Variational Autoencoder (VAE)

## Day 3 - Prompt Engineering and Inference Experiments

The project now includes experiments focused on understanding how Stable Diffusion responds to:
- Prompt wording
- Negative prompts
- Guidance scale
- Inference steps
- Scheduler selection

These experiments help analyze image quality, semantic alignment, creativity, and generation stability.

## Day 4 - Attention Mechanism Analysis

The project now includes experiments and documentation related to attention mechanisms in Stable Diffusion.

Topics explored:
- Self-attention
- Cross-attention
- Prompt-to-image semantic alignment
- Token interactions
- Attention-guided image generation

## Day 5 - Diffusion Scheduler Analysis

The project now includes experiments focused on diffusion schedulers and denoising behavior.

Topics explored:
- Diffusion timesteps
- Scheduler comparisons
- Euler scheduler
- DDIM scheduler
- DPM Solver
- Quality vs speed tradeoffs

## Day 6 - Dataset Analysis and Visualization

The project now includes dataset exploration and preprocessing experiments using image-caption datasets.

Topics explored:
- Dataset structure
- Image visualization
- Class distribution
- Caption analysis
- Data preprocessing

## Day 7 - Dataset Preprocessing Pipeline

The project now includes preprocessing workflows for preparing image-caption datasets for Stable Diffusion training.

Topics explored:
- Image resizing
- Normalization
- Tensor conversion
- Caption tokenization
- Training pipeline preparation