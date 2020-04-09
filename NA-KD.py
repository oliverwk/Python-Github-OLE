import os
os.system('clear')
import requests
from bs4 import BeautifulSoup
import json

#URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"
#URL = "https://www.na-kd.com/nl/lingerie/bodys?sortBy=price&count=18&p_categories=c_1-33036_nl-nl"
URL = "https://www.na-kd.com/nl/lingerie/bhs?sortBy=price&count=18&p_categories=c_1-32923_nl-nl"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers )
soup = BeautifulSoup(page.content, 'html.parser')
prijs = soup.find("span", itemprop="price").get_text()
naam = soup.find("span", itemprop="name").get_text()



prfx = "https://www.na-kd.com"
"""
for lnkt in soup.find_all('img'):
    lnks = lnkt.get('alt')
    if lnks is not None:
       herf = str(prfx) + links
       print(herf)
       NA1KD = open("NA1KD.txt","w")
       NA1KD.writelines(linker)
       NA1KD.close()
"""


print("\nDe {n} is het goedkoopste.".format(n=naam))
print("")
txt = "De prijs is{} euro"
print(txt.format(prijs))
print("")

pref = "https://www.na-kd.com/nl/lingerie/onderbroeken/"



if "Body" in naam:
   pref = "https://www.na-kd.com/nl/lingerie/bodys/"
   print("Het is een body.")


def bhs():
   if "Thong" in naam:
    pref = str(pref) + str("strings/")
    print("Het is een string")

   if "hipster" in naam:
       pref = str(pref) + str("hipsters/")
       print("Het is een hipsters.")

   if "brazilian" in naam:
       pref = str(pref) + str("brazilians/")
       print("Het is een brazilian.")

   if "Brief" in naam:
       pref = str(pref) + str("slipjes/")
       print("Het is een slipje.")

def onderbroeken():
   if "Thong" in naam:
      pref = str(pref) + str("strings/")
      print("Het is een string.")

   if "hipster" in naam:
       pref = str(pref) + str("hipsters/")
       print("Het is een hipsters.")

   if "brazilian" in naam:
       pref = str(pref) + str("brazilians/")
       print("Het is een brazilian.")

   if "Brief" in naam:
       pref = str(pref) + str("slipjes/")
       print("Het is een slipje.")

if "onderbroeken" in URL:
    print("het is een Onderbroek\n")
    onderbroeken()
elif "bh" in URL:
    print("het is een BH.\n")
    bhs()


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
urlr = urls + str("-rood")
resr = requests.get(urlr, headers=headers)
soupr = BeautifulSoup(resr.content, 'html.parser')


def kleuren():
    kleuren_count = 0
    NAKD_url = open("NAKD_url.txt","w")
    if resw.content == 'Bad Request':
       print("geen witte gevonden")
    else:
        kleuren_count += 1
        print(urlw)
        NAKD_url.write(urlw)

    if resz.content == 'Bad Request':
       print("geen zwarten gevonden")
    else:
        kleuren_count += 1
        print(urlz)
        NAKD_url.write("\n{u}".format(u=urlz))

    if resy.content == 'Bad Request':
        print("geen geelen gevonden")
    else:
        kleuren_count += 1
        print(urly)
        NAKD_url.write("\n{u}".format(u=urly))

    if resg.content == 'Bad Request':
       print("geen groenen gevonden")
    else:
        kleuren_count += 1
        print(urlg)
        NAKD_url.write("\n{u}".format(u=urlg))

    if resr.content == 'Bad Request':
        print("geen rode gevonden")
    else:
        kleuren_count += 1
        print(urlr)
        NAKD_url.write("\n{u}".format(u=urlr))

    NAKD_url.close()
    global kleuren_count
kleuren()

print(kleuren_count)
a = prijs
f = open("NAKD.txt", "r")
b = f.readline()
f.close()


if b > a:
  print("\nHij is goedkoper geworden.")
elif a == b:
  print("\nHij is de zelfde prijs.")
elif a < b:
  print("\nHij is duurder geworden.")

if prijs == b:
    print("")
else:
    NAKD = open("NAKD.txt","w")
    NAKD.write(prijs)
    NAKD.close()


v = open("NAKD_url.txt", "r")
ot = v.readline()
pow = v.readline()
bo = v.readline()
v.close()

data = {}

if ot == "\n":
    data['url'] = pow
else:
    data['url'] = ot

data['prijs'] = prijs
data['naam'] = naam
data['kleuren'] = kleuren_count

json_data = json.dumps(data)

g = open("/Library/WebServer/Documents/NAKD.json", "r")
d = g.readline()
g.close()

if json_data == d:
    print("Geen json printen")
else:
    print("Nieuwe json data.")
    N1AKD = open("/Library/WebServer/Documents/NAKD.json","w")
    N1AKD.write(json_data)
    N1AKD.close()
