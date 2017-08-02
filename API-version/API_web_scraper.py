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

print(url)
