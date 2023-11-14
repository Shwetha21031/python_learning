# eg-  while downloading 
import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(sec):
    print('sleeping for ',sec,'s')
    time.sleep(sec)
    print('done',sec,'s')
    return sec

# time1 = time.perf_counter()
# normally
# func(4)
# func(2)
# func(1)
# time2 = time.perf_counter()
# print(time2-time1,"normally")


# with threading
# time3 = time.perf_counter()

# t1 = threading.Thread(target=func,args=[4])
# t2 = threading.Thread(target=func,args=[2])
# t3 = threading.Thread(target=func,args=[1])
# # all three will start at once
# t1.start()
# t3.start()
# t2.start()

# time4 = time.perf_counter()

# print(time4-time3,"threading")
# # less coz py wont wait till the code is done executing it just starts and throws the func to the side to continue

# t1.join()
# t2.join()
# t3.join()

# time5  = time.perf_counter()
# print(time5-time3)
# wait till they get finished

def pooling():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func,3)
        # future2 = executor.submit(func,2)
        # future3 = executor.submit(func,4)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [3,4,6,5]
        results = executor.map(func,l)
        for result in results:
            print(result)

pooling()