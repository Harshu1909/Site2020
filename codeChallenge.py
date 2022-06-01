# Harsh S Patel
# Code Challenge from "Site 2020"
# Date: 31-May-2022 at 11:30 PM
# Python Version 3.8.2 64bit

import requests
from datetime import datetime

#Weather Report including Rainfall
def weatherDetail():

    #Weather Date from "Visualcrossing.com"
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Halifax?unitGroup=metric&include=current&key=5Y7ESSHU7WLGVJMUHZZA2U2Y2&contentType=json"
    
    #Fetch data to JSON, Review the data from POSTMAN
    response = requests.get(BASE_URL).json() 

    #Print Data
    print("---------------- Weather Report ---------------")
    print("Location:"+str(response["address"]))
    print("Date/Time:"+str(response["days"][0]["datetime"]))
    print("Tempreture:"+str(response["days"][0]["temp"])+"C")
    print("Rainfall:"+str(response["days"][0]["precip"]))
    print("Condition:"+str(response["days"][1]["conditions"]))
    print("Description:"+str(response["days"][1]["description"]))
    print(" ")
    print(" ")

#Crypto function resulting Bitcoin and Ethereum current price in USD
def trackCrypto():

    URL = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD"

    #Response in JSON
    response = requests.get(URL).json()
    priceBit = response["BTC"]["USD"]
    priceEth = response["ETH"]["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    #Print Data
    print(" ")
    print(" ")
    print("--------------- Crypto Report ---------------")
    print("Bitcoin:" +str(priceBit)+ " USD")
    print("Ethereum:" +str(priceEth)+ " USD")
    print("Time:" +str(time))
    print(" ")
    print(" ")


#Call the function
trackCrypto()
weatherDetail()