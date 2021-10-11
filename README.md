# COVID WebApp
This project is intended to be a "learning by doing" experience for the developer team.
This was a learning-oriented project done by the devolepers to learn more about git, flask, dash, plotly, deployment,etc and to get the practical experience in handling a project. The whole project was done with the data from COVID INDIA API. In this 
project we created visualization of COVID and vaccination status which includes the statewise Deathrate,Tested cases,Confirmed cases,Recovered cases,Deceased Cases.
Plotly, being more sophisticated is used as data visualization tool  for creating elaborate plots more efficiently. 




## Acknowledgements

 - [COVID INDIA API](https://github.com/covid19india/api)
  


  
## Demo
 

  ![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/86158829/136753012-37c5a8cb-c2e2-4ba6-9171-277bc0241664.gif)

## Documentation
This project aims to create a covid webapp.It is a "learning by doing"experience which provided us the practical experience in handling of git,flask,plotly,dash,deployment etc.This project was done with the data from COVID INDIA API.This covid webapp provides the visualizations of vaccination status in the states of India along with the statewise Death rate,Tested Cases,Confirmed Cases,Recovered Cases,Deceased Cases.Thus making  an efficient way of comparison.

  -Statewise Deathrate is plotted in bar chart,vaccination status in pie chart with labels partially_vaccinated,fully vaccinated and not vaccinated.
  
  -Clicking on a bar in the bar chart makes changes in the adjacent pie chart. (APP Feature) 
  
  -Placing cursor on a single bar shows the state name and death rate of corresponding state(APP Feature).
  
  -Selecting the 'box select' option we can zoom into any particular states by clicking and draging the square box.(DASH Feature)
  
  -Using 'lasso select' option we can freely choose the area that we need to focus by drawing shapes.(DASH Feature).
  
  -Clicking on 'Pan select' option we can move along x and y axises also by using 'Reset axis' option we can reset it.(DASH Feature)
  
  -Using 'Autoscale' option or double clicking on screen we can reset the graph.(DASH Feature).
  
  -Clicking on a legend item of the pie chart makes that item disappear (You can use this feature to tell total vs partially  vaccinated). (DASH Feature)
  
  -Placing the cursor on any particular case of Vaccination Pie chart shows it's label,number of respective case and it's   percentage.(APP Feature)
  
  -In the state comparison tab, selecting no state will result in the line chart of India. (APP Feature)
  
  -In the state comparison tab, the Search option is available. (DASH Feature)
  
  -Cases like Tested,Confirmed,Recovered,Deceased are shown in line chart.Each state is shown in different colour .
  
  -Multiple states can be viewed altoghther which gives the user the better understanding of case rate in each state.(APP   Feature).
  
  -Clicking on the legend item of any particular selected state,makes the line chart of that state disapper(With this feature we can easily differentiate the lines of other states).(DASH Feature)
  
  -Placing the cursor on any point of line graph shows the state,date and number of respective cases reported.(DASH Feature)
  
## Screenshots

![covidwebapp](https://user-images.githubusercontent.com/86158829/136670586-05271c6a-27fd-40f1-adec-17026fc62bd8.png)

![coviviz](https://user-images.githubusercontent.com/86158829/136839294-3d6c8912-ed34-4d00-b2a3-0afdb152fd43.png)

## Deployment

To see the deployed project, follow the link

```bash
  https://coviviz.herokuapp.com/.
```
  
## Authors
- [@Vaishak N](https://github.com/VaishU2235)
- [@Prabin Raj K P](https://github.com/prabinrajkp)
- [@Sreenivas Shenoy](https://github.com/sreeni7799)
- [@Adheena P](https://github.com/Adheena19)
