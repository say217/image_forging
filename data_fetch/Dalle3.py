from openai import OpenAI
import requests
import os

client = OpenAI(api_key="YOUR_API_KEY")

# change class name here
class_name = "human"

# create folder automatically
save_folder = f"data/dalle3/{class_name}"
os.makedirs(save_folder, exist_ok=True)

# prompts
prompts = [
    f"realistic {class_name}"
]

# generate images
for i in range(100):

    prompt = prompts[i % len(prompts)]

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_url = response.data[0].url

    image_data = requests.get(image_url).content

    # save inside class folder
    with open(f"{save_folder}/img_{i}.png", "wb") as f:
        f.write(image_data)

    print(f"Saved: img_{i}.png")

print("Done")