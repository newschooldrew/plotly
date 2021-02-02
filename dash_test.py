import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background':'#111111','text':'#7FDBFF'}

app.layout = html.Div(children=[
    html.H1('Hello',style={'textAlign':'center',
                           'color':colors['text']}),
    dcc.Graph(id='example',
              figure={'data':[
                  {'x':[1,2,3],
                   'y':[4,5,6],
                   'type':'bar',
                   'name':'SF'},
                {'x':[2,1,3],
                   'y':[3,1,0],
                   'type':'bar',
                   'name':'LA'}
              ], 'layout':{
                    'plot_bgcolor':colors['background'],
                    'paper_bgcolor':colors['background'],
                    'font':{'color':colors['text']},
                    'title':'BAR PLOTS'
              }})
],style={'backgroundColor':colors['background']})

app.run_server()