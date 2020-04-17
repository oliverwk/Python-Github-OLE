import os
os.system('clear')
import requests
from bs4 import BeautifulSoup
import csv
import sys
import json

if len(sys.argv) == 1:
   URL = "https://www.hema.nl/dames/lingerie?prefn1=producttype&prefv1=onderbroek&srule=price-low-to-high"
   sort = "onderbroeken"
elif sys.argv[1] == "slip":
    URL = "https://www.hema.nl/dames/lingerie?prefn1=producttype&prefv1=onderbroek&srule=price-low-to-high"
    sort = "onderbroeken"
elif sys.argv[1] == "onderbroek":
    URL = "https://www.hema.nl/dames/lingerie?prefn1=producttype&prefv1=onderbroek&srule=price-low-to-high"
    sort = "onderbroeken"
elif sys.argv[1] == "bh":
    URL = "https://www.hema.nl/dames/lingerie/bh?prefn1=subproducttype&prefv1=padded%20bh%7Csport%20bh%7Ct-shirt%20bh%7Cpush-up%20bh%7Cnon%20padded%20bh%7Cbeugel%20bh%7Cmoulded%20bh%7Csoft%20top%7Ccrop%20top&srule=price-low-to-highr"
    sort = "bh"


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers )
soup = BeautifulSoup(page.content, 'html.parser')
price = soup.find("span", class_="price discounted").get_text()
prijs = price.replace(".-", "")
info = soup.find("div", class_="product js-gtmproduct")
title = soup.find("a", class_="js-product-link").get_text()
description = soup.find("div", class_="short-text").get_text()
print(prijs)



print("De {n} is het goedkoopste.".format(n=title))
print("")
print("De prijs is {}".format(prijs))


descript = description.replace("lees meer", "")
print(str("Dit is de beschrijving: ") + descript)

print(info['data-gtmproduct'])
