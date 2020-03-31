
URL = "https://docs.google.com/document/d/129SWfi_sF3MvKyce4nBSdNU4l5gCDRXfemz8Ycbw-eU/edit?usp=sharing"
print("download docs begin")
import requests
from bs4 import BeautifulSoup
import os

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page_goole = requests.get(URL, headers=headers)

soup = BeautifulSoup(page_goole.content, 'html.parser')

description = soup.find("meta",  property="og:description")

print(description["content"] if description else "Er is geen tekst.")



URLINSTA = description["content"]

page = requests.get(URLINSTA, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

image = soup.find("meta",  property="og:image")

title = soup.find("meta",  property="og:title")

print("")
print(image["content"] if title else "Er is geen afbeelding.")
print("")
print("Dit is de beschrijving:")
print(title["content"] if title else "Er is geen beschrijving.")
print("")

base_dir = os.path.dirname(os.path.abspath(__file__))
target = "tatiana_art"
prefix_list = ["91018230_151840196296351_1894637158564459764_n"]

for prefix in prefix_list:
    path = os.path.join(base_dir, "tatiana")
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.isdir(path):
        exit()

import wget
local_image_filename = wget.download(image["content"], out=path)
