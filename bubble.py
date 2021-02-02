import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./Data/mpg.csv', na_values={'horsepower':'?'})

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   # this is the part that makes it a
                   #bubble chart
                   marker=dict(size=df['weight']/100),
                   # color=df['cylinders'],
                   # showscale=True
                   )]

layout = go.Layout(title="Bubble Chart",hovermode='x')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)