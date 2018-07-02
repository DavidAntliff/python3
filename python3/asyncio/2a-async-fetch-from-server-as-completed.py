#!/usr/bin/env python
# https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e

import time
import random
import asyncio
import aiohttp


URL = "https://api.github.com/events"
MAX_CLIENTS = 3


async def aiohttp_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return response


async def fetch_async(pid):
    start = time.time()
    sleepy_time = random.randint(2, 5)
    print("Fetch async process {} started, sleeping for {} seconds".format(pid, sleepy_time))
    await asyncio.sleep(sleepy_time)
    response = await aiohttp_get(URL)
    datetime = response.headers.get('Date')
    response.close()
    return "Process {}: {}, took: {:.2f} seconds".format(
        pid, datetime, time.time() - start)


async def main():
    start = time.time()
    futures = [fetch_async(i) for i in range(1, MAX_CLIENTS + 1)]
    # asyncio.as_completed returns an iterator of completed futures in the order they complete
    for i, future in enumerate(asyncio.as_completed(futures)):
        result = await future
        print("{} {}".format(">>" * (i + 1), result))
    print("Process took: {:.2f} seconds".format(time.time() - start))


asyncio.run(main())
