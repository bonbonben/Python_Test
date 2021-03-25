#!/usr/bin/env python
# coding: utf-8

# In[1]:


import threading
import time
import random

class CustThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        
        self.name = name
        
    def run(self):
        
        getTime(self.name)
        
        print("Thread", self.name, "Execution Ends")


# In[2]:


def getTime(name):
    print("Thread {} sleeps at {}".format(name, time.strftime("%H:%M:%S", time.gmtime())))
    
    randSleepTime = random.randint(1, 5)
    
    time.sleep(randSleepTime)


# In[3]:


# Create thread objects
thread1 = CustThread("1")
thread2 = CustThread("2")

# Start thread execution of run()
thread1.start()
thread2.start()

# Check if thread is alive
print("Thread 1 Alive :", thread1.is_alive())
print("Thread 2 Alive :", thread2.is_alive())

# Get thread name
# You can change it with setName()
print("Thread 1 Name :", thread1.getName())
print("Thread 2 Name :", thread2.getName())

# Wait for threads to exit
thread1.join()
thread2.join()

print("Execution Ends")

