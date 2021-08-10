#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go

def pie_chart(State):
    url='http://api.covid19india.org/csv/latest/vaccine_doses_statewise_v2.csv'
    vac=pd.read_csv(url)
    pop=pd.read_csv('projected_population2021.csv')

    sumvac=vac.tail(38)

    pop.rename({'State or union territory':'State'},axis=1,inplace=True)
    pop=pop.drop('Rank',axis=1)

    pop['State'][35]="Jammu and Kashmir"
    pop['State'][31]="Andaman and Nicobar Islands"
    pop['State'][32]="Dadra and Nagar Haveli and Daman and Diu"
    pop['State'][37]="Total"
    #342853+242911
    pop.rename({'Population (2021 estimates)':'Population'},axis=1,inplace=True)
    pop['Population'][32]="585764"
    pop['Population']=pop['Population'].str.replace(',','').astype(int)
    df=pd.merge(pop,sumvac,on='State',how='inner')
    df=df.drop('Vaccinated As of',axis=1)
    pie=df[df.State.isin([State])]
    pi=pie.T
    pi.reset_index(inplace=True)
    pi.drop([0,2,3],inplace=True)
    pi.columns=['x','Total']
    li=pi.columns
    #fig = px.pie(dfs, values=li[1], names=li[0], title='Vaccination Percentage')
    #fig.show()
    pie_chart = []
    pie_chart.append(go.Pie(pi, values=li[1], names=li[0], title=State+' Vaccination Percentage'))#color_discrete_sequence=go.colors.sequential.RdBu
    layout_one = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )
    fig = []
    fig.append(dict(data=pie_chart, layout=layout_one))
    return fig

#pie_chart('Lakshadweep')
