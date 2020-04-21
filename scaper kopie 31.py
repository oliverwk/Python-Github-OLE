import time
import requests
from bs4 import BeautifulSoup

input = raw_input("Voer een zoek term in: ")

URL = "https://www.amazon.nl/s?k=usg" + input

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL + str(input), headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#naam = soup.find(id="product-title").get_text()
#name = soup.find_all("input", text="135")#.get_text()

prijs = soup.find("span", class_="a-price-whole").get_text()

print("De prijs is:")
time.sleep(1)
print(prijs.strip())
