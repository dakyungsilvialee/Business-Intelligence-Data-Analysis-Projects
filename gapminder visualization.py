# %%
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# %%
# Load data using gapminder.tsv in Pandas DataFrame 
df = pd.read_csv('/Users/silvialee/ISOM352/gapminder.tsv', sep="\t")
df

# %%
# Bar chart showing population (y-axis) of “United State” over time (x-axis) and bar colors representing the life expectancy

data_US = px.data.gapminder().query("country == 'United States'")
fig = px.bar(data_US, x='year', y='pop', color = 'lifeExp')
fig.show()

# %%
# Line chart for average (over country) lifeExpectancy (y-axis) over time (x-axis) for each continent. Where each continent data is shown in a different facet
# find the average life expectancy for each continent 
avg_lifeExp = df.groupby('country')['lifeExp'].mean()
avg_lifeExp

# append it to our df
df2 = df.append(avg_lifeExp, ignore_index=True)

# display that in different facets
fig = px.area(df2, x="continent", y="lifeExp", facet_col="continent", facet_col_wrap=3)
fig.show()

# %%
# Pie chart showing the distribution of population across countries in the content “Americas”

continent_Americas = px.data.gapminder().query("continent == 'Americas'")
fig = px.pie(continent_Americas, values='pop', names='country')
fig.show()

# %%
# Scatter plot showing gdpPerCapita (x-axis), lifeExpectancy (y-axis), and population (bubble size). 
# Color code the bubbles by continent. Add an animation pane for year.
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent", hover_name="country", animation_frame="year", animation_group="country", log_x=True, size_max=60)
fig

# %%
# Choropleth map of the world showing life expectancy as a color for every country. Add animation pane for the year. 
# (NOTE: you will need the plotly express gapminder data [df = px.data.gapminder()] for column iso_alpha to show the graph)

df_worldmap = px.data.gapminder()
map = px.choropleth(df_worldmap, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", color_continuous_scale='Plasma', height=600)
map.show()


