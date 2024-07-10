import asyncio
from time import sleep, time

async def make_coffee():    # 1
    print("Coffee: prepare ingridients")
    sleep(1)
    print ("Coffee waiting...")
    await asyncio.sleep(5)  # 2: Pause another tasks can be run
    print("Coffee: Ready")
    
async def fry_eggs():   #1
    print("Eggs: Prepare ingridients")
    sleep(1)
    print("Eggs: Frying...")
    await asyncio.sleep(3)  # 2: Pause another tasks can be run
    
async def main():
    start = time()
    coffee_task = asyncio.create_task(make_coffee())    #Schedule execution
    egg_task = asyncio.create_task(fry_eggs())  # Schedule execution
    await coffee_task # Run task with await
    await egg_task
    print(f"Breakfast is ready in {time()-start} min")
    
    
asyncio.run(main()) # Run top-level funtion concurrently