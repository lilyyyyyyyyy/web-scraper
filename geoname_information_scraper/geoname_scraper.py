import requests
from bs4 import BeautifulSoup
import pandas as pd

page_NY = requests.get("http://www.geonames.org/postal-codes/US/NY/new-york.html")
soup = BeautifulSoup(page_NY.content, 'html.parser')

city_NY = soup.find(class_="restable")

lon_and_lat_NY = [ll.get_text() for ll in city_NY.select("a small")]
zipcode_NY = [zp.get_text() for zp in city_NY.select("tr td")][2::9]
city_name_NY = [city.get_text() for city in city_NY.select("tr td")][1::9]

NY = pd.DataFrame({
            "city in NY": city_name_NY,
            "zip code": zipcode_NY,
            "longitude and latitude": lon_and_lat_NY})

NY.to_csv('NY.csv', index=False)
identifier = input("Please enter the ZIP code: " )

lon_lat_NY = NY.loc[NY['zip code'] == identifier]
lon = list(lon_lat_NY["longitude and latitude"])[0]
a, b = lon.split("/")

url = "http://forecast.weather.gov/MapClick.php?lat={0}&lon={1}".format(a,b)
print(url)
