import pandas
import numpy as np
from matplotlib import pyplot
import plotly.plotly as py
import plotly.graph_objs as go
%matplotlib inline
#TODO : Learn from
#https://plot.ly/pandas/intro-to-pandas-tutorial/
df = pandas.read_csv('/Users/nchandregowda/miniconda3/envs/ProblemSolving/data/populationbycountry19802010millions.csv')
columns = df.columns.values
columns[0]="year"
df.columns= columns
transformed_df = df.T
transformed_df.columns=transformed_df.iloc[0]
transformed_df.drop(transformed_df.index[0],inplace=True)
world_df=transformed_df['World']
pa = pd.Series(world_df.index)
world_df.describe()
pyplot.plot(world_df.index,world_df)
py
import plotly.graph_objs as go
data = [go.Scatter(x=world_df.index, y=world_df)]
py.iplot(data)
py.plot(data)
py.image.save_as(data,"test.png")
