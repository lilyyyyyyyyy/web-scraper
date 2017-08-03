import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import csv

menu = """
Step 1: Please create an account on http://www.geonames.org/
Step 2: Please go to http://www.geonames.org/manageaccount and enable your account for free web services
Step 3: Please enter your username:
"""
postalcode = input("Please enter the ZIP code of the city your want to know: ")

username = input(menu)

path = "http://api.geonames.org/postalCodeSearch?"
parameters1 = {"postalcode": postalcode, "country": "US", "username":  username, "type": "json"}
response1 = requests.get(path, params = parameters1 )
data1 = response1.json()

lat = data1["postalCodes"][0]["lat"]
lon = data1["postalCodes"][0]["lng"]

url = "https://api.weather.gov/points/{0},{1}/forecast" .format(lat, lon)

response2 = requests.get(url)
data = response2.json()
data_extract = data["properties"]["periods"]

period_tags = [x['name'] for x in data_extract]
short_descs = [x['shortForecast'] for x in data_extract]
descs = [x['detailedForecast'] for x in data_extract]
temp = [x['temperature'] for x in data_extract]

weather = pd.DataFrame({
        "period": period_tags,
        "short_desc": short_descs,
        "temp": temp,
        "desc":descs
    })

print(weather)
