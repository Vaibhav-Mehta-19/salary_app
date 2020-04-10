#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


# In[8]:


dataset = pd.read_csv("Salary_Data.csv")
print(dataset.head())
print(dataset.shape)


# In[6]:


from sklearn.externals import joblib


# In[9]:


x= dataset["YearsExperience"]
y= dataset["Salary"]
X= x.values.reshape(30,1)


# In[10]:


model = LinearRegression()
model.fit(X,y)


# In[12]:


joblib.dump(model,"mymodel")


# In[15]:


model.predict([[2.3]])


# In[ ]:




