import aiohttp
import os
import json
import asyncio

async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()

async def save_json(index, data):
    os.makedirs("json_files", exist_ok=True)
    with open(f"json_files/file_{index}.json", "w") as file:
        json.dump(data, file)

async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://jsonplaceholder.typicode.com/posts"
        data = await fetch_json(session, url)
        tasks = [save_json(index, obj) for index, obj in enumerate(data, start=1)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
    print("Файлы сохранены.")