import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import csv

path = "http://api.geonames.org/postalCodeSearch?"
parameters1 = {"postalcode": 10003, "country": "US", "username":  "emililyyyyyyy"}
response1 = requests.get(path, params = parameters1 )
soup1 = BeautifulSoup(response1.content, 'html.parser')

lat = [la.get_text() for la in soup1.select("lat")][0]
lon = [l.get_text() for l in soup1.select("lng")][0]

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
