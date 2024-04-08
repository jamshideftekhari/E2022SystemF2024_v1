import asyncio
import time

async def hello():
    print("Hello, ")
    await asyncio.sleep(1)
    print("World!")

async def main():
    await asyncio.gather(hello(), hello(), hello())

def hello_world():
    print("Hello, ")
    time.sleep(1)
    print ("World!")

asyncio.run(main())
hello_world()
hello_world()
hello_world()    