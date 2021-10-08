#!/usr/bin/env python
print('App is Starting...')
print('#################################################################################################')
import pandas as pd
import dash
import gunicorn
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

from datetime import datetime#timestamp

print('Outside imports Completed')
print('#################################################################################################')
from api import data
from viz.plt import lineState,pie_chart,barChart
print('#################################################################################################')
print('Imports Finished')


print("App is Ready to use at ", datetime.now().strftime("%H:%M:%S"))#timestamp

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

app.layout = html.Div([
    html.Title('Statewise Viz'),
    html.H1('COVID VIZ',
            style={'color': 'blue',
                   'fontSize': '80px'}),
    dbc.Tabs([
        dbc.Tab([
            #dcc.Dropdown(id='bar_item',options=[{'label': feature, 'value': feature}
             #             for feature in ['Death_rate']],value='Death_rate'),
            dbc.Container([
                   dbc.Row([
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([
                html.Div([
                    dcc.Graph(id='bar',clickData=None,figure=barChart())
                ],className="six columns"),
                           ])
                           ], color="dark",className="w-100 mb-3")
                       ],width={"size": 6}),
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([
                html.Div([
                    dcc.Graph(id='pie')
                ],className="six columns")
            ])
                    ], color="dark",className="w-100 mb-3")
                   ],width={"size": 6})
                ],align="center")
                   ],fluid=True)
        ], label='Country'),
       dbc.Tab([
           html.Div([
           dcc.Dropdown(id='state1',multi=True,options=[{'label': state, 'value': state}
                          for state in data.statelist()],value=['Kerala','Goa'], style={'background-color':"black",'color': 'black'})
                     ]),
           html.Br(),
           html.Div([
               dbc.Container([
                   dbc.Row([
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([
                           html.Div([
                               dcc.Graph(id='line')
                            ])
                           ])
                           ], color="dark",className="w-100 mb-3")
                       ],width={"size": 6}),#,width={"size": 5}
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([#"This is some text within a card body", #remove comment if needed
                            html.Div([
                                dcc.Graph(id='line2')
                             ])
                             ])
                    ], color="dark")
                   ],width={"size": 6})
                ],align="center")
                   ],fluid=True),
               html.Br(),
               dbc.Container([
               dbc.Row([
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([
                           html.Div([
                               dcc.Graph(id='line3')
                            ])
                           ])
                           ], color="dark")
                       ],width={"size": 6}),#,width={"size": 5,"offset": 1}
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([#"This is some text within a card body", #remove comment if needed
                            html.Div([
                                dcc.Graph(id='line4')
                             ])
                             ])
                    ], color="dark")
                   ],width={"size": 6})
                ],align="center")
                   ],fluid=True)
           ])
       ], label='States Comparision'),
        dbc.Tab([
            dbc.Container([
               dbc.Row([
                   dbc.Col([],width={"size": 2}),
                   dbc.Col([
            dbc.Carousel(
    items=[
        {"key": "1", "src": "/static/images/slide1.png"},
        {"key": "2", "src": "/static/images/slide2.png"},
        {"key": "3", "src": "/static/images/slide3.png"},
        {"key": "4", "src": "/static/images/slide5.png"}
    ],
    className="carousel-fade")
                ],width={"size": 8})
            ,dbc.Col([],width={"size": 2})
                ],align="center")
                ],fluid=True)
        ], label='Devolepers')
    ])
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

#LINES
@app.callback([Output('line', 'figure'),Output('line2','figure'),Output('line3','figure'),Output('line4','figure')],
              [Input('state1', 'value')])
def display_selected_state_line(state1):
    if len(state1) == 0:
    	return lineState(['India'],'Tested'),lineState(['India'],'Confirmed'),lineState(['India'],'Recovered'),lineState(['India'],'Deceased')
    elif len(state1)==1:
        return lineState(state1,'Tested'),lineState(state1,'Confirmed'),lineState(state1,'Recovered'),lineState(state1,'Deceased')
    else:
        return lineState(state1,'Tested'),lineState(state1,'Confirmed'),lineState(state1,'Recovered'),lineState(state1,'Deceased')



#PIECHART
@app.callback(Output('pie', 'figure'),
              Input('bar',component_property='clickData'))
def display_selected_state_line(state):
    if state is None:
        return pie_chart('India')
    else:
        return pie_chart(state['points'][0]['x'])

if __name__ == '__main__':
    app.run_server(debug=True)
