#!/usr/bin/env python
print('App is Starting...')
print('#################################################################################################')
import pandas as pd
import dash
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


#now = #timestamp
#current_time = now#timestamp
print("App is Ready to use at ", datetime.now().strftime("%H:%M:%S"))#timestamp

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    html.Title('Statewise Viz'),
    html.H1('COVID VIZ',
            style={'color': 'blue',
                   'fontSize': '80px'}),
    dbc.Tabs([
        dbc.Tab([
            dcc.Dropdown(id='bar_item',options=[{'label': feature, 'value': feature}
                          for feature in ['Death_rate']],value='Death_rate'),
            html.Div([
                html.Div([
                    dcc.Graph(id='bar',clickData=None)
                ],className="six columns"),
                html.Div([
                    dcc.Graph(id='pie')
                ],className="six columns")
            ],className="row")
        ], label='Country'),
       dbc.Tab([
           html.Div([
           dcc.Dropdown(id='state1',options=[{'label': state, 'value': state}
                          for state in data.statelist()],value='Kerala'),
           dcc.Dropdown(id='state2',options=[{'label': state, 'value': state}
                          for state in data.statelist()],value='Goa')
                     ]),
           html.Br(),
           html.Div([
               dbc.Row([
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([
                           html.Div([
                               dcc.Graph(id='line')
                            ])
                           ])
                           ], color="dark")
                       ],width=6),#,width={"size": 5}
                   dbc.Col([
                       dbc.Card([
                           dbc.CardBody([#"This is some text within a card body", #remove comment if needed
                            html.Div([
                                dcc.Graph(id='line2')
                             ])
                             ])
                    ], color="dark")
                   ],width=6)
                ],align="center"),
               html.Br(),
               dbc.Row([
                html.Div([
                    dcc.Graph(id='line3')
                ]),
                html.Div([
                    dcc.Graph(id='line4')
                ])
            ],align="center",),
           ],style={'width':'75%', 'margin':5, 'Align': 'center'})
       ], label='States Comparision')
    ])
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

#LINES
@app.callback([Output('line', 'figure'),Output('line2','figure'),Output('line3','figure'),Output('line4','figure')],
              [Input('state1', 'value'),
              Input('state2', 'value'),])
def display_selected_state_line(state1,state2):
    return lineState([state1,state2],'Tested'),lineState([state1,state2],'Confirmed'),lineState([state1,state2],'Recovered'),lineState([state1,state2],'Deceased')

#BARCHART
@app.callback(Output('bar', 'figure'),
              Input('bar_item', 'value'))
def display_death_date(bar_item):
    return barChart()

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
