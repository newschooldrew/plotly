# bar chart
#   categories -> x axis
#   aggregation -> y axis

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./Data/mocksurvey.csv',index_col=0)

data = [go.Bar(x=df.index,y=df[res],name=res) for res in df.columns]

# horizontal chart
#data = [go.Bar(y=df.index,x=df[res],orientation='h',res) for res in df.columns]

layout = go.Layout(title='Bar Chart',barmode='stack')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)