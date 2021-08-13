import pandas as pd

url_vac='http://api.covid19india.org/csv/latest/vaccine_doses_statewise_v2.csv'
url_day='https://api.covid19india.org/csv/latest/states.csv'
df=pd.read_csv(url_day)
print("Contact with API")
#global statelist
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
ndf.to_csv('daily.csv',index=False)
print('daily covid data saved!!')

vac=pd.read_csv(url_vac)
#change total to india
vac.to_csv('vac_daily.csv',index=False)
print('daily vaccination data saved!!')

sumvac=vac.tail(38)

pop=pd.read_csv('projected_population2021.csv')

##remove
pop.rename({'State or union territory':'State'},axis=1,inplace=True)
pop=pop.drop('Rank',axis=1)
pop['State'][35]="Jammu and Kashmir"
pop['State'][31]="Andaman and Nicobar Islands"
pop['State'][32]="Dadra and Nagar Haveli and Daman and Diu"
pop['State'][37]="Total"
pop.rename({'Population (2021 estimates)':'Population'},axis=1,inplace=True)
pop['Population'][32]="585764"
pop['Population']=pop['Population'].str.replace(',','').astype(int)

df=pd.merge(pop,sumvac,on='State',how='inner')
df=df.drop('Vaccinated As of',axis=1)
df['Not_Vaccinated']=df['Population']-df['First Dose Administered']
df.rename({'First Dose Administered':'Partially_Vaccinated','Second Dose Administered':'Fully_Vaccinated'},axis=1,inplace=True)
df.drop('Total Doses Administered',axis=1,inplace=True)
df['Partially_Vaccinated1']=df['Partially_Vaccinated']-df['Fully_Vaccinated']
df.to_csv('pop_with_vac.csv',index=False)
print('population data saved!!')
