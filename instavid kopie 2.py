URL = "https://docs.google.com/document/d/129SWfi_sF3MvKyce4nBSdNU4l5gCDRXfemz8Ycbw-eU/edit?usp=sharing"

import requests
import wget
from bs4 import BeautifulSoup
TK_SILENCE_DEPRECATION=1
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page_goole = requests.get(URL, headers=headers)

soup = BeautifulSoup(page_goole.content, 'html.parser')

description = soup.find("meta",  property="og:description")

print(description["content"] if description else "Er is geen tekst.")

URLINSTA = description["content"]

page = requests.get(URLINSTA, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

image = soup.find("meta",  property="og:image")

print(image["content"] if image else "Er is geen afbeelding.")

#test link https://www.instagram.com/p/B-PZFIvAT7a/

#test link googe docs https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing

local_image_filename = wget.download(image["content"])

print("\nklaar ja kan nu naar de map OLE gaan")
