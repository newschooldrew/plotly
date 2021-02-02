import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go

app = dash.Dash()
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([dcc.Graph(id='scatterplot1',
                                 figure={'data': [
                                     go.Scatter(
                                         x=random_x,
                                         y=random_y,
                                         mode='markers',
                                         marker={
                                             'size':12,
                                             'color':'rgb(50,200,150)',
                                             'line':{'width':2}
                                         }
                                     )],
                                     'layout': go.Layout(title='Scatter plot')}),
                       dcc.Graph(id='scatterplot2',
                                 figure={'data': [
                                     go.Scatter(
                                         x=random_x,
                                         y=random_y,
                                         mode='markers',
                                         marker={
                                             'size': 12,
                                             'color': 'rgb(250,10,150)',
                                             'line': {'width': 2}
                                         }
                                     )],
                                     'layout': go.Layout(title='Scatter plot 2')})
                       ])
app.run_server()