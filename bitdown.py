print("Downloading ...")
import requests
from bs4 import BeautifulSoup


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
URL = "https://docs.google.com/document/d/129SWfi_sF3MvKyce4nBSdNU4l5gCDRXfemz8Ycbw-eU/edit?usp=sharing"
page_goole = requests.get(URL, headers=headers)
soup = BeautifulSoup(page_goole.content, 'html.parser')
description = soup.find("meta",  property="og:description")

print("writing")

Tatianafile = open("/Users/MWK/Desktop/tatiana_down.txt","w")
Tatianafile.writelines(description["content"])
Tatianafile.close() #to change file access modes
print("klaar")


file1 = open("/Users/MWK/Desktop/tatiana_down.txt","r+")
print "Output of Read function is "
print file1.read()
file1.close()
