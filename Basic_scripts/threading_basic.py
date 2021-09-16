
#Threading
import threading

import time

def myfunction():
    print("Start a thread")
    time.sleep(3)
    print("End a thread")

threads = []

for i in range(5):
    th = threading.Thread(target=myfunction)
    th.start()
    threads.append(th)
for th in threads:
    th.join()

for i in range(5):
    myfunction()

"""
#Threading
start() #simply starts or initiates the thread

join() #makes sure the program waits for all threads to terminate

th = threading.Thread(target = myfunction) #using the Thread class form the 'threading' module and telling it the target function to be executed using the 'target' argument

"""