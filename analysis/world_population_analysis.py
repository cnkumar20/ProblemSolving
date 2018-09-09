import pandas
import numpy as np
from matplotlib import pyplot
import plotly.plotly as py
import plotly.graph_objs as go
%matplotlib inline
#TODO : Learn from
#https://plot.ly/pandas/intro-to-pandas-tutorial/
df = pandas.read_csv('/Users/nchandregowda/miniconda3/envs/ProblemSolving/data/populationbycountry19802010millions.csv')
df.describe()
df.head(4)
df.index
df.head(0)
columns = df.columns.values
columns
columns[0]="year"
columns
df.columns= columns
df.head(2)
transformed_df = df.T
transformed_df.describe
transformed_df.head(1)

transformed_df.columns=transformed_df.iloc[0]
transformed_df.head(3)
transformed_df.drop(transformed_df.index[0],inplace=True)
transformed_df.head(3)

world_df
pa = pd.Series(world_df.index)
world_df.describe()

world_df
pyplot.plot(world_df.index,world_df)
py
import plotly.graph_objs as go
data = [go.Scatter(x=world_df.index, y=transformed_df)]
py.iplot(data)
py.image.save_as(data,"test.png")
