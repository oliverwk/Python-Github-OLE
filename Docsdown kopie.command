#!/usr/bin/env python
import os
os. system('echo -n -e "\033]0;Instagram downloader\007"')
os. system('clear')
print("Downloading ...")
import requests
from bs4 import BeautifulSoup
print("")


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
URL = "https://docs.google.com/document/d/129SWfi_sF3MvKyce4nBSdNU4l5gCDRXfemz8Ycbw-eU/edit?usp=sharing"
page_goole = requests.get(URL, headers=headers)
soup = BeautifulSoup(page_goole.content, 'html.parser')
description = soup.find("meta",  property="og:description")
import sys


os.system('python /Users/MWK/Desktop/pi.py {}'.format(description["content"]))
