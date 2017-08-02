import requests
from bs4 import BeautifulSoup
import pandas as pd

page_NY_again = requests.get("http://www.geonames.org/postalcode-search.html?q=&country=US&adminCode1=NY")
soup = BeautifulSoup(page_NY_again.content, 'html.parser')

state_raw = soup.find_all('select')[1]

state_name = [sn.get_text() for sn in state_raw.select('option')]

acronym_state_name = [ac["value"] for ac in state_raw.select('option')]

state = pd.DataFrame({
        "acronym": acronym_state_name, "state": state_name,
        })

path_1 = "/Users/lily/Desktop/web-scraper/data/state_list.csv"
state.to_csv(path_1, index=False)



# acronym_state = [ac.get_text() for ac in state_name.select("a small")]
# zipcode_NY = [zp.get_text() for zp in city_NY.select("tr td")][2::9]
