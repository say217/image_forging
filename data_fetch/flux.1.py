from diffusers import FluxPipeline
import torch
import os

pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.float16
).to("cuda")

# change class name here
class_name = "african_elephant"

# create folder automatically
save_folder = f"data/flux/{class_name}"
os.makedirs(save_folder, exist_ok=True)

# prompts
prompts = [
    f"realistic {class_name}"
]

# generate images
for i in range(100):

    prompt = prompts[i % len(prompts)]

    image = pipe(prompt).images[0]

    # save image inside class folder
    image.save(f"{save_folder}/img_{i}.png")

    print(f"Saved: img_{i}.png")

print("Done")