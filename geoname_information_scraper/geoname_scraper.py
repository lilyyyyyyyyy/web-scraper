import requests
from bs4 import BeautifulSoup

page_NY = requests.get("http://www.geonames.org/postal-codes/US/NY/new-york.html")
soup = BeautifulSoup(page_NY.content, 'html.parser')
print(soup)

city_NY = soup.find(class_="restable")

lon_and_lat_NY = [ll.get_text() for ll in city_NY.select("a small")]
zipcode_NY = [zp.get_text() for zp in city_NY.select("tr td")][2::9]
city_name_NY = [city.get_text() for city in city_NY.select("tr td")][1::9]

print(lon_and_lat_NY)
print(zipcode_NY)
print(city_name_NY)
