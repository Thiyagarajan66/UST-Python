#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[10]:


dataset =pd.read_csv('FDNY.csv')


# In[11]:


display(dataset)


# In[12]:


dataset.head()


# In[13]:


dataset=pd.read_csv('FDNY.csv',skiprows=1)
dataset


# In[14]:


dataset.head(5)


# In[15]:


dataset.describe()


# In[16]:


dataset.columns


# In[17]:


dataset.dtypes


# In[18]:


dataset.index


# In[ ]:




