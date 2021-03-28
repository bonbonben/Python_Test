#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
import threading


# In[2]:


def firstThread():
    global count
    count = 0
    
    print ("This is the first thread!")
    
    while (count < 100):
        count += 1
    
    print (count)


# In[3]:


def secondThread():
    global count
    count = 0
    
    print ("This is the second thread!")
    
    while (count < 200):
        count += 1
    
    print (count)


# In[4]:


def main():
    thread1 = threading.Thread(target=firstThread, name = "Thread_1")
    thread1.start()
    thread1.join()
    print (thread1.ident)
    print (thread1.isDaemon())
    
    thread2 = threading.Thread(target=secondThread, name = "Thread_2")
    thread2.setDaemon(True)
    thread2.start()
    print (thread2.ident)
    print (thread2.isDaemon())
    
    print (threading.active_count())
    print (threading.enumerate())
    print (threading.current_thread())
    
    print (thread1.is_alive())
    print (thread2.is_alive())


# In[5]:


if (__name__ == "__main__"):
    main()

