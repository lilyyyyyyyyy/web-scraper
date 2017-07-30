
import requests
from bs4 import BeautifulSoup
path = "http://forecast.weather.gov/MapClick.php?lat=32.7157&lon=-117.1617"
page = requests.get(path)

soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")

period_tags = [pt.get_text() for pt in seven_day.select(".tombstone-container .period-name")]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(period_tags)
print(short_descs)
print(temps)
print(descs)
