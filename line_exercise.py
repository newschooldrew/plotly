import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('./Data/2010YumaAZ.csv')

days = []

df.set_index('DAY',inplace=True)
for day in df.index:
    days.append(day)

frame_days = pd.DataFrame(days)
frame_days_unique = frame_days.drop_duplicates()
the_days = frame_days_unique[0].to_list()
data = []

df.reset_index(inplace=True)
print(df)

for day in the_days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y= df[df['DAY'] == day]['T_HR_AVG'],
                       mode='lines',name=day)
    data.append(trace)

layout = go.Layout(title='Yuma Temps')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='line_exercise.html')