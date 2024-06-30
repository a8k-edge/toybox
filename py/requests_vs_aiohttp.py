import time
import asyncio

import requests
import aiohttp


N = 100
URL = 'https://httpbin.org/get'


def main():
    start_time = time.time()
    for _ in range(N):
        requests.get(URL)
    print("Requests took --- %s seconds ---" % (time.time() - start_time))

    asyncio.run(run_aiohttp())
    asyncio.run(run_aiohttp_cache_session())


async def run_aiohttp():
    start_time = time.time()
    for _ in range(N):
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                ...
    print("Aiohttp took --- %s seconds ---" % (time.time() - start_time))


async def run_aiohttp_cache_session():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        for _ in range(N):
            async with session.get(URL) as response:
                ...
    print("Aiohttp with cache session took --- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
