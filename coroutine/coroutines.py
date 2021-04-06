from random import randint
import time
import asyncio


def randn():
    time.sleep(3)
    return randint(1, 10)


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f'Task {name}: Compute factorial{i} ... ')
        await asyncio.sleep(1)
        f *= i

    print(f'Task {name}: factorial({number}) = {f}')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def eternity():
    await asyncio.sleep(3600)
    print('yayuo')


async def coroutine():
    print(f'Started at {time.strftime("%X")}')

    await say_after(1, 'Ello')
    await say_after(3, 'Brooo')


async def coroutine_as_task():
    task_one = asyncio.create_task(say_after(2, 'Task_hello'))
    task_two = asyncio.create_task(say_after(2, 'Task_bro'))
    print(f'Started at {time.strftime("%X")}')

    await task_one
    await task_two

    print(f'Finished at {time.strftime("%X")}')


async def coroutine_gather():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4)
    )


async def coroutine_wait_for():
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')


if __name__ == '__main__':
    # print(f'Start time {time.strftime("%X")}', [randn() for _ in range(3)])
    #
    # asyncio.run(coroutine())

    # asyncio.run(coroutine_as_task())

    # asyncio.run(coroutine_gather())

    asyncio.run(coroutine_wait_for())