import asyncio
import time

async def count():
    print("Before")
    await asyncio.sleep(1)

    print("After")

async def anothercount():
    print("Another Before")
    await asyncio.sleep(1)
    print("Another After")

async def main():
    # await asyncio.gather(count(), count(), count())
    await asyncio.gather(count(), anothercount())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")