#!/usr/bin/env python
from flask import Flask, render_template, flash, request, jsonify, Markup


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv('states18.csv')
#df.head()


# In[3]:


#df.tail()


# In[4]:


statelist=df['State'].unique()


# ### The above data set is in a cumulative form we have convert it to the usual form

# In[5]:


#newdf=pd.DataFrame()


# In[6]:


#test=df.groupby('State').get_group('India')


# In[7]:


test.tail()


# In[8]:


#test=test.set_index(['Date'])
#test.head(2)


# In[9]:


#test.drop('State',axis=1,inplace=True)
#test.tail()


# In[10]:


#test=test.diff(axis=0,periods=1)
#test.tail()


# In[11]:


#test['State']='India'
#test.tail()


# In[12]:


#test.reset_index()


# In[13]:


#newdf.append(test, ignore_index = True)


# In[14]:


c=df.columns


# In[15]:


ndf = pd.DataFrame(columns=c)


# In[16]:


ndf=pd.DataFrame()


# In[17]:


for state in statelist:
    dftest=df.groupby('State').get_group(state)
    
    dftest=dftest.set_index(['Date'])
    
    dftest.drop('State',axis=1,inplace=True)
    
    dftest=dftest.diff(axis=0,periods=1)
    
    dftest['State']=state
    
    
    
    dftest.reset_index(inplace=True)
    
   # display(dftest.tail())
    
    #ndf.append(dftest,ignore_index = True)
    ndf=pd.concat([ndf,dftest])
    
    


# In[18]:


#ndf.tail()


# In[19]:


#df.shape


# In[20]:


n#df.shape


# In[21]:


ndf.sort_values(by=['Date'],ignore_index=True,inplace=True)


# In[22]:


#display(ndf.head(2))
#ndf.tail(2)


# In[23]:


#ndf.isnull().sum()


# In[24]:


ndf.dtypes


# #### Aproximately splitting the data set into First wave and second wave by assuming that  the seceond wave started in march 2021 in india
# 

# In[25]:


#ndf


# In[26]:


#ndf.loc[ndf['Date']=='2021-03-01']


# In[27]:


swave=ndf.loc[12610:,["Date",'State','Confirmed','Recovered','Deceased','Other','Tested']]


# In[28]:


#swave.head()


# In[ ]:





# In[29]:


#swave.groupby('State').get_group("Kerala").plot(x='Date',y=['Confirmed','Tested'],figsize=(10,8.5),label=['Kerala_Confirmed',"tested"])
#plt.legend()
#swave.groupby('State').get_group("Uttar Pradesh").plot(x='Date',y=['Confirmed','Tested'],figsize=(10,8.5),label=['UPConfirmed','Tested'])
#plt.xticks(rotation=60)
#plt.legend()
#plt.title('Two or more lines on same plot with suitable legends ')
#plt.show()


# In[30]:


#kerala=swave.groupby('State').get_group("Kerala")
#ktest=kerala['Tested']
#ktest
#kconf=kerala['Confirmed']
#up=swave.groupby('State').get_group("Uttar Pradesh")
#utest=up["Tested"]
#uconf=up['Confirmed']
#date=up['Date']


# In[31]:


#fig, ax = plt.subplots(figsize=(12, 7))
#plt.plot(date, ktest, label = "kerala tested")
#plt.plot(date, kconf, label = "kerala confirmed")
#plt.plot(date,utest,label='up tested')
#plt.plot(date,uconf,label='up confirmed')
#plt.legend()


# In[33]:


#swave.head()


# In[36]:


#li=['Kerala','Uttar Pradesh']
#klup=swave[swave.State.isin(li)]


# In[87]:


#x = np.random.randint(low=0, high=5, size=150)

#fig, ax = plt.subplots(figsize=(12, 7))
s#ns.lineplot(data=klup, x="Date", y='Confirmed', hue="State",linewidth = 2)
#plt.legend( bbox_to_anchor=(1.02, 1),loc='upper left', borderaxespad=0, title='feature')
#plt.title('covid comparrisson')
#plt.xticks(np.arange(0, len(x)+15, 20))
#ax.set_xticks(np.arange(0, len(x)+1, 5))
#plt.show


# In[90]:


def twoStates(slist,feature):
    df=swave[swave.State.isin(slist)]
    x = np.random.randint(low=0, high=5, size=150)

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.lineplot(data=df, x="Date", y=feature, hue="State",linewidth = 2)
    plt.legend( bbox_to_anchor=(1.02, 1),loc='upper left', borderaxespad=0, title='states')
    plt.title(feature+' Comparrison')
    plt.xticks(np.arange(0, len(x)+15, 20))
    #ax.set_xticks(np.arange(0, len(x)+1, 5))
    plt.show
    




