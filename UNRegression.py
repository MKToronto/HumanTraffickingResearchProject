# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 13:13:02 2016

@author: marckendal
"""

import pandas as pd

mergedUEM = pd.read_csv('UNMerged.csv')
print(mergedUEM.head())

import scipy.stats  as sc
import matplotlib.pyplot as plt






# start with importing statsmodels
import statsmodels.api as sm

regressors = mergedUEM.as_matrix(['GDP per Capita 2015', 'Proportion of seats held by women in national parliaments (%)', 'Unemployment, female (% of female labor force)']) 

referrals_2015_matrix = mergedUEM.as_matrix(['Referals in 2015'])
referrals_2015 = referrals_2015_matrix[:,0]

# our dependent variable is Ref
# we use the OLS function from statsmodels
model = sm.OLS(referrals_2015,regressors)
results = model.fit()

# the summary function returns a very comprehensive report on the results
print ("Params: ", results.summary())
    



#gdp2015= matrix_array[:,0]
women_parliament = regressors[:,1]
unemployment =  regressors[:,2]
#
women_parliament_r, pvalue1 = sc.stats.pearsonr(women_parliament,referrals_2015)
wp_spearman_r, pvalue2 = sc.stats.spearmanr(women_parliament,referrals_2015)

print ("Correlation Pearson: ", women_parliament_r, pvalue1)
print("Correlation Spearman: ", wp_spearman_r, pvalue2)
##
##
plt.figure(1)
plt.suptitle('Proportion of seats held by women in national parliaments (%) vs. Referals in 2015')
plt.xlabel('Proportion of seats held by women in national parliaments')
plt.ylabel('Referals in 2015')
#plt.scatter(arr1, arr2 , c = "#D06B36", s = 50, alpha = 0.4, linewidth='0')
plt.scatter(women_parliament,referrals_2015, c = "#D06B36", s = 50, alpha = 0.4, linewidth='0')

#unemployment_r = sc.stats.pearsonr(unemployment,referrals_2015)
#spearman_r = sc.stats.spearmanr(unemployment,referrals_2015)
###
###
#plt.scatter(unemployment,referrals_2015)
##
#slope, intercept, r_value, p_value, std_err = sc.stats.linregress(x,y)