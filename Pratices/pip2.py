import asyncio
import time

async def Counter():
    total = 0
    for i in range(100):
        total += 2
    print(f"Total Counts is: {total}")
    await asyncio.sleep(1)

def main():

    await asyncio.gather(Counter(), Counter(), Counter())

asyncio.run(main())