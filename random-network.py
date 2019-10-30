#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as ne
import matplotlib.pyplot as mp
import random
import numpy as np
from random import choice
import pandas as pd
#erdos renyi graphy

def result(i,Belief_Array):
    print ("Update",i,"times:", Belief_Array)
    ans=count(Belief_Array)
    print("Result:",ans)
    converge=0
    if ans[0] == x:
        converge=1
    elif ans[2] == x:
        converge=2
    else:
        converge=0
    return converge

def count(Belief_Array):
    count1=0
    count2=0
    count3=0
    for i in range(0,len(Belief_Array)):
        if Belief_Array[i] == 0:
            count1+=1
        if Belief_Array[i] == 0.5:
            count2+=1
        if Belief_Array[i] == 1:
            count3+=1
    return count1,count2,count3

for t in range(1,11):                   # number of experiments is 10
    print ("No.", t,"experiment:")
    x = random.randrange(3,10,1)        # number of agents is 3~10
    y = random.randrange(5,8,1)/10      # line possibility to connect other agents is 0.5~0.8
    z = random.randrange(0,11,1)/10     # endidece possibility is 0~1
    print ('number of agents:', x)
    print ('line possibility to connect other agents:', y)
    print ('endidece possibility:', z)
    rg = ne.erdos_renyi_graph(x,y)      # use possibility to random connect
    ps = ne.shell_layout(rg)
    ne.draw(rg,ps,with_labels=False,node_size=100)
    mp.show()
    p = []
    temp = 0

    for i in range(0,x):
        print ('degree of node', i,'is', rg.degree(i))
        adjacent = []
        for j in rg.neighbors(i):
            adjacent.append(j)
        print ('adjacent nodes of node', i,'is', adjacent)
        p.append(adjacent)
        temp += rg.degree(i)

    edge = int(temp/2)
    print ('\nnumber of edges:', edge, '\n')

    Martix = np.array([[0, 0, 0.5], [0, 0.5, 1], [0.5, 1, 1]])

    Belief_Array = []
    for work in range(0,x):
        Belief_Array.append((random.randrange(0,3,1)) / 2)

    print("Original Belief_Array:",Belief_Array)

    for r in range(1,1000):
        A = random.randrange(0,len(p),1)
        B = random.choice(p[A])
        a = Martix[int(2*Belief_Array[A]),int(2*Belief_Array[B])]
        Belief_Array[A]=a
        Belief_Array[B]=a
        converge=result(r,Belief_Array)
        if converge == 1:
            print("Converge at 0\n")
            break
        elif converge == 2:
            print("Converge at 1\n")
            break
        else:
            pass

