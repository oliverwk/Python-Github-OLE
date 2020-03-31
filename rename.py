import os
import requests
from bs4 import BeautifulSoup
count = 0
while (count < 20):
    count = count + 1

urlinsta = sys.argv[1]
page1 = requests.get(urlinsta, headers=headers)
soup1 = BeautifulSoup(page1.content, 'html.parser')
naamfile = soup1.find("title")
print(naamfile)

x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))+1
print(x)
MWK = "/Users/MWK/tatiana_art_{x}.jpg".format(x=x)
os.rename(r"/Users/MWK/Desktop/tatiana/91352641_214138349664039_3803035465347445593_n.jpg",r"{new}" .format(new=MWK))


import shutil
shutil.move(MWK, '/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x))
