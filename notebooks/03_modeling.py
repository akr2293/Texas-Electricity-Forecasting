#!/usr/bin/env python
# coding: utf-8

# ### Read in Libraries


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from autots import AutoTS


# ### Read in the data


df = pd.read_csv('../data/final_dfs/2019_clean.csv', index_col='date')



df.head()


df['total'] = df.sum(axis=1)




df




# plt.figure(figsize=(12,12))
# plt.plot(df['total'])


# plt.figure(figsize=(11,8))


# df.rolling(30)['Coal'].mean().plot(kind='line')
# df.rolling(30)['NGas'].mean().plot(kind='line')
# df.rolling(30)['Hydro'].mean().plot(kind='line')
# df.rolling(30)['Nuclear'].mean().plot(kind='line')
# df.rolling(30)['Other'].mean().plot(kind='line')
# df.rolling(30)['Solar'].mean().plot(kind='line')
# df.rolling(30)['Wind'].mean().plot(kind='line')

# plt.legend(['Biomass', 'Coal', 'NGas', 'Hydro', 'Nuclear', 'Other', 'Solar', 'Wind'])


# ## VAR Time Series Models


# Code written by Joseph Nelson.
# Improved by Hovanes Gasparian

def interpret_dftest(dftest):
    dfoutput = pd.Series(dftest[0:3], index=['Test Statistic','p-value', 'Lag Used'])
    return dfoutput


# ## Dickey-Fuller Tests on each Source

# ### Biomass

# biomass_adf = interpret_dftest(adfuller(df['Biomass']))


# ### Coal


# print(interpret_dftest(adfuller(df['Coal'])))



# print(interpret_dftest(adfuller(df['NGas'])))


# # Differenced 
# print(interpret_dftest((adfuller(df['NGas'].diff(1).dropna()))))



# print(interpret_dftest(adfuller(df['Hydro'])))



# print(interpret_dftest(adfuller(df['Nuclear'])))


# print(interpret_dftest(adfuller(df['Other'])))



# print(interpret_dftest(adfuller(df['Wind'])))


# print(interpret_dftest(adfuller(df['Solar'])))


# ### Plot ACF & PACF


# plot the total electricity acf
plot_acf(df['total'], lags = 50);



# plot the total electricity pacf
plot_pacf(df['total'], lags = 50)

models = ["MotifSimulation","VAR"]
model = AutoTS(
    forecast_length=10,
    frequency='infer',
    prediction_interval=0.9,
    ensemble="all",
    model_list=models,
	transformer_list="fast",
    max_generations=100,
    num_validations=4,
    validation_method="even")




df.index = pd.to_datetime(df.index)


model = model.fit(df["Nuclear"])

prediction = model.predict()

forecasts_df = prediction.forecast
forecasts_df.plot()
model_results = model.results()
# and aggregated from cross validation
validation_results = model.results("validation")

validation_results["ModelParameters"].head(1)

print(df.columns)

columns = df.columns
print(columns)


def dickey(columns):
    plt.figure(figsize=(11,8))
    for i in columns:
        print(i)
        print(interpret_dftest(adfuller(df[i])))
        
        df.rolling(30)[i].mean().plot(kind='line')
    plt.legend(columns)

    

xxv =dickey(columns)