import pandas as pd
from numpy import delete

#def __init__():
#   ndf=pd.read_csv('daily.csv')

def daily():
    ndf=pd.read_csv('daily.csv')
    swave=ndf.loc[12610:,["Date",'State','Confirmed','Recovered','Deceased','Other','Tested','Death_Rate']]
    return swave


def statelist():
    ndf=pd.read_csv('daily.csv')
    sl=ndf['State'].unique()
    sln=[]
    for i in sl:
    	if i=='India'or i=='State Unassigned':
    		continue
    	else:
    		sln.append(i)
    return sln

def featurelist():
    return ['Confirmed','Recovered','Deceased','Tested','Death_Rate']

def vac_percent():
    ndf=pd.read_csv('pop_with_vac.csv')
    return ndf
