import pandas as pd

#def __init__():
#   ndf=pd.read_csv('daily.csv')

def daily():
    ndf=pd.read_csv('daily.csv')
    swave=ndf.loc[12610:,["Date",'State','Confirmed','Recovered','Deceased','Other','Tested']]
    return swave

def statelist():
    ndf=pd.read_csv('daily.csv')
    return ndf['State'].unique()

def featurelist():
    return ['Confirmed','Recovered','Deceased','Tested']

def vac_percent():
    ndf=pd.read_csv('pop_with_vac.csv')
    return ndf
