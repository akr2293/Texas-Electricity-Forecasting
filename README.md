# DSI Capstone - CHECK-IN 2
### Electricity Consumption and Winter Storm Uri

### Problem Statement
Winter Storm Uri, which devastated the Texas electrical grid in February of 2021, led many to questioning the viability of different energy sources for powering the lives of the vast majority of Texans.

Texas generally has a diverse profile of inputs for it's electricity generation despite being known as a major proudcer and consumer of fossil fuels. It is even the #1 producer of wind energy in the United States. This project aims to conduct multivariate time series analysis to address forecast how this mix of generation sources is projected to change given current rates. This will help guide infrastructure planning for new pipelines and electric lines as more of this energy comes online.


### Methods and Goals:
Several methods for multivariate regression are being explored for the project and warrant further investigation. However, methods such as Vector Auto Regression and XGBoost are potential options.

Given this is a forecasting problem, I will aim to optimize RMSE, however what that precise goal is quantitatively is currently unknown.

### Datasources
Primary dataset comes from the ERCOT (Electric Reliability Council of Texas) and consists of .xlsx data from 2007 to the present day (covering Winter Storm Uri) and is recorded at the granularity of every fifteen minutes.

The data has time in columns and each row is a day/data source. So there will be a decent amount of cleaning to get the data into a form necessary for modeling. The data is located in the "FuelMixReport_PreviousYears" folder within the "data" repo.


### Items to boost the appeal
Additionally, the incorporation of climate data such as temperature, cloud cover, and wind could provide further features for predicting how consumption will change relative to given generation sources.

Also, the EIA publishes realtime demand for the ERCOT system, so I could potentially investigate how the energy mix changes during periods of steady demand versus demand during periods with high variance.

# Risks and Challenges
Following the cleaning, the modeling process _shouldn't_ be terribly challenging after. So, a major challenge will be making the project interesting to the point that it's not just a simple forecasting model. This is why I would like to incorporate other sources like climate or demand.

**Initial cleaning efforts are in the 01_cleaning notebook on my github**


Main Data source:
http://www.ercot.com/gridinfo/generation

Additional Data sources:
Real time EIA Electricity demand:
https://www.eia.gov/realtime_grid/#/data/graphs?end=20210324T18&start=20210317T22&bas=002&regions=0
