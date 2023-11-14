import asyncio 
 
async def main():
    task = asyncio.create_task(another_func()) # this will execute in the spare time but stops as soon as main stops executing
    print('A')
    await asyncio.sleep(1)
    return_val = await task # now this will wait until the task gets finished too
    print('B')
    print(return_val)

async def another_func():
    print('1')
    await asyncio.sleep(1)
    print('2')
    return 10

asyncio.run(main())
# async def fn():
#     print('This is ')
#     await asyncio.sleep(1)
#     print('asynchronous programming')
#     await asyncio.sleep(1)
#     print('and not multi-threading')
 
# asyncio.run(fn())


 
# async def fn():
     
#     print("one")
#     await fn2()
#     print('four')
#     await asyncio.sleep(1)
#     print('five')
#     await asyncio.sleep(1)
 
# async def fn2():
#     await asyncio.sleep(1)
#     print("two")
#     await asyncio.sleep(1)
#     print("three")
#     await asyncio.sleep(1)
# asyncio.run(fn())


 
# async def func1():
#     print("Function 1 started..")
#     await asyncio.sleep(2)
#     print("Function 1 Ended")
 
 
# async def func2():
#     print("Function 2 started..")
#     await asyncio.sleep(3)
#     print("Function 2 Ended")
 
 
# async def func3():
#     print("Function 3 started..")
#     await asyncio.sleep(1)
#     print("Function 3 Ended")
 
 
# async def main():
#     L = await asyncio.gather(
#         func1(),
#         func2(),
#         func3(),
#     )
#     print("Main Ended..")
 
 
# asyncio.run(main())


# Asynchronous programming allows only one part of a program to run at a specific time.
# Consider three functions in a Python program: fn1(), fn2(), and fn3().
# In asynchronous programming, if fn1() is not actively executing (e.g., it’s asleep, waiting, or has completed its task), it won’t block the entire program.
# Instead, the program optimizes CPU time by allowing other functions (e.g., fn2()) to execute while fn1() is inactive.
# Only when fn2() finishes or sleeps, the third function, fn3(), starts executing.
# This concept of asynchronous programming ensures that one task is performed at a time, and other tasks can proceed independently.
# In contrast, in multi-threading or multi-processing, all three functions run concurrently without waiting for each other to finish.
# With asynchronous programming, specific functions are designated as asynchronous using the async keyword, and the asyncio Python library helps manage this asynchronous behavior.