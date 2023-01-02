#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
get_ipython().system('pip install cerberus')
import re


# In[36]:


df = pd.read_csv('/Users/fors/Downloads/cleaned_full_travel_data_after_sort.csv', header = None)


# In[37]:


df.head(10)


# In[38]:


df.tail()


# In[48]:


df1 = df.iloc[:,3:7]


# In[49]:


df1.head()


# In[53]:


df1.columns = ['City', 'Transplantation Type', 'Duration(min)', 'Price' ]


# In[54]:


df1.info()


# In[55]:


df1.head()


# In[56]:


df1.tail()


# In[57]:


df1.describe()


# In[40]:


from cerberus import Validator


# In[74]:


schema = {
    'City' : {'type': 'integer', 'min': 8, 'max': 797},
    'Transplantion Type' : {'type': 'integer', 'min':1, 'max':10},
    'Price' : {'type': 'float'},
    'Duration(min)': {'type': 'integer', 'min': 5, 'max': 15240}
    
    
    
    
}


# In[75]:


v = Validator(schema)
v.allow_unknown = True
v.require_all = True


# In[88]:


df_dict =df1.to_dict(orient = 'dict')


# In[89]:


if v.validate(df_dict):
    print('data is valid')
else:
    print('invalid data')

