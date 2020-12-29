import requests
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, time, date
import time
from dateutil import parser, rrule

# define function to get data
def getWeatherData(city, station, month, year):
    url = "https://www.wunderground.com/history/monthly/ke/{city}/{station}/date/{year}-{month}"
    full_url = url.format(city = city, station = station, month = month, year = year)

    # request data
    response = requests.get(full_url, 
                            headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
    data = response.text

    data = data.replace("<br>","")
    print(data)

    # get dataframe
    try:
        dataframe = pd.read_csv(io.StringIO(data), index_col=False)
        dataframe['city'] = city
        dataframe['station'] = station
    except Exception as e:
        print("Issue with date: {}-{} for station {}".format(month,year, station))
        return None

    return dataframe

# test mombasa
df = getWeatherData("mombasa","HKMO",6,2019)
df.to_csv("test_data.csv",index=False)