# %%
import yfinance as yf
import pandas as pd 
import numpy as np
import pandas_datareader
import datetime
import pandas_datareader.data as web
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split
pd.options.display.float_format = '{:,.2f}'.format

# %%
start = datetime.datetime(2021,1,1)
end = datetime.datetime(2022,1,1)

# %%
coke = web.DataReader('KO','yahoo',start,end)
coke.head()

# %%
coke['percent_change'] = (coke['Close']-coke['Open']) / coke['Open'] 
coke

# %%
pepsi = web.DataReader('PEP','yahoo',start,end)
pepsi.head()

# %%
pepsi['percent_change'] = (pepsi['Close']-pepsi['Open']) / pepsi['Open'] 
pepsi

# %%
coke2 = web.DataReader('COKE','yahoo',start,end)
coke2.head()

# %%
coke2['percent_change'] = (coke2['Close']-coke2['Open']) / coke2['Open'] 
coke2

# %%
monster = web.DataReader('MNST','yahoo',start,end)
monster.head()

# %%
monster['percent_change'] = (monster['Close']-monster['Open']) / monster['Open'] 
monster

# %%
keurig = web.DataReader('KDP','yahoo',start,end)
keurig.head()

# %%
keurig['percent_change'] = (keurig['Close']-keurig['Open']) / keurig['Open'] 
keurig

# %%
celsius = web.DataReader('CELH','yahoo',start,end)
celsius.head()

# %%
celsius['percent_change'] = (celsius['Close']-celsius['Open']) / celsius['Open'] 
celsius

# %%
result = pd.concat([pepsi, coke2, monster, keurig, celsius], axis=1).reindex(pepsi.index)["Open"]

# %%
result

# %%
coke[coke["percent_change"] >= 0] = 1
coke[coke["percent_change"] < 0] = 0
coke

# %%
data_train, data_test, label_train, label_test = train_test_split(result,coke['percent_change'],test_size=0.2)

# %%
label_train = label_train.to_numpy()
label_test = label_test.to_numpy()

# %%
mlp = MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=500)
mlp.fit(data_train,label_train)
label_predict = mlp.predict(data_test)
print(metrics.accuracy_score(label_test, label_predict))
print(metrics.confusion_matrix(label_test, label_predict))

# %%
avg_score = []
for i in range(0,100):
    mlp = MLPClassifier(hidden_layer_sizes=(10,10,10),max_iter=500)
    mlp.fit(data_train,label_train)
    label_predict = mlp.predict(data_test)
    score = metrics.accuracy_score(label_test, label_predict)
    avg_score.append(score)

print(avg_score)
print(np.mean(avg_score))

# %%



