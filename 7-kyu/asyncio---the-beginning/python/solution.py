import asyncio

async def dreaming(n, m):
    await asyncio.sleep(n)
    return m ** n
