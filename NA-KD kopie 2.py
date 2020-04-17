import os
os.system('clear')
import requests
from bs4 import BeautifulSoup

#input = raw_input("Voer een zoek term in: ")
#URL = "https://www.na-kd.com/nl/lingerie"

URL = "https://www.na-kd.com/nl/lingerie?sortBy=price&count=18&p_categories=c_1-32922_nl-nl"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers )

soup = BeautifulSoup(page.content, 'html.parser')
count = 0
titel = soup.find("title").get_text()
fruits = ["1", "2", "3", "4", "5", "6"]
for x in fruits:
  count +1
  print(count)
  prijs = soup.find("span", itemprop="price")#.get_text()
  print(prijs)

print("")
print(titel)
print("")
