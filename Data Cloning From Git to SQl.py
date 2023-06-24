

#before import Ensure to install required libraries
#import required libraries to be imported

import pandas as pd         
import streamlit as st
import sqlite3
import mysql.connector
import os      #To use my system dir
import json
import subprocess
import requests



#------------------------------------------------------Cloning & Storing in local Dir-------------------------------------------------------

#Specify the GitHub repository URL
response = requests.get('https://api.github.com/repos/PhonePe/pulse')
repo = response.json()
clone_url = repo['clone_url']

#Specify the local directory path
clone_dir = "E:/phonepe_pulse"

# Clone the repository to the specified local directory
subprocess.run(["git", "clone", clone_url, clone_dir], check=True)

#Contents

#1 --> aggregated_transaction
#2 --> aggregated_user
#3 --> map_transaction
#4 --> map_user
#5 --> top_transaction
#6 --> top_user

# <---------------------------------------------------------------------------DATA PROCESSING------------------------------------------------------------------------------------->


# <-----------------------------------------------------Extracting the data to create the dataframe as agg <-----> transaction---------------------------------------------------->


#This is to direct the path to get the data as states
path_1 = "E:/phonepe_pulse/data/aggregated/transaction/country/india/state/"

Agg_tran_state_list = os.listdir(path_1)    

Agg_tra = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}   #Empty list to append the data

for i in Agg_tran_state_list:
    p_i = path_1 + i + "/"
    Agg_yr = os.listdir(p_i)


    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            A = json.load(Data)

            for l in A['data']['transactionData']:
                      Name = l['name']
                      count = l['paymentInstruments'][0]['count']
                      amount = l['paymentInstruments'][0]['amount']
                      Agg_tra['State'].append(i)
                      Agg_tra['Year'].append(j)
                      Agg_tra['Quarter'].append(int(k.strip('.json')))
                      Agg_tra['Transaction_type'].append(Name)
                      Agg_tra['Transaction_count'].append(count)
                      Agg_tra['Transaction_amount'].append(amount)

df_aggregated_transaction = pd.DataFrame(Agg_tra)


# <-----------------------------------------------------Extracting the data to create the dataframe as agg <-----> User--------------------------------------------------------->

#2


path_2 = "E:/phonepe_pulse/data/aggregated/user/country/india/state/"
Agg_user_state_list = os.listdir(path_2)
Agg_user = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'User_Count': [], 'User_Percentage': []} #Empty list to append the data

for i in Agg_user_state_list:
    p_i = path_2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            B = json.load(Data)

            try:
                for l in B["data"]["usersByDevice"]:
                    brand_name = l["brand"]
                    count_ = l["count"]
                    ALL_percentage = l["percentage"]
                    Agg_user["State"].append(i)
                    Agg_user["Year"].append(j)
                    Agg_user["Quarter"].append(int(k.strip('.json')))
                    Agg_user["Brands"].append(brand_name)
                    Agg_user["User_Count"].append(count_)
                    Agg_user["User_Percentage"].append(ALL_percentage*100)
            except:
                pass

df_aggregated_user = pd.DataFrame(Agg_user)


# <-----------------------------------------------------Extracting the data to create the dataframe as Map <-----> Transaction----------------------------------------------------------># TO GET THE DATA-FRAME OF MAP <--> TRANSACTION



# 3

path_3 = "E:/phonepe_pulse/data/map/transaction/hover/country/india/state/"
map_tra_state_list = os.listdir(path_3)
map_tra = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_Count': [], 'Transaction_Amount': []}  #Empty list to append the data

for i in map_tra_state_list:
    p_i = path_3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            C = json.load(Data)

            for l in C["data"]["hoverDataList"]:
                District = l["name"]
                count = l["metric"][0]["count"]
                amount = l["metric"][0]["amount"]
                map_tra['State'].append(i)
                map_tra['Year'].append(j)
                map_tra['Quarter'].append(int(k.strip('.json')))
                map_tra["District"].append(District)
                map_tra["Transaction_Count"].append(count)
                map_tra["Transaction_Amount"].append(amount)

df_map_transaction = pd.DataFrame(map_tra)


# <-----------------------------------------------------Extracting the data to create the dataframe as Map <-----> User------------------------------------------------------------->


# 4

path_4 = "E:/phonepe_pulse/data/map/user/hover/country/india/state/"
map_user_state_list = os.listdir(path_4)
map_user = {"State": [], "Year": [], "Quarter": [], "District": [], "Registered_User": []} #Empty list to append the data

for i in map_user_state_list:
    p_i = path_4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            for l in D["data"]["hoverData"].items():
                district = l[0]
                registereduser = l[1]["registeredUsers"]
                map_user['State'].append(i)
                map_user['Year'].append(j)
                map_user['Quarter'].append(int(k.strip('.json')))
                map_user["District"].append(district)
                map_user["Registered_User"].append(registereduser)

df_map_user = pd.DataFrame(map_user)


# <-----------------------------------------------------Extracting the data to create the dataframe as Top <-----> Transaction------------------------------------------------------------->


# 5
path_5 = "E:/phonepe_pulse/data/top/transaction/country/india/state/"
top_tra_state_list = os.listdir(path_5)
top_tra = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Transaction_count': [], 'Transaction_amount': []} #Empty list to append the data

for i in top_tra_state_list:
    p_i = path_5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            E = json.load(Data)

            for l in E['data']['pincodes']:
                Name = l['entityName']
                count = l['metric']['count']
                amount = l['metric']['amount']
                top_tra['State'].append(i)
                top_tra['Year'].append(j)
                top_tra['Quarter'].append(int(k.strip('.json')))
                top_tra['District_Pincode'].append(Name)
                top_tra['Transaction_count'].append(count)
                top_tra['Transaction_amount'].append(amount)

df_top_transaction = pd.DataFrame(top_tra)


# <-----------------------------------------------------Extracting the data to create the dataframe as Top <-----> User---------------------------------------------------------------->


# 6

path_6 = "E:/phonepe_pulse/data/top/user/country/india/state/"
top_user_state_list = os.listdir(path_6)
top_user = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Registered_User': []}   #Empty list to append the data

for i in top_user_state_list:
    p_i = path_6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            F = json.load(Data)

            for l in F['data']['pincodes']:
                Name = l['name']
                registeredUser = l['registeredUsers']
                top_user['State'].append(i)
                top_user['Year'].append(j)
                top_user['Quarter'].append(int(k.strip('.json')))
                top_user['District_Pincode'].append(Name)
                top_user['Registered_User'].append(registeredUser)

df_top_user = pd.DataFrame(top_user)



# checking for missing and null values:

#df_aggregated_transaction.info()
#df_aggregated_user.info()
#df_map_transaction.info()
#df_map_user.info()
#df_top_transaction.info()
#df_top_user.info()

# creating connection with SQL server:
con = sqlite3.connect("phonepe pulse.db")
cursor = con.cursor()

# Inserting each DF to SQL server:

df_aggregated_transaction.to_sql('aggregated_transaction', con, if_exists='replace')
df_aggregated_user.to_sql('aggregated_user', con, if_exists='replace')
df_map_transaction.to_sql('map_transaction', con, if_exists='replace')
df_map_user.to_sql('map_user', con, if_exists='replace')
df_top_transaction.to_sql('top_transaction', con, if_exists='replace')
df_top_user.to_sql('top_user', con, if_exists='replace')


#closing the sql connection
cursor.close()
con.close()


print('Thanks')