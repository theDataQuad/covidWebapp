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

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.Title('Statewise Viz'),
    html.H1('COVID VIZ',
            style={'color': 'blue',
                   'fontSize': '80px'}),
    dbc.Tabs([
        dbc.Tab([
            dcc.Dropdown(id='selected_state_in_bar',options=[{'label': state, 'value': state}
                          for state in data.statelist()],value='Goa'),#Should be replaced by selection in bar

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
                          for state in data.statelist()],value='Goa'),
           dcc.Dropdown(id='feature',options=[{'label': feature, 'value': feature}
                          for feature in data.featurelist()],value='Confirmed')#remove this
                     ]),
           html.Br(),
           html.Div(id='report'),
           html.Div([
           html.Div([
                html.Div([
                    dcc.Graph(id='line')
                ],className="six columns")
            ],className="row",style={'width':'75%', 'margin':5, 'Align': 'center'}),
           html.Div([
                html.Div([
                    dcc.Graph(id='line2')
                ],className="six columns")
            ],className="row"),
           html.Div([
                html.Div([
                    dcc.Graph(id='line3')
                ],className="six columns")
            ],className="row"),
           html.Div([
                html.Div([
                    dcc.Graph(id='line4')
                ],className="six columns")
            ],className="row")
           ],style={'width':'75%', 'margin':5, 'Align': 'center'})
       ], label='States Comparision')
    ])
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(Output('report', 'children'),
              Input('state1', 'value'),
              Input('state2', 'value'),
              Input('feature', 'value'))
def display_selected_state(state1,state2,feature):
    return 'You selected ' + state1 + ' and ' +state2 +' with feature ' + feature


@app.callback([Output('line', 'figure'),Output('line2','figure'),Output('line3','figure'),Output('line4','figure')],
              [Input('state1', 'value'),
              Input('state2', 'value'),])
             
def display_selected_state_line(state1,state2):
    return lineState([state1,state2],'Tested'),lineState([state1,state2],'Confirmed'),lineState([state1,state2],'Recovered'),lineState([state1,state2],'Deceased')

@app.callback(Output('bar', 'figure'),
              Input('bar_item', 'value'))
def display_death_date(bar_item):
    return barChart()


@app.callback(Output('pie', 'figure'),
              Input('bar',component_property='clickData'))#Input('selected_state_in_bar', 'value'))#should be replaced by input from bar
def display_selected_state_line(state):
    if state is None:
        return pie_chart('India')
    else:
        return pie_chart(state['points'][0]['x'])

if __name__ == '__main__':
    app.run_server(debug=True)
