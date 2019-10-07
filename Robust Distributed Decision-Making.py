#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy as np
from random import choice
import pandas as pd

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

work11 = (random.randrange(0,3,1))
work21 = (random.randrange(0,3,1))
work31 = (random.randrange(0,3,1))
work41 = (random.randrange(0,3,1))
work51 = (random.randrange(0,3,1))
work61 = (random.randrange(0,3,1))
work71 = (random.randrange(0,3,1))
work81 = (random.randrange(0,3,1))
work91 = (random.randrange(0,3,1))

work1 = work11/2
work2 = work21/2
work3 = work31/2
work4 = work41/2
work5 = work51/2
work6 = work61/2
work7 = work71/2
work8 = work81/2
work9 = work91/2

Belief_Array = [work1, work2, work3, work4, work5, work6, work7, work8, work9]

array = [1,2,3,4,5,6,7,8,9]
result = []

elarge = [(u, v) for (u, v, d) in G.edges(data=True)]

# positions for all nodes
pos = nx.spring_layout(G)

# nodes
nx.draw_networkx_nodes(G, pos, node_size=400)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6, alpha=0.5, edge_color='k', style='solid')

# labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

#plt.figure(figsize=(3,3))
plt.axis('off')
plt.show()

print("Original Belief_Array:",Belief_Array)

i = 0

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

def judge(ans):
    converge=0
    if ans[0] == 9:
        converge=1
    elif ans[2] == 9:
        converge=2
    else:
        converge=0
    return converge

while i < 100:
    x=random.choice(array)
    if x==1:
        if(i==1):
            a= Martix[work11,work71]
        else:
            a= Martix[int(2*work1),int(2*work7)]
        work1 = a
        work7 = a
        i += 1
        Belief_Array[0]=a
        Belief_Array[6]=a
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
            
    elif x==2:
        if(i==1):
            b= Martix[work21,work71]
        else:
            b= Martix[int(2*work2),int(2*work7)]
        work2 = b
        work7 = b
        i += 1
        Belief_Array[1]=b
        Belief_Array[6]=b
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
    elif x==3:
        if(i==1):
            c= Martix[work31,work71]
        else:
            c= Martix[int(2*work3),int(2*work7)]
        work3 = c
        work7 = c
        i += 1
        Belief_Array[2]=c
        Belief_Array[6]=c
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
    elif x==4:
        if(i==1):
            d= Martix[work41,work81]
        else:
            d= Martix[int(2*work4),int(2*work8)]
        work4 = d
        work8 = d
        i += 1
        Belief_Array[3]=d
        Belief_Array[7]=d
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
    elif x==5:
        if(i==1):
            e= Martix[work51,work81]
        else:
            e= Martix[int(2*work5),int(2*work8)]
        work5 = e
        work8 = e
        i += 1
        Belief_Array[4]=e
        Belief_Array[7]=e
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
    elif x==6:
        if(i==1):
            f= Martix[work61,work91]
        else:
            f= Martix[int(2*work6),int(2*work9)]
        work6 = f
        work9 = f
        i += 1
        Belief_Array[5]=f
        Belief_Array[8]=f
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
    elif x==7:
        if(i==1):
            g= Martix[work71,work81]
        else:
            g= Martix[int(2*work7),int(2*work8)]
        work7 = g
        work8 = g
        i += 1
        Belief_Array[6]=g
        Belief_Array[7]=g
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
    elif x==8:
        if(i==1):
            h= Martix[work81,work91]
        else:
            h= Martix[int(2*work8),int(2*work9)]
        work8 = h
        work9 = h
        i += 1
        Belief_Array[7]=h
        Belief_Array[8]=h
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass
    else:
        if(i==1):
            j= Martix[work71,work91]
        else:
            j= Martix[int(2*work7),int(2*work9)]
        work7 = j
        work9 = j
        i += 1
        Belief_Array[6]=j
        Belief_Array[8]=j
        print ("Update", i,"times:", Belief_Array)
        ans=count(Belief_Array)
        print("Result:",ans)
        converge=judge(ans)
        if converge == 1:
            print("Converge at 0")
            break
        elif converge == 2:
            print("Converge at 1")
            break
        else:
            pass

