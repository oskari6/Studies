import httpx
import asyncio

"""
async support
http2 support
connection pooling
retries
"""

client = httpx.Client(http2=True)
response = httpx.get("https://httpbin.org/bearer", headers={"Authorization": "Bearer YOUR_TOKEN"})
response = httpx.get("https://httpbin.org/basic-auth/user/pass", auth=("user", "pass"))

# download file
response = httpx.get("https://httpbin.org/image/png")
with open("downloaded_image.png", "wb") as file:
    file.write(response.content)

#upload
files = {"file": open("example.txt", "rb")}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())

response = httpx.get("https://jsonplaceholder.typicode.com/posts",)
if response.status_code == 200:
    print(response.json())

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts")
        print(response.json())