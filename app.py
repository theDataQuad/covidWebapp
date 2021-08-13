#!/usr/bin/env python
import pandas as pd
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input

from api import data
from viz.plt import lineState,pie_chart,barChart

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1('COVID WEBAPP',
            style={'color': 'blue',
                   'fontSize': '40px'}),
    dbc.Tabs([
       dbc.Tab([
           html.Div([
           dcc.Dropdown(id='state1',options=[{'label': state, 'value': state}
                          for state in data.statelist()],value='Kerala'),
           dcc.Dropdown(id='state2',options=[{'label': state, 'value': state}
                          for state in data.statelist()],value='Goa'),
           dcc.Dropdown(id='feature',options=[{'label': feature, 'value': feature}
                          for feature in data.featurelist()],value='Confirmed')
                     ]),
           html.Br(),
           html.Div(id='report'),
           dcc.Graph(id='line'),
           dcc.Graph(id='pie')
       ], label='States'),
        dbc.Tab([
            dcc.Dropdown(id='bar_item',options=[{'label': feature, 'value': feature}
                          for feature in ['Death_rate']],value='Death_rate'),
            dcc.Graph(id='bar'),
        ], label='Death Rate')
    ])
])

@app.callback(Output('report', 'children'),
              Input('state1', 'value'),
              Input('state2', 'value'),
              Input('feature', 'value'))
def display_selected_state(state1,state2,feature):
    return 'You selected ' + state1 + ' and ' +state2 +' with feature ' + feature


@app.callback(Output('line', 'figure'),
              Input('state1', 'value'),
              Input('state2', 'value'),
              Input('feature', 'value'))
def display_selected_state_line(state1,state2,Feature='Confirmed'):
    return lineState([state1,state2],Feature)

@app.callback(Output('bar', 'figure'),
              Input('bar_item', 'value'))
def display_death_date(bar_item):
    return barChart()


@app.callback(Output('pie', 'figure'),
              Input('state2', 'value'))
def display_selected_state_line(state2):
    return pie_chart(state2)

if __name__ == '__main__':
    app.run_server(debug=True)
