import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import csv

path = "http://api.geonames.org/postalCodeSearch?"
parameters1 = {"postalcode": 10003, "country": "US", "username":  "emililyyyyyyy"}
response1 = requests.get(path, params = parameters1 )
soup1 = BeautifulSoup(response1.content, 'html.parser')

print(soup1)
