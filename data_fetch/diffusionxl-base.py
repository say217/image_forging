from diffusers import StableDiffusionXLPipeline
import torch
import os

# load SDXL model
pipe = StableDiffusionXLPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16
).to("cuda")

# change class name here
class_name = "african_elephant"

# create folder automatically
save_folder = f"data/sdxl/{class_name}"
os.makedirs(save_folder, exist_ok=True)

# prompts
prompts = [
    f"realistic {class_name}"
]

# generate images
for i in range(10):

    prompt = prompts[i % len(prompts)]

    image = pipe(prompt).images[0]

    # save image inside class folder
    image.save(f"{save_folder}/img_{i}.png")

    print(f"Saved: img_{i}.png")

print("Done")