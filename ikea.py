#!/usr/bin/python
import os
os.system('clear')
import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.ikea.com/nl/nl/p/fyrtur-verduisterend-rolgordijn-koordloos-op-batterijen-grijs-90408170/"


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers )
soup = BeautifulSoup(page.content, 'html.parser')

naam = soup.find("meta",  property="og:title")
description = soup.find("meta",  property="og:description")
url = soup.find("meta",  property="og:image")
prijs = soup.find("span",  class_="range-revamp-price__integer").get_text()


import bitly_api

BITLY_ACCESS_TOKEN ="168b3257210b004d16e1d0eed5097e4fd58e7363"

b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

response = b.shorten(url["content"])



print(naam["content"])
print("")
print(description["content"])
print("")
print(response["url"])
print("")
prijzen = prijs + str(" Euro.")
print(prijzen)



fields = ['naam', 'prijs', 'beschrijving', 'url']

# data rows of csv file
rows = [ [naam["content"], prijzen, description["content"], response["url"]]]

# writing to csv file
with open("ikea.csv", 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    # writing the fields
    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(rows)

print("csv bestand gemaakt.")
