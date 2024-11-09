import time

def task1():
    print("Task 1 starting...")
    time.sleep(3)
    print("Task 1 finished...")

def task2():
    print("Task 2 starting...")
    time.sleep(3)
    print("Task 2 finished...")


#running on a single thread!!!!
print("Single threaded execution")
task1()
task2()
