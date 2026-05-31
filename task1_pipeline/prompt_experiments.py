from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)

pipe = pipe.to("cuda")

prompt = "A futuristic cyberpunk city"

image = pipe(prompt).images[0]

image.save("cyberpunk_city.png")

print("Prompt experiment completed.")