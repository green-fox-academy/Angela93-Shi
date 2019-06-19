import requests
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import math


estate_data = pd.read_csv("estate_data4.csv")
data = pd.DataFrame(estate_data)
# print(estate_data['noBed'])

#--------------------------------------------------------------------------------------------------------------
#get the post code
def get_post_code(value):
    list_result = value.split()
    return " ".join(list_result[-2:])

data['postCode'] = data['address'].apply(get_post_code)

#transfer sold price
def transfer_price(value):
    price = int(value[1:].replace(',',''))
    return price

data['soldPrice'] = data['soldPrice'].apply(transfer_price)

#deal with the bedroom
def deal_bedroom(value):
    bedroom_num = (str(value)).split()[0]
    return bedroom_num

data['noBed'] = data['noBed'].apply(deal_bedroom)

#----------------------------------------clean data--------------------------------------------------------------
def get_year(value):
    year = value[-2:]
    return year

data['soldYear'] = data['soldDate'].apply(get_year)

sorted_df = data[data['soldYear'] > '11']
# sorted_df = sorted_df.dropna(subset = ['noBed'])

index_numbers = pd.Series([x for x in range(len(sorted_df))])
new_data = sorted_df.set_index(index_numbers)

new_data['soldYear'] = new_data['soldYear'].astype(int)
#new_data['noBed'] = new_data['noBed'].astype(int)
new_data = new_data.drop(['address','soldDate'], axis=1)
new_data = new_data[new_data['noBed'] != 'nan']

#---------------------merge with ukpostcodes.csv----------------------------------------
ukpostcodes_df = pd.read_csv("ukpostcodes.csv")
ukpostcodes_df = ukpostcodes_df.drop('id',axis=1)
data_df = pd.merge(new_data,ukpostcodes_df,how="left", left_on="postCode",right_on="postcode")
# data_df.to_csv('data_df.csv',header=True,index=False)

# deal with holdType : Freehold :0 ,Leasehold :1
data_df['holdType'] = data_df['holdType'].str.strip()
def holdType(value):
    if value == 'Freehold':
        return 1
    elif value == 'Leasehold':
        return 2
    else:
        return value

# data_df['holdType'] = data_df['holdType'].replace('Freehold',0,inplace=True)
data_df['holdType'] = data_df['holdType'].map(holdType)

#deal with homeType: Semi-Detached:0,Detached:1,Terraced:2,Flat:3
def homeType(value):
    if value == 'Semi-Detached':
        return 1
    elif value == 'Detached':
        return 2
    elif value == 'Terraced':
        return 3
    elif value == 'Flat':
        return 4
    else:
        return value

data_df['homeType'] = data_df['homeType'].map(homeType)

# deal with usage: Residential:0 , Residential\xa0(New Build):1
data_df['usage'] = data_df['usage'].str.strip()

def usage(value):
    if value == 'Residential':
        return 1
    elif value == 'Residential\xa0(New Build)':
        return 2
    else:
        return value

data_df['usage'] = data_df['usage'].map(usage)

#------------------------------build model------------------------------------------
new_data_df = data_df[['holdType','homeType','noBed','soldPrice','usage','latitude','longitude']]
x_train = new_data_df[['holdType','homeType','noBed','usage','latitude','longitude']]
y_train = new_data_df['soldPrice'].apply(math.log)
linear_regression = LinearRegression()
linear_regression.fit(x_train,y_train)
y_predict_test = linear_regression.predict(x_train)
#---------------get the score for this model-----------------------
score = linear_regression.score(x_train,y_train)
# xx = pd.Series([x for x in range(len(x_train))])
# plt.scatter(xx,y_predict_test)
# plt.show()
a = linear_regression.predict([[1,1,2,1,50.953005,-2.641757]])