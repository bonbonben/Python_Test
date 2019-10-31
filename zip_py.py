#!/usr/bin/env python
# coding: utf-8

# In[1]:


def myZip(list_1,list_2):
    deck = []
    for i in range(min(len(list_1),len(list_2))):
        while True:
            card = (list_1[i],list_2[i])
            deck.append(card)
            break
    print(deck)

myZip([1,2,3,4,5],[1,4])

