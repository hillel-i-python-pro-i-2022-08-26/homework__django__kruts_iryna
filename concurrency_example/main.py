import asyncio
import random
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import logging
import concurrent.futures

from requests_example.init_logging import init_logging


def make_action(number):
    wait_time = random.randint(1, 5)
    message = f"wait {wait_time} seconds for {number}"
    logging.info(f"[start] {message}")
    time.sleep(wait_time)
    logging.info(f"[end] {message}")
    return

async def make_action_async(number: int):
    wait_time = random.randint(1, 5)
    message = f"wait {wait_time} seconds for {number}"
    logging.info(f"[start] {message}")
    await asyncio.sleep(wait_time)
    logging.info(f"[end] {message}")
    return

def make_with_classic_way(items: list[int]):
    return list(map(make_action, items))

def make_with_thread_pool_executor(items: list[int]):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(make_action, items)
    #     futures = [executor.submit(make_action, item) for item in items]
    #     results = [
    #             future.result()
    #             for future in concurrent.futures.as_completed(futures)
    #         ]
    # return results
    return list(result)

def make_with_process_pool_executor(items: list[int]):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(make_action, items)
    return list(result)


async def make_with_asyncio(items: list[int]):
    return await asyncio.gather(*[make_action_async(item) for item in items])



def main():
    items = list(range(10))
    # # make_with_classic_way(items)
    # make_with_thread_pool_executor(items)
    # make_with_process_pool_executor(items)
    asyncio.run(make_with_asyncio(items))


if __name__ == "__main__":
    init_logging()
    main()