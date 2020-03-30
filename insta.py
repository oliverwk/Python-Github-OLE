URL = raw_input("Voer het Instagram url in: ")

import wget
import requests
from bs4 import BeautifulSoup
TK_SILENCE_DEPRECATION=1

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

description = soup.find("meta",  property="og:image")

#test link https://www.instagram.com/p/B-PZFIvAT7a/

local_image_filename = wget.download(description["content"])

print("\nklaar ja kan nu naar de map OLE gaan")
