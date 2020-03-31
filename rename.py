import os
import requests
import sys
from bs4 import BeautifulSoup


print("hello world!")
urlinsta = sys.argv[1]
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
page = requests.get(urlinsta, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
naamfile = soup.find("title")

print(naamfile)

x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))+1
print(x)
MWK = "/Users/MWK/tatiana_art_{x}.jpg".format(x=x)
os.rename(r"/Users/MWK/Desktop/tatiana/70932798_1072836726441605_527163624535307822_n.jpg ",r"{new}" .format(new=MWK))


import shutil
shutil.move(MWK, '/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x))
