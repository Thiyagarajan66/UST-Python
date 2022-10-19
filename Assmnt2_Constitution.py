#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[33]:


skip_words = ['0','1','2','3','4','5','6','7','8','9', ' ', '\n', ',', '.', ':', '-', '(', ')', '"', ';']

words = open('constitution.txt', 'r')
letters_count = {}
for word in words:
    for letter in word:
        if letter in skip_words:
            continue
        if letter in letters_count:
            letters_count[letter] = letters_count[letter] + 1
        else:
            letters_count[letter] = 1

print(letters_count)

print(len(letters_count.keys()))


import numpy as np
import matplotlib.pyplot as plt

letters = list(letters_count.keys())
count = list(letters_count.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(letters, count, color ='maroon',
        width = 0.4)
 
plt.xlabel("Letters")
plt.ylabel("Total Number of presence")
plt.title("Constitution Text")
plt.show()


# In[ ]:





# In[ ]:




