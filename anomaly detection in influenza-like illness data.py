# %%
# Using IsolationForest, identify weeks when anomalies are first detected over the years using 
# the following three columns: ILITOTAL, NUM. OF PROVIDERS, and pct UNWEIGHTED for following 5 states: Georgia, Alabama, Texas, California, New York
# Consider the three columns together and separately (submit code, charts, and writeup for combined columns only)

# %%
import pandas as pd
import plotly.express as px
from sklearn.ensemble import IsolationForest

# %%
dfili = pd.read_csv('/Users/silvialee/ISOM352/ILINet_states.csv')
dfili

# %%
# Replace X with 0 

dfili = dfili.replace("X", 0)
dfili

# %%
# re-format date
dfili['date']=pd.to_datetime(dfili['YEAR'].astype(str) + dfili['WEEK'].astype(str) + '0', format='%Y%W%w')

# convert object as integer and float type
dfili["ILITOTAL"]=dfili["ILITOTAL"].astype(int)
dfili["NUM. OF PROVIDERS"]=dfili["NUM. OF PROVIDERS"].astype(int)
dfili["pctUNWEIGHTED ILI"]=dfili["pctUNWEIGHTED ILI"].astype(float)

# %%
dfili= pd.concat([dfili["REGION"], dfili["ILITOTAL"], dfili["NUM. OF PROVIDERS"], dfili["pctUNWEIGHTED ILI"], dfili['date']], axis =1)
dfili

# %%
# Filter out each df by state

filtered_df = dfili[dfili['REGION'] =='Georgia']
filtered_df

filtered_df2 = dfili[dfili['REGION'] =='Alabama']
filtered_df2

filtered_df3 = dfili[dfili['REGION'] =='Texas']
filtered_df3

filtered_df4 = dfili[dfili['REGION'] =='California']
filtered_df4

filtered_df5 = dfili[dfili['REGION'] =='New York']
filtered_df5

# %%
model = IsolationForest(random_state=42, contamination=0.05).fit(filtered_df[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])

model2 = IsolationForest(random_state=42, contamination=0.05).fit(filtered_df2[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])

model3 = IsolationForest(random_state=42, contamination=0.05).fit(filtered_df3[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])

model4 = IsolationForest(random_state=42, contamination=0.05).fit(filtered_df4[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])

model5 = IsolationForest(random_state=42, contamination=0.05).fit(filtered_df5[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])

# %%
filtered_df['scores']=model.decision_function(filtered_df[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df['anomaly']=model.predict(filtered_df[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']]


filtered_df2['scores']=model2.decision_function(filtered_df2[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df2['anomaly']=model2.predict(filtered_df2[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df2[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']]


filtered_df3['scores']=model3.decision_function(filtered_df3[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df3['anomaly']=model3.predict(filtered_df3[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df3[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']]


filtered_df4['scores']=model4.decision_function(filtered_df4[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df4['anomaly']=model4.predict(filtered_df4[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df4[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']]


filtered_df5['scores']=model5.decision_function(filtered_df5[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df5['anomaly']=model5.predict(filtered_df5[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI']])
filtered_df5[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']]

# %%
# display only anomalous data
filtered_df[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']].loc[filtered_df['anomaly']== -1]
filtered_df2[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']].loc[filtered_df2['anomaly']== -1]
filtered_df3[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']].loc[filtered_df3['anomaly']== -1]
filtered_df4[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']].loc[filtered_df4['anomaly']== -1]
filtered_df5[['ILITOTAL', 'NUM. OF PROVIDERS', 'pctUNWEIGHTED ILI', 'scores', 'anomaly']].loc[filtered_df5['anomaly']== -1]

# %%
# plot
fig = px.scatter(x=filtered_df.date, y=filtered_df['ILITOTAL'], color=filtered_df['anomaly'])
fig.show()

# %%
fig = px.scatter(x=filtered_df2.date, y=filtered_df2['ILITOTAL'], color=filtered_df2['anomaly'])
fig.show()

# %%
fig = px.scatter(x=filtered_df3.date, y=filtered_df3['ILITOTAL'], color=filtered_df3['anomaly'])
fig.show()

# %%
fig = px.scatter(x=filtered_df4.date, y=filtered_df4['ILITOTAL'], color=filtered_df4['anomaly'])
fig.show()

# %%
fig = px.scatter(x=filtered_df5.date, y=filtered_df5['ILITOTAL'], color=filtered_df5['anomaly'])
fig.show()


