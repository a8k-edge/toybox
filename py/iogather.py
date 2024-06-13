import aiohttp
import asyncio
import random


async def get(id):
    delay = random.randint(0, 10)
    
    async with aiohttp.ClientSession() as session:
        await session.get(f'https://httpbin.org/delay/{delay}', timeout=4)
    
    print('done for', id)
    return id


async def main():
    futures = [get(i) for i in range(10)]

    try:
        result = await asyncio.gather(*futures, return_exceptions=True)
        print('result', result)
    except asyncio.TimeoutError as e:
        print('got error', e)
        pass
    
    await asyncio.sleep(10)


if __name__ == '__main__':
    asyncio.run(main())
