import os
import requests


def download_images(topic):

    folder = "images"

    if not os.path.exists(folder):
        os.makedirs(folder)

    image_urls = [
        "https://picsum.photos/800/400",
        "https://picsum.photos/801/400",
        "https://picsum.photos/802/400"
    ]

    image_paths = []

    for i, url in enumerate(image_urls):

        response = requests.get(url)

        filename = f"{folder}/image_{i+1}.jpg"

        with open(filename, "wb") as f:
            f.write(response.content)

        image_paths.append(filename)

    return image_paths