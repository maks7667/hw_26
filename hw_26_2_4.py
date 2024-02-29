import os
import requests

os.makedirs("images_requests", exist_ok=True)

for i in range(1, 11):
    response = requests.get("https://picsum.photos/200")
    with open(f"images_requests/image_{i}.jpg", "wb") as f:
        f.write(response.content)
