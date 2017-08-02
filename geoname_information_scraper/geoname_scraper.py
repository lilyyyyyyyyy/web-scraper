import requests
from bs4 import BeautifulSoup
import pandas as pd

acronym_of_state_name = input("Please enter the acronym of state you are interested in: ")

page = requests.get("http://www.geonames.org/postalcode-search.html?q=&country=US&adminCode1={0}".format(acronym_of_state_name))
soup = BeautifulSoup(page.content, 'html.parser')

city = soup.find(class_="restable")

lon_and_lat = [ll.get_text() for ll in city.select("a small")]
zipcode = [zp.get_text() for zp in city.select("tr td")][2::9]
city_name = [city.get_text() for city in city.select("tr td")][1::9]

STATE = pd.DataFrame({
            "city in NY": city_name,
            "zip code": zipcode,
            "longitude and latitude": lon_and_lat})

print(STATE)

# STATE.to_csv('NY.csv', index=False)

identifier = input("Please enter the ZIP code: " )

lon_lat = STATE.loc[STATE['zip code'] == identifier]
lon = list(lon_lat["longitude and latitude"])[0]
a, b = lon.split("/")

url = "http://forecast.weather.gov/MapClick.php?lat={0}&lon={1}".format(a,b)
print(url)
