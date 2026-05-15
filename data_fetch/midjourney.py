# Midjourney Discord Automation Example

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time
import os

# change class name here
class_name = "human"

# create folder automatically
save_folder = f"data/midjourney/{class_name}"
os.makedirs(save_folder, exist_ok=True)

# prompts
prompts = [
    f"realistic {class_name}"
]

# open chrome
driver = webdriver.Chrome()

# open your Midjourney Discord channel
driver.get("https://discord.com/channels/YOUR_SERVER/YOUR_CHANNEL")

print("Login manually...")
time.sleep(40)

for i in range(100):

    prompt = prompts[i % len(prompts)]

    # find Discord message box
    message_box = driver.find_element(By.TAG_NAME, "textarea")

    # send imagine prompt
    message_box.send_keys(f"/imagine {prompt}")
    message_box.send_keys(Keys.ENTER)

    print(f"Prompt Sent: {prompt}")

    # wait for generation
    time.sleep(60)

    # get latest generated image
    images = driver.find_elements(By.TAG_NAME, "img")

    if len(images) > 0:

        image_url = images[-1].get_attribute("src")

        try:
            image_data = requests.get(image_url).content

            with open(f"{save_folder}/img_{i}.png", "wb") as f:
                f.write(image_data)

            print(f"Saved: img_{i}.png")

        except:
            print("Failed to download image")

print("Done")