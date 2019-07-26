# -*- coding: utf-8 -*-

"""
Created on Thu Dec  8 15:34:48 2016

@author: marckendal
"""

# This code will merge UN indicator data with the existing  Human trafficking Data
import pandas as pd

#
#GDP Date MERGING
GDPData = pd.read_csv('GDP.csv', skiprows=4)
HTData = pd.read_csv('Final_Decisions_2015_Total_Removed.csv')
GDPData2015 = GDPData.loc[:,['Country Name','2015']]
# In order to merge files it is necessary to have the same common column names
GDPData2015_Rename = GDPData2015.rename(columns = {'2015':'GDP per Capita 2015'})
HTData_Column_Name_Change = HTData.rename(columns = {'Nationality':'Country Name'})
#Merging Data File
mergedGDP  = pd.merge(HTData_Column_Name_Change, GDPData2015_Rename, on='Country Name')

#GEN Data Merging
GENData = pd.read_csv('GEN.csv', skiprows=4)
GENData2015 = GENData.loc[:,['Country Name','2015']]
GENData2015_Rename = GENData2015.rename(columns = {'2015':'Proportion of seats held by women in national parliaments (%)'})
mergedGEN  = pd.merge(mergedGDP, GENData2015_Rename, on='Country Name')


#UEM Data Merging
UEMData = pd.read_csv('UEM.csv', skiprows=4)
UEMData2015 = UEMData.loc[:,['Country Name','2014']]
UEMData2015_Rename = UEMData2015.rename(columns = {'2014':'Unemployment, female (% of female labor force)'})
mergedUEM  = pd.merge(mergedGEN, UEMData2015_Rename, on='Country Name')
print (mergedUEM .head())  


mergedUEM.to_csv('UNMerged.csv',header=True, index=False)

print (mergedUEM .head()) 

