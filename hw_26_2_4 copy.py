import asyncio
import aiohttp

os.makedirs("images_aiohttp", exist_ok=True)

async def download_image(session, url, filename):
    async with session.get(url) as response:
        content = await response.read()
        with open(filename, "wb") as f:
            f.write(content)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 11):
            url = f"https://picsum.photos/200?random={i}"
            filename = f"images_aiohttp/image_{i}.jpg"
            tasks.append(download_image(session, url, filename))
        await asyncio.gather(*tasks)

asyncio.run(main())
