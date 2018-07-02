#!/usr/bin/env python
# https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e

import asyncio


async def foo():
    print("Running in foo")
    await asyncio.sleep(0)
    print("Explicit context switch to foo again")


async def bar():
    print("Explicit context to bar")
    await asyncio.sleep(0)
    print("Implicit context switch back to bar")


async def main():
    print("Collect tasks")
    tasks = [foo(), bar()]
    print("Gathering")
    await asyncio.gather(*tasks)


asyncio.run(main())
