#!/usr/bin/env python
# coding: utf-8

# In[110]:


import pandas as pd
import numpy as np
import csv
import re
import regex
import censusdata
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)
import statsmodels.formula.api as sm
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.cluster import KMeans
import plotly.express as px


# In[80]:


# import dataset from censusdata, include factors such as sex_by_age, etc. for the 2020 election results
statedata = censusdata.download('acs5', 2020, censusdata.censusgeo([('state', '*')]),
                                ['B01001_001E', 'B19013_001E', 'B19083_001E',
                                 'C17002_001E', 'B03002_001E', 'B27011_001E'])
statedata = statedata.rename(columns={'B01001_001E': 'sex_by_age', 'B19013_001E': 'median_household_income', 'B19083_001E':'gini_index', 'C17002_001E':'ratio_income_poverty', 'B03002_001E':'his_or_lat', 'B27011_001E':'health_insurance_employment'})
statedata.head()


# In[81]:


# reset index of the statedata dataframe and rename the column to be state_name
statedata = statedata.reset_index()
statedata = statedata.rename(columns={"index": "state_name"})
statedata.head()


# In[82]:


# import the election data from wikipedia
election_df = pd.read_csv("/Users/katiezhang/Downloads/ISOM 352/Python_Assignments/Assignments/election_2020_clean4.csv")
election_df.head()


# In[84]:


# split the state name from the : in the statedata df and create a new column with the cleaned state names
statedata["state_name"] = statedata["state_name"].astype(str)
statedata['new_state_name'] = statedata["state_name"].str.split(":")
statedata['new_state_name'] = statedata['new_state_name'].str[0]
statedata.head()


# In[86]:


# create a new dataframe with the relevant columns
statedata2 = statedata[["new_state_name", "sex_by_age", "median_household_income", "gini_index", "ratio_income_poverty", 'health_insurance_employment']]


# In[87]:


# rename the new_state_name column so the state_name columns match for the dataframes to merge
statedata2 = statedata2.rename(columns={"new_state_name":"state_name"})
statedata2.head()


# In[88]:


# merge dataframes based on state names
df_merged = election_df.merge(statedata2, on="state_name")
df_merged.head()


# In[91]:


# create a regression model based on all the factors we thought were important
# the dependent variable is the democratic percentage of votes
model2 = smf.ols("Biden_Harris_Democratic_perc ~ sex_by_age + ratio_income_poverty + gini_index + median_household_income + health_insurance_employment", data=df_merged).fit()
print(model2.summary())


# In[109]:


# create a scatterplot showing the distribution of states against median household income and gini_index, two of the statistically significant variables
km1 = KMeans(n_clusters=2, random_state=42).fit(df_merged[['median_household_income', 'gini_index']])
cluster1 = pd.DataFrame(km1.labels_, columns=['cluster'])
df1 = pd.concat([df_merged[['state_name', 'median_household_income','gini_index']], cluster1], axis=1)
fig1 = px.scatter(df1, 'median_household_income', 'gini_index', text='state_name', color='cluster', height=800)
fig1.show()


# In[111]:


fig = px.histogram(df1, 'median_household_income', 'gini_index', color='cluster')
fig.show()


# In[ ]:




