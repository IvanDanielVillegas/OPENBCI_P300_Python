import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")
    for i in range (1, 20 ):
        await say_after(i, 'hello')
        await say_after(i+1, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())