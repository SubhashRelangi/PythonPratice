# import time

# def task():
#     time.sleep(2)
#     print("Done")

# task()
# task()

# import asyncio

# async def task():
#     await asyncio.sleep(2)
#     print("Done")

# async def main():
#     await asyncio.gather(task(), task())

# asyncio.run(main())

import asyncio

async def download(n):
    print(f"Task {n} starting...")
    await asyncio.sleep(2)
    print(f"Task {n} done!")

async def main():
    await asyncio.gather(
        download(1),
        download(2),
        download(3)
    )

asyncio.run(main())
