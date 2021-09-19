import pandas as pd

#def __init__():
#   ndf=pd.read_csv('daily.csv')

def daily():
    ndf=pd.read_csv('daily.csv')
    swave=ndf.loc[12610:,["Date",'State','Confirmed','Recovered','Deceased','Other','Tested','Death_Rate']]
    return swave
        

def statelist():
    ndf=pd.read_csv('daily.csv')
    #print(type(ndf['State'].unique()))
    #print(ndf['State'].unique())
    return ndf['State'].unique()#.drop(labels=['India','State Unassigned'])

def featurelist():
    return ['Confirmed','Recovered','Deceased','Tested','Death_Rate']

def vac_percent():
    ndf=pd.read_csv('pop_with_vac.csv')
    return ndf
