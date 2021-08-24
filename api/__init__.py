import pandas as pd
import warnings
warnings.filterwarnings("ignore")

url_vac='http://api.covid19india.org/csv/latest/vaccine_doses_statewise_v2.csv'
url_day='https://api.covid19india.org/csv/latest/states.csv'
df=pd.read_csv(url_day)
#TODO: clarify about state unassigned
print("Contact with API")

statelist=df['State'].unique()
ndf = pd.DataFrame(columns=df.columns)
for state in statelist:
    dftest=df.groupby('State').get_group(state)
    dftest=dftest.set_index(['Date'])
    dftest=dftest.drop('State',axis=1).diff(axis=0,periods=1)
    dftest['State']=state
    dftest.reset_index(inplace=True)
    ndf=pd.concat([ndf,dftest])
ndf.sort_values(by=['Date'],ignore_index=True,inplace=True)

ndf['Death_Rate']=((df['Deceased']/df['Confirmed'])*1000).round(2)#it is df's cumulative data and death rate till date
ndf.to_csv('daily.csv',index=False)
print('daily covid data saved!!')

vac=pd.read_csv(url_vac)

vac.to_csv('vac_daily.csv',index=False)
print('daily vaccination data saved!!')

sumvac=vac.tail(38)
sumvac.reset_index(inplace=True)
sumvac['State'][37]="India"

pop=pd.read_csv('projected_population2021.csv')

df=pd.merge(pop,sumvac,on='State',how='inner')
df=df.drop('Vaccinated As of',axis=1)
df['Not_Vaccinated']=df['Population']-df['First Dose Administered']
df.rename({'First Dose Administered':'Partially_Vaccinated','Second Dose Administered':'Fully_Vaccinated'},axis=1,inplace=True)
df.drop('Total Doses Administered',axis=1,inplace=True)

df['Partially_Vaccinated']=df['Partially_Vaccinated']-df['Fully_Vaccinated']

df.to_csv('pop_with_vac.csv',index=False)
print('population data saved!!')
