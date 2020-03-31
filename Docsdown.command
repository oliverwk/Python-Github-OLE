#!/usr/bin/env python
import os
os. system('echo -n -e "\033]0;Instagram downloader\007"')
os. system('clear')
print("Download docs begint")
import requests
from bs4 import BeautifulSoup
print("")


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
URL = "https://docs.google.com/document/d/129SWfi_sF3MvKyce4nBSdNU4l5gCDRXfemz8Ycbw-eU/edit?usp=sharing"
page_goole = requests.get(URL, headers=headers)
soup = BeautifulSoup(page_goole.content, 'html.parser')
description = soup.find("meta",  property="og:description")


import urllib2
fp = urllib2.urlopen(description["content"])
print(fp.geturl())
#print(description["content"] if description else "Er is geen tekst.")


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
#test link https://www.instagram.com/p/B-PZFIvAT7a/

base_dir = os.path.dirname(os.path.abspath(__file__))
target = "tatiana_art"
prefix_list = ["91018230_151840196296351_1894637158564459764_n"]

for prefix in prefix_list:
    path = os.path.join(base_dir, "tatiana")
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.isdir(path):
        exit()


#test link googe docs https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing
import wget
local_image_filename = wget.download(image["content"], out=path)
print("")
print("\nklaar ja kan nu naar de tatiana map gaan")
