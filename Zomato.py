#!/usr/bin/env python
# coding: utf-8

# # Zomato Data Set

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv('zomato.csv', encoding='latin-1')


# In[4]:


df.head()


# In[5]:


df.columns


# In[6]:


df.info()


# In[7]:


df.describe()


# # In Data Analysis What all things do we do
# 1. Missing Values
# 2. Explore about the numberical values
# 3. Explore about the categorical values
# 4. Finding relationship between features

# In[8]:


df.isnull().sum()


# In[9]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[10]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False)


# In[11]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[12]:


df.columns


# In[13]:


final_df = pd.merge(df, df_country, on='Country Code', how='left')
final_df.head()


# In[14]:


final_df.dtypes


# In[15]:


final_df.Country.value_counts()


# In[16]:


country_names= final_df.Country.value_counts().index


# In[17]:


country_val= final_df.Country.value_counts().values


# # Pie Chart

# In[19]:


plt.pie(country_val[:3], labels = country_names[:3],autopct='%1.2f%%')


# # Observation 1:
# Zomatos maximum records or transactions are from India followed by Us and then UK

# In[20]:


final_df.columns


# In[25]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[26]:


ratings


# # Observation 2
# 1. When rating is between 4.5 to 4.9 -------> Excellent
# 2. When rating is between 4.0 to 4.4 -------> Very Good
# 3. When rating is between 3.5 to 3.9 -------> Good
# 4. When rating is between 3.0 to 3.4 -------> Average
# 5. When rating is between 2.5 to 2.9 -------> Average
# 6. When rating is between 2.0 to 2.4 -------> Poor

# In[27]:


ratings.head()


# In[28]:


import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x='Aggregate rating', y='Rating Count',data=ratings)


# In[31]:


sns.barplot(x='Aggregate rating', y='Rating Count',hue='Rating color',data=ratings, palette=['blue', 'red', 'orange', 'yellow', 'green', 'green'])


# # Observation 3
# 1. Not rated count is very high
# 2. Maximum rating are between 2.7 to 3.7

# In[32]:


sns.countplot(x='Rating color', data=ratings, palette=['blue', 'red', 'orange', 'yellow', 'green', 'green'])


# # Country Names who gave 0 rating

# In[33]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# # Observation
# Max 0 ratings are from India
