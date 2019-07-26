# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:08:24 2016

@author: marckendal

As discussed with Cagatay, since I haven't scraped my data into the right 
format for analysis yet, I just need to show that I have made progress with 
Python with similar data.
See below, where I have taken the crime data from the tutorial and done 
some analysis of the data, including analysing the relationship betweeen 
median Income and Violent Crimes per Population and have utilised pearsons, 
spearmans, and linear regression and have plotted the variables on a scatter 
plot.
"""

#import csv as csv
#import numpy as np
import pandas as pd
#import statsmodels.api as sm
import scipy.stats  as sc
import matplotlib.pyplot as plt


crime_data = pd.read_csv('censusCrimeClean.csv')
print(crime_data.head())

matrix_array = crime_data.as_matrix(['medIncome', 'ViolentCrimesPerPop']) 
print (matrix_array)
#matrix_array = crime_data.as_matrix() 
x= matrix_array[:,0]
y= matrix_array[:,1]




pearsons_r = sc.stats.pearsonr(x,y)
spearman_r = sc.stats.spearmanr(x,y)


plt.scatter(x,y)

slope, intercept, r_value, p_value, std_err = sc.stats.linregress(x,y)

#model = sm.OLS(y,x)
#results = model.fit()
