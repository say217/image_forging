from vertexai.preview.vision_models import ImageGenerationModel
import vertexai
import os

# initialize Vertex AI
vertexai.init(
    project="YOUR_PROJECT_ID",
    location="us-central1"
)

# load Imagen model
model = ImageGenerationModel.from_pretrained("imagegeneration@006")

# change class name here
class_name = "human"

# create folder automatically
save_folder = f"data/imagen/{class_name}"
os.makedirs(save_folder, exist_ok=True)

# prompts
prompts = [
    f"realistic {class_name}"
]

# generate images
for i in range(100):

    prompt = prompts[i % len(prompts)]

    images = model.generate_images(
        prompt=prompt,
        number_of_images=1
    )

    # save image inside class folder
    images[0].save(f"{save_folder}/img_{i}.png")

    print(f"Saved: img_{i}.png")

print("Done")