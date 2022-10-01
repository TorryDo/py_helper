import asyncio
import time


def asleep(sec: float):
    """
    async sleep, this function shorten the code below
    asyncio.run(asyncio.sleep(sec))
    """
    asyncio.run(asyncio.sleep(sec))  # this function will suspend
    # time.sleep(sec)              # this function caused print work improperly


def run_async(job):
    """
    :param job: a function
    run async task simultaneously (not await)
    """
    asyncio.get_running_loop().create_task(job())
