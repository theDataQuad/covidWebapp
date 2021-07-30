#!/usr/bin/env python
from flask import Flask, render_template, flash, request, jsonify, Markup


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64, os

matplotlib.use('Agg')
app = Flask(__name__)


@app.before_first_request
def startup():
    def twoStates(slist,feature):
            df=swave[swave.State.isin(slist)]
            x = np.random.randint(low=0, high=5, size=150)

            fig, ax = plt.subplots(figsize=(12, 7))
            sns.lineplot(data=df, x="Date", y=feature, hue="State",linewidth = 2)
            plt.legend( bbox_to_anchor=(1.02, 1),loc='upper left', borderaxespad=0, title='states')
            plt.title(feature+' Comparrison')
            plt.xticks(np.arange(0, len(x)+15, 20))
            #ax.set_xticks(np.arange(0, len(x)+1, 5))
            img = io.BytesIO()
            plt.savefig(img, format='png')
            return(img.seek(0))
    df=pd.read_csv('states18.csv')
    statelist=df['State'].unique()
    c=df.columns
    ndf = pd.DataFrame(columns=c)
    ndf=pd.DataFrame()
    for state in statelist:
        dftest=df.groupby('State').get_group(state)
        dftest=dftest.set_index(['Date'])
        dftest.drop('State',axis=1,inplace=True)
        dftest=dftest.diff(axis=0,periods=1)
        dftest['State']=state
        dftest.reset_index(inplace=True)
        ndf=pd.concat([ndf,dftest])
    ndf.sort_values(by=['Date'],ignore_index=True,inplace=True)
    ndf.dtypes
    swave=ndf.loc[12610:,["Date",'State','Confirmed','Recovered','Deceased','Other','Tested']]
#swave.groupby('State').get_group("Kerala").plot(x='Date',y=['Confirmed','Tested'],figsize=(10,8.5),label=['Kerala_Confirmed',"tested"])
#plt.legend()
#swave.groupby('State').get_group("Uttar Pradesh").plot(x='Date',y=['Confirmed','Tested'],figsize=(10,8.5),label=['UPConfirmed','Tested'])
#plt.xticks(rotation=60)
#plt.legend()
#plt.title('Two or more lines on same plot with suitable legends ')
#plt.show()

#kerala=swave.groupby('State').get_group("Kerala")
#ktest=kerala['Tested']
#ktest
#kconf=kerala['Confirmed']
#up=swave.groupby('State').get_group("Uttar Pradesh")
#utest=up["Tested"]
#uconf=up['Confirmed']
#date=up['Date']


#fig, ax = plt.subplots(figsize=(12, 7))
#plt.plot(date, ktest, label = "kerala tested")
#plt.plot(date, kconf, label = "kerala confirmed")
#plt.plot(date,utest,label='up tested')
#plt.plot(date,uconf,label='up confirmed')
#plt.legend()

#swave.head()
#li=['Kerala','Uttar Pradesh']
#klup=swave[swave.State.isin(li)]
#x = np.random.randint(low=0, high=5, size=150)

#fig, ax = plt.subplots(figsize=(12, 7))
#sns.lineplot(data=klup, x="Date", y='Confirmed', hue="State",linewidth = 2)
#plt.legend( bbox_to_anchor=(1.02, 1),loc='upper left', borderaxespad=0, title='feature')
#plt.title('covid comparrisson')
#plt.xticks(np.arange(0, len(x)+15, 20))
#ax.set_xticks(np.arange(0, len(x)+1, 5))
#plt.show
DEFAULT_STATE1='India'
DEFAULT_STATE2='Kerala'

@app.route("/", methods=['POST', 'GET'])
def submit_new_request():
    if request.method == 'POST':
        selected_state1 = request.form['selected_state1']
        selected_state2 = request.form['selected_state2']
        states=[selected_state1,selected_state2]
        feature='Confirmed'
        img=twoStates(states,feature)
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        return render_template('index.html',
                model_plot = Markup('<img src="data:image/png;base64,{}">'.format(plot_url)),
            selected_state1=selected_state1,
            selected_state2=selected_state2)
    else:
        return render_template('index.html',
            model_plot = '',
            selected_state1=DEFAULT_STATE1,
            selected_state2=DEFAULT_STATE2)

if __name__=='__main__':
	app.run(debug=False)
