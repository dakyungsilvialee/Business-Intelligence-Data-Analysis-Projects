#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
from nba_api.stats import endpoints
import statsmodels.formula.api as smf
import statsmodels.formula.api as sm
from statsmodels.graphics.regressionplots import plot_partregress_grid


# In[3]:


data = endpoints.leagueleaders.LeagueLeaders()
df = data.league_leaders.get_data_frame()


# In[4]:


df.head()


# In[5]:


# explore the columns in the dataframe
df.columns


# In[4]:


# create a dataframe including player information and other relevant metrics
df1 = df[["PLAYER_ID", "RANK", "PLAYER", "TEAM", "PTS", "GP", "FGM", "FTM", "DREB", "STL", "BLK", "AST_TOV"]]
df1.head()


# In[5]:


# create a new column that calculates the average points per game played
df1['PTSperGP'] = df1['PTS'] / df1['GP']
df1.head()


# In[6]:


# create a new dataframe with the columns of interest
# included average points per game played, field goals made, free throws made, defensive rebounds, steals, blocks, and assist to turnover ratio
df2 = df1[['PTSperGP', "FGM", "FTM", "DREB", "STL", "BLK", "AST_TOV"]]


# In[9]:


# explore correlations between the variables; FGM and FTM have the highest positive correlations with average points per games played
# assist to turnover ratio has the lowest positive correlation with average points per games played
df2.corr()


# In[7]:


# create a correlation heatmap to visualize the correlations between the variables by color
px.imshow(df2.corr())


# In[8]:


# another format of the correlation heatmap
sns.set(font_scale=1.15)
plt.figure(figsize=(8,4))
sns.heatmap(df2.corr(), cmap='RdBu_r', annot=True, vmin=-1, vmax=1)


# In[11]:


# develop a regression model adding all of these variables together
model = smf.ols('PTSperGP ~ FGM + FTM + DREB + STL + BLK + AST_TOV', data = df2)
results = model.fit()
results.summary() 
# high r squared indicates that the model explains about 90% of the variation in the data


# In[12]:


# create a plot of the residuals in a histogram; it appears right skewed
pred_val = results.fittedvalues.copy()
residual = df2['PTSperGP'] - pred_val
fig = sns.histplot(residual)


# In[14]:


# plot of partial residuals (only considering FGM)
fig = sns.lmplot(x= 'FGM', y = "PTSperGP", data = df2, height = 5, aspect = 2)

