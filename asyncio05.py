import asyncio
from random import random
import time

async def cook_rice():
    start_time = time.time()
    await asyncio.sleep(1 + random())
    end_time = time.time()
    return "rice", end_time - start_time

async def cook_noodle():
    start_time = time.time()
    await asyncio.sleep(1 + random())
    end_time = time.time()
    return "noodle", end_time - start_time

async def cook_curry():
    start_time = time.time()
    await asyncio.sleep(1 + random())
    end_time = time.time()
    return "curry", end_time - start_time

async def main():
    tasks = [
        asyncio.create_task(cook_rice()),
        asyncio.create_task(cook_noodle()),
        asyncio.create_task(cook_curry())
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for task in done:
        dish, elapsed_time = task.result()
        print(f'Student A gets {dish} after {elapsed_time:.2f} seconds')

# Wait for the rest of the tasks to complete
    remaining_results = await asyncio.gather(*pending)
    for dish, elapsed_time in remaining_results:
        print(f'{dish} was completed in {elapsed_time:.2f} seconds')

# start the asyncio program
asyncio.run(main())