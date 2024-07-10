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
    print("Eggs: Ready")
    
async def main():   # 1
    start = time()
    await make_coffee() # Run task with await
    await fry_eggs()
    print(f"Breakfast is ready in {time()-start} min")
    
    
asyncio.run(main()) # Run top-level funtion concurrently