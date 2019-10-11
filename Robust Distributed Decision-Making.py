#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy as np
from random import choice
import pandas as pd

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

def result(i,Belief_Array):
    print ("Update", i,"times:", Belief_Array)
    ans=count(Belief_Array)
    print("Result:",ans)
    converge=0
    if ans[0] == 9:
        converge=1
    elif ans[2] == 9:
        converge=2
    else:
        converge=0
    return converge

for t in range(1,11):
    G = nx.Graph()
    G.add_nodes_from(['worker1','worker2','worker3','worker4','worker5','worker6','worker7','worker8','worker9'])
    G.add_edge('worker7', 'worker1')
    G.add_edge('worker7', 'worker2')
    G.add_edge('worker7', 'worker3')
    G.add_edge('worker7', 'worker8')
    G.add_edge('worker7', 'worker9')
    G.add_edge('worker8', 'worker4')
    G.add_edge('worker8', 'worker5')
    G.add_edge('worker8', 'worker9')
    G.add_edge('worker9', 'worker6')

    Martix = np.array([[0, 0, 0.5], [0, 0.5, 1], [0.5, 1, 1]])
    
    Belief_Array = []
    for work in range(1,10):
        Belief_Array.append((random.randrange(0,3,1)) / 2)

    array = [1,2,3,4,5,6,7,8,9]

    # positions for all nodes
    pos = nx.spring_layout(G)

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=400)

    # edges
    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, alpha=0.5, edge_color='k', style='solid')

    # labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

    #plt.figure(figsize=(3,3))
    plt.axis('off')
    plt.show()

    print ("No.", t,"experiment:")
    print("Original Belief_Array:",Belief_Array)
    for i in range(1,1000):
        x=random.choice(array)
        if x==1:
            a= Martix[int(2*Belief_Array[0]),int(2*Belief_Array[6])]
            Belief_Array[0]=a
            Belief_Array[6]=a
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
            
        elif x==2:
            b= Martix[int(2*Belief_Array[1]),int(2*Belief_Array[6])]
            Belief_Array[1]=b
            Belief_Array[6]=b
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
        elif x==3:
            c= Martix[int(2*Belief_Array[2]),int(2*Belief_Array[6])]
            Belief_Array[2]=c
            Belief_Array[6]=c
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
        elif x==4:
            d= Martix[int(2*Belief_Array[3]),int(2*Belief_Array[7])]
            Belief_Array[3]=d
            Belief_Array[7]=d
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
        elif x==5:
            e= Martix[int(2*Belief_Array[4]),int(2*Belief_Array[7])]
            Belief_Array[4]=e
            Belief_Array[7]=e
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
        elif x==6:
            f= Martix[int(2*Belief_Array[5]),int(2*Belief_Array[8])]
            Belief_Array[5]=f
            Belief_Array[8]=f
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
        elif x==7:
            g= Martix[int(2*Belief_Array[6]),int(2*Belief_Array[7])]
            Belief_Array[6]=g
            Belief_Array[7]=g
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
        elif x==8:
            h= Martix[int(2*Belief_Array[7]),int(2*Belief_Array[8])]
            Belief_Array[7]=h
            Belief_Array[8]=h
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass
        else:
            j= Martix[int(2*Belief_Array[6]),int(2*Belief_Array[8])]
            Belief_Array[6]=j
            Belief_Array[8]=j
            converge=result(i,Belief_Array)
            if converge == 1:
                print("Converge at 0\n")
                break
            elif converge == 2:
                print("Converge at 1\n")
                break
            else:
                pass

