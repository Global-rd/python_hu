from concurrent.futures import ThreadPoolExecutor
import time

def task(name, duration):
    print(f"Task {name} starting...")
    time.sleep(duration)
    print(f"Task {name} finished..")


#create threadpool
with ThreadPoolExecutor(max_workers=3) as executor:
    #submit task to the pool
    executor.submit(task, "A", 3)
    executor.submit(task, "B", 2)
    executor.submit(task, "C", 1)
    executor.submit(task, "D", 1)
    executor.submit(task, "E", 1)
    executor.submit(task, "F", 1)
    executor.submit(task, "G", 1)




