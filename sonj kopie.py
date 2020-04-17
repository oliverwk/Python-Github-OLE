import os
#os.system('clear')
import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers )
soup = BeautifulSoup(page.content, 'html.parser')
prijs = soup.find("span", itemprop="price").get_text()
naam = soup.find("span", itemprop="name").get_text()



prfx = "https://www.na-kd.com"
for lnkt in soup.find_all('a'):
    lnks = lnkt.get('herf')
    if lnks is not None:
       herf = str(prfx) + links
       print(herf)
       NA1KD = open("NA1KD.txt","w")
       NA1KD.writelines(linker)
       NA1KD.close()



NAKD = open("NAKD.txt","w")
NAKD.write(prijs)
NAKD.close()


pref = "https://www.na-kd.com/nl/lingerie/onderbroeken/"


print("")
print("\nDe {n} is het goedkoopste.".format(n=naam))
print("")
txt = "De prijs is{} euro"
print(txt.format(prijs))
print("")

urls = str(pref) + naam.replace(" ", "-")
urlw = urls + str("-wit")
urlz = urls + str("-zwart")
resw = requests.get(urlw, headers=headers)
resz = requests.get(urlz, headers=headers)
soupz = BeautifulSoup(resz.content, 'html.parser')
soupw = BeautifulSoup(resw.content, 'html.parser')
urlg = urls + str("-groen")
resg = requests.get(urlg, headers=headers)
soupg = BeautifulSoup(resg.content, 'html.parser')
urly = urls + str("-geel")
resy = requests.get(urly, headers=headers)
soupy = BeautifulSoup(resy.content, 'html.parser')

def kleuren():
    NAKD_url = open("NAKD_url.txt","w")
    if resw.content == 'Bad Request':
       print("geen witte gevonden")
    else:
        print(urlw)
        NAKD_url.write(urlw)

    if resz.content == 'Bad Request':
       print("geen zwarten gevonden")
    else:
        print(urlz)
        NAKD_url.write("\n{u}".format(u=urlz))
    if resy.content == 'Bad Request':
        print("geen geelen gevonden")
    else:
        print(urly)
        NAKD_url.write("\n{u}".format(u=urly))

    if resg.content == 'Bad Request':
       print("geen groenen gevonden")
    else:
        print(urlg)
        NAKD_url.write("\n{u}".format(u=urlg))


    NAKD_url.close()

kleuren()

a = prijs
f = open("NAKD.txt", "r")
b = f.readline()
f.close()
#print("print de link er naar toe {n}".format(n=link))

if b > a:
  print("\nHet is goedkoper geworden.")
elif a == b:
  print("\nHet is de zelfde prijs.")
else:
  print("\nHet is duurder geworden.")

v = open("NAKD_url.txt", "r")
ot = v.readline()
pow = v.readline()
bo = v.readline()
v.close()

data = {}
data['prijs'] = prijs
data['naam'] = naam
data['url'] = ot

json_data = json.dumps(data)
print("")
NAKD = open("NAKD.json","w")
NAKD.write(json_data)
NAKD.close()
print(json_data)
