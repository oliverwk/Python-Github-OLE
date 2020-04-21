import time
import requests
from bs4 import BeautifulSoup

URL = "http://localhost/kopie.html"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

prijs = soup.find_all('p')

print(prijs)

time.sleep(1)

print(soup.find(id="link"))
