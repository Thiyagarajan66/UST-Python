#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
data = pd.read_csv("faa_ai_prelim.csv")

# view the content
print(data)


# In[8]:



# data shape
shape = data.shape
  
print(shape)


# In[10]:


columns = data.columns
print(columns)


# In[13]:


print(data["ACFT_MAKE_NAME"], data['LOC_STATE_NAME'], data['ACFT_MODEL_NAME'], data["RMK_TEXT"], data['FLT_PHASE'],
     data['EVENT_TYPE_DESC'], data['FATAL_FLAG'])


# In[15]:


print(data.isna().sum())


# In[21]:


data["FATAL_FLAG"].fillna('No',inplace=True)
print(data["FATAL_FLAG"])


# In[23]:


data.dropna(subset = ['ACFT_MAKE_NAME'], inplace=True)
print(data)


# In[ ]:




