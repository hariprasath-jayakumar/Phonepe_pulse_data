
#Importing Required Lib

import sqlite3

import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu 

import seaborn as sns

import plotly as plt
import plotly.express as px

from PIL import Image


# creating connection with SQL server:
connection = sqlite3.connect("phonepe pulse.db")
cursor = connection.cursor()


#---------------------------------------------------------PAGE CONFIGURATION AND LAYOUT-------------------------------------------------

st.set_page_config(
     page_title="PhonePe Data Visualization",
     page_icon="chart_with_upwards_trend",
     layout="wide",
     initial_sidebar_state="expanded")

# Hide the streamlit app content
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """

st.markdown(hide_default_format, unsafe_allow_html=True)
#-----------------------------------------------------------------Webpage Title----------------------------------------------------

st.title("Phonepe Pulse Data Visualization")

# ------------------------------------------------------------SETTING CONTENTS PAGE-------------------------------------------------------

SELECT = option_menu(
    menu_title=None,
    options=["About",  "Home", "Basic insights","Trust & Protection"],
    icons=["bar-chart","house", "toggles", "key"],
    default_index=1,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white", "size": "cover"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}
    })

#------------------------------------------------------------------BASIC INSIGHTS------------------------------------------------------------

if SELECT == "Basic insights":
    st.subheader("Here we see some basic insights about the data")
    options = ["--select--",
                "Top 10 states based on amount of transaction",
               "Least 10 states based on amount of transaction",
               "Top 10 registered state & Registered user Brand",
               "Top 10 Users brand with user stats",
               "Least 10 Users brand with user stats",
               "Top 10 transactions_type based on states and transaction_amount",
               "Least 10 transactions_type based on states and transaction_amount"]
    
    
    select = st.selectbox("Select the option", options)

#---------------------------------------------------Top 10 states based on amount of transaction---------------------------------------------------

    if select == "Top 10 states based on amount of transaction":
        cursor.execute(
      "SELECT DISTINCT State,Transaction_amount, SUM(Transaction_Amount) as Total_Transaction  FROM top_transaction  GROUP BY State ORDER BY transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transaction_amount', 'Total_Transaction'])
        col1, col2 = st.columns(2)
        with col1:
          st.write(df)
        with col2:
           st.title("Top 10 states based on amount of transaction")
           fig = px.bar(df, x="State", y="Transaction_amount")
           st.plotly_chart(fig, theme=None, use_container_width=True)

#------------------------------------------------------Least 10 states based on amount of transaction----------------------------------------------

    elif select == "Least 10 states based on amount of transaction":
         cursor.execute(
      "SELECT DISTINCT State,Transaction_amount, SUM(Transaction_Amount) as Total_Transaction  FROM top_transaction  GROUP BY State ORDER BY transaction_amount ASC LIMIT 10");
         df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transaction_amount','Total_Transaction'])
         col1, col2 = st.columns(2)
         with col1:
             st.write(df)
         with col2:
             st.title("Least 10 State based amount of Transaction")
             fig = px.bar(df, x= 'State', y = 'Transaction_amount')
             st.plotly_chart(fig, theme = None) 
     
#-----------------------------------------------------Top 10 registered state & Registered user Brand----------------------------------------------

    elif select == "Top 10 registered state & Registered user Brand":
          cursor.execute(
     "SELECT DISTINCT State, Brands, SUM ( User_Count) as User_Count, User_Percentage FROM aggregated_user GROUP BY State ORDER BY User_Count DESC LIMIT 10");
          df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Brands', 'User_Count', 'User_Percentage'])
          col1, col2 = st.columns(2)
          with col1:
               st.write(df)
          with col2:
               st.title("Top registered state & Registered user Brand")
               fig = px.bar(df, x="State", y="User_Percentage")
               st.plotly_chart(fig, theme="streamlit")

#---------------------------------------------------------Top 10 Users brand with user stats---------------------------------------------------

    elif select == "Top 10 Users brand with user stats":
          cursor.execute( " SELECT DISTINCT State, Brands, SUM(User_Count) User_Count, User_Percentage FROM aggregated_user GROUP BY Brands, State ORDER BY User_Count DESC LIMIT 10");
          df = pd.DataFrame(cursor.fetchall(), columns = ['State', 'Brands', 'User_Count', 'User_Percentage'])
          col1, col2 = st.columns(2)
          with col1:
               st.write(df)
          with col2:
               st.title("Top 10 Users brand with user stats")
               fig = px.bar(df, x='Brands', y='User_Count')
               st.plotly_chart(fig, theme  = 'streamlit')


#---------------------------------------------------------Least 10 Users brand with user stats---------------------------------------------------

    elif select == "Least 10 Users brand with user stats":
          cursor.execute( " SELECT DISTINCT State, Brands, SUM(User_Count) User_Count, User_Percentage FROM aggregated_user GROUP BY Brands, State ORDER BY User_Count ASC LIMIT 10");
          df = pd.DataFrame(cursor.fetchall(), columns = ['State', 'Brands', 'User_Count', 'User_Percentage'])
          col1, col2 = st.columns(2)
          with col1:
               st.write(df)
          with col2:
               st.title("Least 10 Users brand with user stats")
               fig = px.bar(df, x='Brands', y='User_Count')
               st.plotly_chart(fig, theme  = 'streamlit')


 #--------------------------------------------Top 10 Transactions_type based on states and transaction_amount--------------------------------------

    elif select == "Top 10 transactions_type based on states and transaction_amount":
         cursor.execute(
              "SELECT DISTINCT State, Transaction_type, Transaction_count, Transaction_amount FROM aggregated_transaction GROUP BY State, Transaction_type ORDER BY Transaction_amount DESC LIMIT 10");
         df = pd.DataFrame(cursor.fetchall(), columns = ['State', 'Transaction_type', 'Transaction_count','Transaction_amount'])
         col1, col2 = st.columns(2)
         with col1:
             st.write(df)
         with col2:
             st.title("Top 10 transactions_type based on states and transaction_amount")
             fig = px.bar(df, x= 'State', y = 'Transaction_amount')
             st.plotly_chart(fig, theme  = 'streamlit')

#------------------------------------------Least 10 transactions_type based on states and tranaction_amount

    elif select == "Least 10 transactions_type based on states and transaction_amount":
         cursor.execute(
              "SELECT DISTINCT State, Transaction_type, Transaction_count, Transaction_amount FROM aggregated_transaction GROUP BY State, Transaction_type ORDER BY Transaction_amount ASC LIMIT 10");
         df = pd.DataFrame(cursor.fetchall(), columns = ['State', 'Transaction_type', 'Transaction_count','Transaction_amount'])
         col1, col2 = st.columns(2)
         with col1:
             st.write(df)
         with col2:
             st.title("Least 10 transactions_type based on states and transaction_amount")
             fig = px.bar(df, x= 'State', y = 'Transaction_amount')
             st.plotly_chart(fig, theme  = 'streamlit')


#--------------------------------------------------------------------HOME---------------------------------------------------------------------------

if SELECT == "Home":

     col1,col2= st.columns(2)

     col1.image(Image.open(r"E:\py\Phonepe_project\Phonepe-logo.jpg"),width=700)
     with col1:
               
          st.subheader("PhonePe is a leading digital payment platform widely used in India for seamless transactions and financial services. With a user-friendly interface and extensive network, it allows users to easily send and receive money, pay bills, and make online purchases using UPI, wallets, and cards. PhonePe has gained popularity for its secure transactions, fast processing times, and robust features, making it a preferred choice among millions of users in India. Its widespread acceptance across merchants and e-commerce platforms further enhances its utility and convenience for everyday transaction")
          st.write()         
          st.subheader('To Download the Official Phonepe Application, Click Below')
          st.markdown("Click [here](https://www.phonepe.com/app-download/) to download the application.")

     with col2:
          st.video(r"E:\py\Phonepe_project\Phonepe - Introduction.mp4")

#--------------------------------------------------------------Trust & Protection-------------------------------------------------------------------
if SELECT == 'Trust & Protection':

     st.video(r"E:\py\Phonepe_project\phonepeprotection.mp4")
     st.subheader("PhonePe's seamless user experience has also contributed to its trustworthiness. The platform offers a user-friendly interface, making it easy for people to navigate and carry out transactions. Whether it's sending money to friends and family, paying bills, or making online purchases, PhonePe provides a smooth and hassle-free experience. The reliability and efficiency of the platform have earned the trust of citizens who rely on it for their daily financial transactions.")
     st.subheader("Top Transaction type with Transactions")
     cursor.execute ("""
     SELECT Transaction_type, SUM(Transaction_Amount) as Total_Transaction, SUM (Transaction_count) as Total_Transaction
     FROM aggregated_transaction 
     GROUP BY Transaction_type
     ORDER BY Transaction_amount DESC
     LIMIT 3
     """);
     df = pd.DataFrame (cursor.fetchall(), columns= ['Transaction_type','Transaction_amount','Transaction_count'])
     col1, col2 = st.columns(2)
     with col1:
          st.write(df)
     with col2:
          fig = px.bar(df, x= 'Transaction_amount', y = 'Transaction_type')
          st.plotly_chart(fig, theme  = 'streamlit') 

     
     st.subheader('Least Transaction type with Transactions')
     cursor.execute ("""
     SELECT Transaction_type, SUM(Transaction_Amount) as Total_Transaction, SUM (Transaction_count) as Total_Transaction
     FROM aggregated_transaction 
     GROUP BY Transaction_type
     ORDER BY Transaction_amount ASC
     LIMIT 3
     """);
     df = pd.DataFrame(cursor.fetchall(), columns = ['Transaction_type','Transaction_amount','Transaction_count'])
     col1, col2 = st.columns(2)

     cursor.execute ("""
     SELECT State, Transaction_type, SUM(Transaction_Amount) as Total_Transaction, SUM (Transaction_count) as Total_Transaction
     FROM aggregated_transaction 
     GROUP BY Transaction_type
     ORDER BY Transaction_amount ASC
     LIMIT 3
     """);
     df = pd.DataFrame(cursor.fetchall(), columns = ['State','Transaction_type','Transaction_amount','Transaction_count'])
     
     import matplotlib.pyplot as plt
     import numpy as np 

     with col1:
          st.write(df)
     with col2:
          fig = px.bar(df,x='Transaction_amount',y= 'Transaction_type')
          st.plotly_chart(fig,theme='streamlit')
     
#-------------------------------------------------------------------About---------------------------------------------------------------------------
 
if SELECT ==  'About':
     
     col1,col2 = st.columns(2)
     with col1:
          st.video(r"E:\py\Phonepe_project\about.mp4")
     with col2:    
          st.header('About') 
          st.subheader('PhonePe is a trusted digital payment platform in India, revolutionizing financial transactions. With advanced security measures, seamless user experience, and strong partnerships, PhonePe ensures safe and convenient payments. Its widespread acceptance in various sectors and reliable customer support make it a preferred choice. PhonePe empowers millions, providing secure and efficient digital transactions across the country.')
     col1, col2 = st.columns(2)
     with col1:
          st.header('UPI')
          st.subheader("PhonePe, a leading digital payment platform, has witnessed exponential usage in India. With its user-friendly interface, users can effortlessly send money, pay bills, and make online purchases. Its secure and reliable features have instilled confidence in millions of users, leading to widespread adoption. PhonePe's seamless integration with banks and merchants has made it a convenient choice for diverse transactions, making it an indispensable tool for modern-day financial management")
     with col2:
          st.video(r"E:\py\phonepe_project\upi.mp4")             

