
import requests
from bs4 import BeautifulSoup
path = "http://forecast.weather.gov/MapClick.php?lat=32.7157&lon=-117.1617"
page = requests.get(path)
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(id="seven-day-forecast")

print(seven_day.prettify())
