# %%
import mysql.connector
import pymysql 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sqlalchemy import create_engine 

# Load Citibike data in mySQL
conn = mysql.connector.connect(
    host="isom352.cqxikovybdnm.us-east-2.rds.amazonaws.com",
    database="citibike",
    user="admin",
    password="ISOM352db")
cursor = conn.cursor()

# %%
cursor.execute('select * from tripdata201306 limit 10;')
df = pd.DataFrame(cursor.fetchall())

df.columns = cursor.column_names
df.columns

# %%
df

# %%
# Using Python, query the data to get the average trip duration and number of trips for following customer segments by gender, age, day of the week, gender and age, gender and day of the week


query = "SELECT gender, AVG(tripduration) AS Avg_tripduration, COUNT(bikeid) AS Num_of_trips "\
        "FROM tripdata201306 "\
        "GROUP BY gender;"
cursor.execute(query)
df = pd.DataFrame(cursor.fetchall())
df.columns = ['gender', 'Avg_tripduration', 'Num_of_trips']
df

# %%
query2 = "SELECT birth_year AS Age, AVG(tripduration) AS Avg_tripduration, COUNT(bikeid) AS Num_of_trips "\
        "FROM tripdata201306 "\
        "GROUP BY birth_year;"
cursor.execute(query2)
df2 = pd.DataFrame(cursor.fetchall())
df2.columns = ['Age', 'Avg_tripduration', 'Num_of_trips']
df2

# %%
query3 = "SELECT WEEKDAY(starttime) AS Day_of_the_week, AVG(tripduration) AS Avg_tripduration, COUNT(bikeid) AS Num_of_trips "\
        "FROM tripdata201306 "\
        "GROUP BY starttime;"
cursor.execute(query3)
df3 = pd.DataFrame(cursor.fetchall())
df3.columns = ['Day_of_the_week', 'Avg_tripduration', 'Num_of_trips']
df3

# %%
query4 = "SELECT gender, birth_year AS Age, AVG(tripduration) AS Avg_tripduration, COUNT(bikeid) AS Num_of_trips "\
        "FROM tripdata201306 "\
        "GROUP BY gender, birth_year;"
cursor.execute(query4)
df4 = pd.DataFrame(cursor.fetchall())
df4.columns = ['gender', 'Age', 'Avg_tripduration', 'Num_of_trips']
df4

# %%
query5 = "SELECT gender, WEEKDAY(starttime) AS Day_of_the_week, AVG(tripduration) AS Avg_tripduration, COUNT(bikeid) AS Num_of_trips "\
        "FROM tripdata201306 "\
        "GROUP BY gender, starttime;"
cursor.execute(query5)
df5 = pd.DataFrame(cursor.fetchall())
df5.columns = ['gender', 'Day_of_the_week', 'Avg_tripduration', 'Num_of_trips']
df5

# %%
# Plot the above data on a chart using seaborn library
# Use scatterplots for single variable segment (gender, age) -> gender vs num of trips, gender vs avg trip duration, age vs num of trips, age vs avg trip duration 

fig = sns.scatterplot(data=df, x="gender", y="Num_of_trips")

# %%
fig2 = sns.scatterplot(data=df, x="gender", y="Avg_tripduration")
fig2

# %%
fig3 = sns.scatterplot(data=df2, x="Age", y="Num_of_trips")
fig3

# %%
fig4 = sns.scatterplot(data=df2, x="Age", y="Avg_tripduration")
fig4

# %%
# Use scatterplots with bubble size representing the avg trip duration and number of trips for muti-variable segments (gender-age)
# Gender on y-axis, age on x-axis, and avg trip duration as bubble size. You want to know what customer types are renting more and renting bikes for longer.

# it means two graphs - one with avg trip duration as bubble and second with number of trips as bubble.
fig5 = sns.scatterplot(data=df4, x="Age", y="gender", size="Num_of_trips", hue="gender",legend=False)
fig5.set_xlim(0,30)
fig5.set_ylim(0,5)
fig5

# %%
# first, change 'Avg_tripduration' data type to integer
df4["Avg_tripduration"]=df4["Avg_tripduration"].astype(int)

sns.scatterplot(data=df4, x="Age", y="gender", size="Avg_tripduration", hue='gender', sizes=(20, 2000), legend=False)

# %%
# Identify and plot the average trip duration for the top 10: Starting stations, Ending stations, Bikes (id) -> bar chart
query6 = "SELECT start_station_name, end_station_name, AVG(tripduration) AS Avg_tripduration, COUNT(bikeid) AS Num_of_trips "\
        "FROM tripdata201306 "\
        "GROUP BY start_station_name, end_station_name, bikeid "\
        "ORDER BY Avg_tripduration DESC "\
        "LIMIT 10;"
cursor.execute(query5)
df6 = pd.DataFrame(cursor.fetchall())
df6.columns = ['start_station_name', 'end_station_name', 'Avg_tripduration', 'Num_of_trips']
df6

# %%
sns.barplot(x = 'start_station_name', y = 'Avg_tripduration', data = df6)

# %%



