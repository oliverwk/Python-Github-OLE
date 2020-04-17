reset_data = """{"NA-KD": {
      "bhs": {
        "url": "https://www.na-kd.com/nl/lingerie/bhs/Print-Bra-geel", "naam": "Print Bra", "prijs": " EUR 6.88", "kleuren": 1
            },
      "slip": {
        "url": "https://www.na-kd.com/nl/lingerie/onderbroeken/Basic-Brazilian-Micro-Panty-wit", "naam": "Basic Brazilian Micro Panty", "prijs": " EUR 5.40", "kleuren": 3
            },
    "bodys": {
        "url": "https://www.na-kd.com/nl/lingerie/bodys/Floral-Lace-Cup-Bodysuit-zwart", "naam": "Floral Lace Cup Bodysuit", "prijs": " EUR 17.37", "kleuren": 1
      }
}}"""

import os
os.system('clear')
import requests
from bs4 import BeautifulSoup
import json
import sys



def reset():
    NKD = open("/Library/WebServer/Documents/NAKD.json","w")
    NKD.writelines(reset_data)
    NKD.close()


counters = open("/Users/MWK/Desktop/OLE/.count","r")
counter = counters.readline()
counters.close()


if counter > 2:
    reset()

counts = open(".count","w")
num = int(counter)
num += 1
if num == 2:
    reset()

counts.write('{}'.format(num))
counts.close()


if len(sys.argv) == 1:
   URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"
   sort = "onderbroeken"
elif sys.argv[1] == "slip":
    URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"
    sort = "onderbroeken"
elif sys.argv[1] == "body":
    URL = "https://www.na-kd.com/nl/lingerie/bodys?sortBy=price&count=18&p_categories=c_1-33036_nl-nl"
    sort = "body"
elif sys.argv[1] == "bh":
    URL = "https://www.na-kd.com/nl/lingerie/bhs?sortBy=price&count=18&p_categories=c_1-32923_nl-nl"
    sort = "bh"



#URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"
#URL = "https://www.na-kd.com/nl/lingerie/bodys?sortBy=price&count=18&p_categories=c_1-33036_nl-nl"
#URL = "https://www.na-kd.com/nl/lingerie/bhs?sortBy=price&count=18&p_categories=c_1-32923_nl-nl"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers )
soup = BeautifulSoup(page.content, 'html.parser')
prijs = soup.find("span", itemprop="price").get_text()
naam = soup.find("span", itemprop="name").get_text()


"""prfx = "https://www.na-kd.com"

for lnkt in soup.find_all('img'):
    lnks = lnkt.get('src')
    if lnks is not None:
       herf = str(prfx) + lnks
       print(herf)
       print("")"""


print("\nDe {n} is het goedkoopste.".format(n=naam))
print("")
txt = "De prijs is{} euro"
print(txt.format(prijs))
print("")

pref = "https://www.na-kd.com/nl/lingerie/onderbroeken/"



def onderbroeken():
    if "Thong" in naam:
        sort_sort = "string"
        pref = str(pref) + str("strings/")
        print("Het is een string")

    if "hipster" in naam:
        sort_sort = "hipster"
        pref = str(pref) + str("hipsters/")
        print("Het is een hipsters.")

    if "brazilian" in naam:
        sort_sort = "brazilian"
        pref = str(pref) + str("brazilians/")
        print("Het is een brazilian.")

    if "Brief" in naam:
        sort_sort = "Brief"
        pref = str(pref) + str("slipjes/")
        print("Het is een slipje.")



if sort == "body":
   pref = "https://www.na-kd.com/nl/lingerie/bodys/"
   print("Het is een body.\n")
   bodyj = soup.find(id="0")
   print(bodyj['data-tracking-json'])
if sort == "onderbroeken":
    print("het is een Onderbroek\n")
    slipj = soup.find(id="0")
    print(slipj['data-tracking-json'])
    onderbroeken()
elif sort == "bh":
    print("het is een BH.\n")
    pref = "https://www.na-kd.com/nl/lingerie/bhs/"
    bhj = soup.find(id="0")
    print(bhj['data-tracking-json'])
    burlh = bhj.find("a", class_="qa9")
    kgg = burlh['href']




if sort == "bh":
    bh_sort = kgg.rsplit('/', 1)[-2]
    pref = "https://www.na-kd.com/" + bh_sort + "/"
    urls = str(pref) + naam.replace(" ", "-")

if sort == "onderbroeken":
    urls = str(pref) + naam.replace(" ", "-")

if sort == "body":
    urls = str(pref) + naam.replace(" ", "-")



urlw = urls + str("-wit")
resw = requests.get(urlw, headers=headers)
urlz = urls + str("-zwart")
resz = requests.get(urlz, headers=headers)
urlg = urls + str("-groen")
resg = requests.get(urlg, headers=headers)
urly = urls + str("-geel")
resy = requests.get(urly, headers=headers)
urlr = urls + str("-rood")
resr = requests.get(urlr, headers=headers)
urlp = urls + str("-roze")
resp = requests.get(urlp, headers=headers)



def kleuren():
    kleuren_count = 0
    NAKD_url = open("NAKD_url.txt","w")
    NAKD_url_image = open(".NAKD_url_image.txt","w")
    if resw.content == 'Bad Request':
       print("geen witte gevonden")
    else:
        images = soup.find('img')
        image = images.find_next('img')
        imag = image.find_next('img')
        ima = imag.find_next('img')
        im = ima.find_next('img')
        i = im.find_next('img')
        op = i.find_next('img')
        print(op['src'] + str("\n"))
        NAKD_url_image.write(str(op))
        kleuren_count += 1
        print(urlw)
        NAKD_url.write(urlw)

    if resz.content == 'Bad Request':
       print("geen zwarten gevonden")
    else:
        images = soup.find('img')
        image = images.find_next('img')
        imag = image.find_next('img')
        ima = imag.find_next('img')
        im = ima.find_next('img')
        i = im.find_next('img')
        op = i.find_next('img')
        print(op['src'] + str("\n"))
        NAKD_url_image.write(str(op))
        kleuren_count += 1
        print(urlz)
        NAKD_url.write("\n{u}".format(u=urlz))

    if resy.content == 'Bad Request':
        print("geen geelen gevonden")
    else:
        images = soup.find('img')
        image = images.find_next('img')
        imag = image.find_next('img')
        ima = imag.find_next('img')
        im = ima.find_next('img')
        i = im.find_next('img')
        op = i.find_next('img')
        print(op['src'] + str("\n"))
        NAKD_url_image.write(str(op))
        kleuren_count += 1
        print(urly)
        NAKD_url.write("\n{u}".format(u=urly))

    if resg.content == 'Bad Request':
       print("geen groenen gevonden")
    else:
        images = soup.find('img')
        image = images.find_next('img')
        imag = image.find_next('img')
        ima = imag.find_next('img')
        im = ima.find_next('img')
        i = im.find_next('img')
        op = i.find_next('img')
        print(op['src'] + str("\n"))
        NAKD_url_image.write(str(op))
        kleuren_count += 1
        print(urlg)
        NAKD_url.write("\n{u}".format(u=urlg))

    if resr.content == 'Bad Request':
        print("geen rode gevonden")
    else:
        images = soup.find('img')
        image = images.find_next('img')
        imag = image.find_next('img')
        ima = imag.find_next('img')
        im = ima.find_next('img')
        i = im.find_next('img')
        op = i.find_next('img')
        print(op['src'] + str("\n"))
        NAKD_url_image.write(str(op))
        kleuren_count += 1
        print(urlr)
        NAKD_url.write("\n{u}".format(u=urlr))

    if resp.content == 'Bad Request':
        print("geen roze gevonden")
    else:
        images = soup.find('img')
        image = images.find_next('img')
        imag = image.find_next('img')
        ima = imag.find_next('img')
        im = ima.find_next('img')
        i = im.find_next('img')
        op = i.find_next('img')
        print(op['src'] + str("\n"))
        NAKD_url_image.write(str(op))
        kleuren_count += 1
        print(urlp)
        NAKD_url.write("\n{u}".format(u=urlp))

    NAKD_url.close()
    global kleuren_count
kleuren()

if kleuren_count == 1:
    print("\nEr is {k} kleur gevonden".format(k=kleuren_count))
else:
    print("\nEr zijn {k} kleuren gevonden".format(k=kleuren_count))


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
d1 = g.readline()
d2 = g.readline()
d3 = g.readline()
d4 = g.readline() #de zijn  voor bhs
d5 = g.readline()
d6 = g.readline()
d7 = g.readline() #de zin voor onder
d8 = g.readline()
d9 = g.readline()
d10 = g.readline() #de zijn  voor bodys
d11 = g.readline()
d12 = g.readline()
d13 = g.readline()
d14 = g.readline()
d15 = g.readline()
d16 = g.readline()
g.close()


d99 = "}}"
d88 = json_data.replace("}", "")
dnew = d88.replace("{", "")
dkom = "},"

if sort == "onderbroeken":
    if "}," in d3:
        L = [d1, d2, d3, d4, d5, dnew, dkom, d7, d8, d9, d10, d11, d12]
    L = [d1, d2, d3, d4, d5, dnew, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16]

if sort == "bh":
    if "}," in d3:
        L = [d1, d2, dnew, dkom, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16]
    L = [d1, d2, dnew, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16]
if sort == "body":
    L = [d1, d2, d3, d4, d5, d6, d7, d8, dnew, d10, d11, d12, d13, d14, d15, d16]

#L = [d, d1, d3, d4, d5, d6, d7, d8, d9, d18, d12, d13, d14, d15, d16, d99]

if d11 == d1:
    print("Geen json printen")
else:
    print("Nieuwe json data.")
    N1AKD = open("/Library/WebServer/Documents/NAKD.json","w")
    N1AKD.writelines(L)
    N1AKD.close()

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

notify("NA-KD", "Je prijs check is klaar.")
