import requests
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
from bs4 import BeautifulSoup

street_list = {'Bath':'116','Bridgwater':'212','Burnham-On-Sea':'251','Chard':'301','Cheddar':'306','Clevedon':'337','Crewkerne':'381','Frome':'536','Glastonbury':'551','Ilminster':'678','Minehead':'942','Radstock':'1109','Shepton+Mallet':'1198','Street':'1287','Taunton':'1317','Wellington':'1414','Wells':'1415','Weston-Super-Mare':'1437','Wincanton':'1458','Yeovil':'1497'}

#street_list = {'Bath':'116'}
base_url = "https://www.rightmove.co.uk/house-prices/detail.html?country=england&locationIdentifier=REGION%5E"

# def get_description(item):
#     if item.find('a',{'class':'soldAddress'}):
#         a_link = item.find('a',{'class':'soldAddress'}).get('href')
#         detail_page = requests.get(f"{a_link}")
#         detail = BeautifulSoup(detail_page.content,"html.parser")
#         try:
#             key_features = detail.find('ul',{'class':'keyfeatures'}).text
#             key_features = " ".join(list(key_features.split("\n")))
#             return key_features
#         except:
#             pass

def get_info():
    estate_info = []
    for key,value in street_list.items():
        specific_url = base_url + value + "&searchLocation=" + key
        for j in range(0,40 *25,25):
            specific_index_url = specific_url + "&index=" + str(j)
            page = requests.get(specific_index_url)
            soup = BeautifulSoup(page.content,"html.parser")
            items = soup.find_all('li', class_='soldUnit')
            for item in items:
                estate_info_item = {}
                sold_price = item.find('td',{'class':'soldPrice'}).text
                estate_info_item["soldPrice"] = sold_price

                home_type = item.find('td',{'class':'soldType'}).text.split(',')[0]
                estate_info_item["homeType"] = home_type

                hold_type = item.find('td',{'class':'soldType'}).text.split(',')[1]
                estate_info_item["holdType"] = hold_type

                usage = item.find('td',{'class':'soldType'}).text.split(',')[2]
                estate_info_item["usage"] = usage

                sold_date = item.find('td',{'class':'soldDate'}).text
                estate_info_item["soldDate"] = sold_date
                try:
                    sold_bed = item.find('td',{'class':'noBed'}).text
                    estate_info_item["noBed"] = sold_bed
                except:
                    pass
                sold_address = item.find(['a','div'],{'class':'soldAddress'}).text
                # description = get_description(item)
                estate_info_item["address"] = sold_address
                estate_info_item["city"] = key
                # estate_info_item["description"] = description
                estate_info.append(estate_info_item)
    return estate_info

estate_info = get_info()

data =  pd.DataFrame(estate_info)
data.to_csv('estate_data4.csv',header=True,index=False)
#--------------------------------------------------------------------------------------------------------------
#get the post code
# def get_post_code(value):
#     list_result = value.split()
#     return "".join(list_result[-2:-1])

# data['postCode'] = data['address'].apply(get_post_code)

# #transfer sold price
# def transfer_price(value):
#     price = int(value[1:].replace(',',''))
#     return price

# data['soldPrice'] = data['soldPrice'].apply(transfer_price)

# #deal with the bedroom
# def deal_bedroom(value):
#     bedroom_num = (str(value)).split()[0]
#     return bedroom_num

# data['noBed'] = data['noBed'].apply(deal_bedroom)
#-------------------------------------------------------------------------------------------------------
