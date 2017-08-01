import requests
from bs4 import BeautifulSoup

page_NY = requests.get("http://www.geonames.org/postal-codes/US/NY/new-york.html")
soup = BeautifulSoup(page_NY.content, 'html.parser')
print(soup)
