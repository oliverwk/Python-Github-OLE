import os
import sys
import requests
from bs4 import BeautifulSoup


print("hello world!")
urlinsta = 'https://scontent-amt2-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/70932798_1072836726441605_527163624535307822_n.jpg?_nc_ht=scontent-amt2-1.cdninstagram.com&_nc_cat=105&_nc_ohc=9kcsuUtkPyoAX-imbZK&oh=684aac7dc619697f0fd211dce53c51c9&oe=5EAB70B6'
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
page = requests.get(urlinsta, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
naamfile = soup.find("title")

print(naamfile)

x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))+1
print(x)

MWK = "/Users/MWK/tatiana_art_{n}.jpg".format(n=x)

import shutil
shutil.move('/Users/MWK/70932798_1072836726441605_527163624535307822_n.jpg', MWK)

os.rename(r"/Users/MWK/tatiana/70932798_1072836726441605_527163624535307822_n.jpg ",r"{n}".format(n=MWK))
