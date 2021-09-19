from api import data
import pandas as pd
from plotly.express import line as px_line
import plotly.graph_objs as go

def lineState(State,Feature):
    #REMOVE GRID LINES
    swave=data.daily()
    s=swave[swave.State.isin(State)]
    return px_line(s, x="Date", y=Feature,color='State',title='Comparison of '+Feature+' Cases in '+State[0]+' and '+State[1]).update_layout(
                        template='plotly_dark',
                        plot_bgcolor= 'rgba(0, 0, 0, 0)',
                        paper_bgcolor= 'rgba(0, 0, 0, 0)')


def pie_chart(State):
    df=data.vac_percent()
    pi=df[df.State.isin([State])].T
    pi.reset_index(inplace=True)
    pi.drop([0,1,2],inplace=True)
    pi.columns=['x','Total']
    x=pi['x'].tolist()
    y=pi['Total'].tolist()
    trace = go.Pie(labels=x,values=y)
    data_to_plot = [trace]
    layout_one = go.Layout(height=900, width=900,title=go.layout.Title(text='Vaccination status of '+State))
    pie_chart = go.Figure(data = data_to_plot,layout=layout_one)
    pie_chart.update_layout(paper_bgcolor="#113340")
    pie_chart.layout.legend.font.color = 'white'
    pie_chart.layout.titlefont.color = 'white'
    return pie_chart

def barChart():
    last37=data.daily()
    last37=last37.tail(37)
    last37.sort_values(by='Death_Rate',inplace=True,ascending=False)
    data_to_plot = [go.Bar(x =last37['State'],y =last37['Death_Rate'] ,orientation="v")]
    layout=go.Layout(height=900, width=900,title=go.layout.Title(text="Statewise Death Rates"),plot_bgcolor='#113340')
    fig = go.Figure(data=data_to_plot,layout=layout)
    fig.update_layout(paper_bgcolor="#113340")
    fig.layout.xaxis.color = 'white'
    fig.layout.yaxis.color = 'white'
    fig.layout.titlefont.color = 'white'
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    return fig
