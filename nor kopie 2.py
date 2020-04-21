import requests
from bs4 import BeautifulSoup
from time import sleep

base_url = 'https://raw.githubusercontent.com/oliverwk/oliverwk.github.io/master/tatiana%20art/91018230_151840196296351_1894637158564459764_n'

all_urls = list()

def generate_urls():
    for i in range(1,11):
        all_urls.append(base_url + str(i) + str(".jpg"))

def scrape(url):
    res = requests.get(url)
    print(res.status_code, res.url)

generate_urls()
for url in all_urls:
    scrape(url)
