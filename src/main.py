import asyncio
import time

from src.async_utils import asleep, run_async
from src.def2async import to_async


@to_async
def test_async():
    asleep(2.3)
    print('hello after 2 secs')


async def rr():
    for i in range(5):
        run_async(test_async)


async def test2():
    print('Hello ...')
    await asyncio.sleep(2)
    print('... World!')


if __name__ == '__main__':
    # asyncio.run(rr())
    asyncio.run(test2())
