#!/usr/bin/ python3
# -*- coding: utf-8 -*-
reset_data = """{"NA-KD": {
      "bhs": {
        "url": "https://www.na-kd.com/nl/lingerie/bhs/Print-Bra-geel", "naam": "Print Bra", "prijs": " EUR 6.88", "kleuren": 1
            },
      "slip": {
        "url": "https://www.na-kd.com/nl/lingerie/slip/Basic-Brazilian-Micro-Panty-wit", "naam": "Basic Brazilian Micro Panty", "prijs": " EUR 5.40", "kleuren": 3
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

reset()

if len(sys.argv) == 1:
   URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"
   sort = "slip"
elif sys.argv[1] == "slip":
    URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"
    sort = "slip"
elif sys.argv[1] == "body":
    URL = "https://www.na-kd.com/nl/lingerie/bodys?sortBy=price&count=18&p_categories=c_1-33036_nl-nl"
    sort = "bodys"
elif sys.argv[1] == "bh":
    URL = "https://www.na-kd.com/nl/lingerie/bhs?sortBy=price&count=18&p_categories=c_1-32923_nl-nl"
    sort = "bhs"



#URL = "https://www.na-kd.com/nl/lingerie/onderbroeken?sortBy=price&count=18&p_categories=c_1-32927_nl-nl"
#URL = "https://www.na-kd.com/nl/lingerie/bodys?sortBy=price&count=18&p_categories=c_1-33036_nl-nl"
#URL = "https://www.na-kd.com/nl/lingerie/bhs?sortBy=price&count=18&p_categories=c_1-32923_nl-nl"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',  'Content-Type': 'application/json'}


r = requests.get(URL, headers=headers )
soup = BeautifulSoup(r.content, 'html.parser')

try:
  prijs = soup.find("span", itemprop="price").get_text()
except AttributeError:
  file = open("/Users/MWK/Desktop/error.html","w")
  file.write(str(r.content))
  file.close()
  print("written")
  sys.exit()

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

pref = "https://www.na-kd.com/nl/lingerie/slip/"



def slip():
    global pref
    if "Thong" in naam:
        sort_sort = "string"
        pref = str(pref) + str("strings/")
        print("\nHet is een string")
    elif "hipster" in naam:
        sort_sort = "hipster"
        pref = str(pref) + str("hipsters/")
        print("\nHet is een hipsters.")
    elif "brazilian" in naam:
        sort_sort = "brazilian"
        pref = str(pref) + str("brazilians/")
        print("\nHet is een brazilian.")
    elif "Brief" in naam:
        sort_sort = "Brief"
        pref = str(pref) + str("slipjes/")
        print("\nHet is een slipje.")


import emoji
if sort == "bodys":
   pref = "https://www.na-kd.com/nl/lingerie/bodys/"
   print(emoji.emojize('het is een body :one-piece_swimsuit:'))
   print("")
   bodyj = soup.find(id="0")
   bodyje = soup.find(class_="qa9")
   print(bodyj['data-tracking-json'])
   kgg = bodyje['href']
if sort == "slip":
    pref = "https://www.na-kd.com/nl/lingerie/slip/"
    print(emoji.emojize('het is een slip :briefs:'))
    print("")
    slipj = soup.find(id="0")
    slipje = soup.find(class_="qa9")
    print(slipj['data-tracking-json'])
    slip()
    kgg = slipje['href']
elif sort == "bhs":
    print(emoji.emojize('het is een Bh :bikini:'))
    print("")
    pref = "https://www.na-kd.com/nl/lingerie/bhs/"
    bhj = soup.find(id="0")
    print(bhj['data-tracking-json'])
    burlh = bhj.find("a", class_="qa9")
    kgg = burlh['href']




if sort == "bhs":
    bh_sort = kgg.rsplit('/', 1)[-2]
    pref = "https://www.na-kd.com" + bh_sort + "/"
    urls = str(pref) + naam.replace(" ", "-")

if sort == "slip":
    urls = str(pref) + naam.replace(" ", "-")

if sort == "bodys":
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
    NAKD_url = open("/Users/MWK/Desktop/OLE/NAKD_url.txt","w")
    NAKD_url_image = open("/Users/MWK/Desktop/OLE/.NAKD_url_image.txt","w")
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
        NAKD_url_image.write(str(op['src']))
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
        NAKD_url_image.write(str(op['src']))
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
        NAKD_url_image.write(str(op['src']))
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
        NAKD_url_image.write(str(op['src']))
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
        NAKD_url_image.write(str(op['src']))
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
        NAKD_url_image.write(str(op['src']))
        kleuren_count += 1
        print(urlp)
        NAKD_url.write("\n{u}".format(u=urlp))

    try:
        name = op['src']
    except UnboundLocalError:
        import shutil
        urlh = "https://www.na-kd.com" + kgg
        print(urlh)
        page1 = requests.get(urlh, headers=headers )
        soup1 = BeautifulSoup(page1.content, 'html.parser')
        NAKD_url.write("\n{u}".format(u=urlh))
        images = soup.find('img')
        image = images.find_next('img')
        imag = image.find_next('img')
        ima = imag.find_next('img')
        im = ima.find_next('img')
        i = im.find_next('img')
        op = i.find_next('img')
        name = op['src']
        image_url = name.rsplit('?', 1)[-2]
        print(image_url)
        resk = requests.get(image_url, stream=True)
        local_file = open('/Users/MWK/Desktop/OLE/temp_nakd.jpg', 'wb')
        resk.raw.decode_content = True
        shutil.copyfileobj(resk.raw, local_file)
    NAKD_url.close()
    import shutil
    name = op['src']
    image_url = name.rsplit('?', 1)[-2]
    resk = requests.get(image_url, stream=True)
    local_file = open('/Users/MWK/Desktop/OLE/temp_nakd.jpg', 'wb')
    resk.raw.decode_content = True
    shutil.copyfileobj(resk.raw, local_file)
    if kleuren_count == 1:
        print("\nEr is {k} kleur gevonden".format(k=kleuren_count))
    else:
        print("\nEr zijn {k} kleuren gevonden".format(k=kleuren_count))


kleuren()


a = prijs
f = open("/Users/MWK/Desktop/OLE/NAKD.txt", "r")
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
    NAKD = open("/Users/MWK/Desktop/OLE/NAKD.txt","w")
    NAKD.write(prijs)
    NAKD.close()


v = open("/Users/MWK/Desktop/OLE/NAKD_url.txt", "r")
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

prijs2 = prijs.replace("EUR ", " ")




#if ot == "\n":
#    img_url = imgpow
#else:
#    img_url = imgot




if ot == "\n":
    durl = pow
else:
    durl = ot




def NewBrowser():
    param = (
        ('soort', sort),
        ('naam', naam),
        ('img_url', img_url),
        ('prijs', "&euro;"+prijs2),
        ('url', durl),
        )

    response = requests.get('https://us-central1-wittopkoningweb.cloudfunctions.net/addMessage', params=param)
    print(response.content)


def browser():
    ismg = open("/Users/MWK/Desktop/OLE/.NAKD_url_image.txt","r")
    img_url = ismg.readline()
    ismg.close()
    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import db

# Fetch the service account key JSON file contents
    GOOGLE_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    cred = credentials.Certificate(GOOGLE_CREDENTIALS)

# Initialize the app with a custom auth variable, limiting the server's access
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://wittopkoningweb.firebaseio.com',
        'databaseAuthVariableOverride': {
            'uid': 'x6plHOrLxnRigLbyL0GfOg67TWx2'
            }
            })
    ref = db.reference('/NA-KD/lingerie/'+sort)
    ref.update({

        'naam': naam,
        'prijs': "&euro;"+prijs2,
        'img_url': img_url,
        'url': durl
    })


def Write():
    import time
    from selenium import webdriver
    ismg = open("/Users/MWK/Desktop/OLE/.NAKD_url_image.txt","r")
    img_url = ismg.readline()
    ismg.close()


    chrome_options = webdriver.ChromeOptions();
    #chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
    chrome_options.add_argument("user-data-dir=/Users/MWK/Library/Application\ Support/Google/Chrome/Profile\ 1")
    chrome_options.add_argument("download.default_directory=/Library/WebServer/Documents/naKD")
    browser = webdriver.Chrome('/Users/MWK/Desktop/ProjectInitializationAutomation-master/chromedriver', options=chrome_options);
    browser.get('http://wittopkoning.nl/input')

    time.sleep(3)

    browser.find_elements_by_xpath('/html/body/button[2]')[0].click()
    time.sleep(6)
    print("loged in.")

    el = browser.find_element_by_xpath("//*[@id='categorie']")
    for option in el.find_elements_by_tag_name('lingerie'):
        if option.text in labels:
            option.click()
    browser.find_elements_by_xpath('//*[@id="sort"]')[0].send_keys(sort)
    browser.find_elements_by_xpath('//*[@id="kleuren"]')[0].send_keys("1")
    browser.find_elements_by_xpath('//*[@id="prijs"]')[0].send_keys("&euro;"+prijs2)
    browser.find_elements_by_xpath('//*[@id="image_url"]')[0].send_keys(img_url)
    browser.find_elements_by_xpath('//*[@id="url"]')[0].send_keys(durl)
    browser.find_elements_by_xpath('//*[@id="naam"]')[0].send_keys(naam)

    browser.find_elements_by_xpath('/html/body/div[1]/button')[0].click()
    time.sleep(3)
    print("submitted.")
    browser.quit()



if sort == "slip":
    rslip_nakd = open("/Users/MWK/Desktop/OLE/.slip_nakd.txt","r")
    rrslip = rslip_nakd.readline()
    rslip_nakd.close()
    if rrslip == dnew:
        print("zelfde")
    else:
        browser()
        slip_nakd = open("/Users/MWK/Desktop/OLE/.slip_nakd.txt","w")
        slip_nakd.writelines(dnew)
        slip_nakd.close()
        #L = ref.get()
        N1AKD = open("/Library/WebServer/Documents/NAKD.json","w")
        N1AKD.writelines(L)
        N1AKD.close()

if sort == "bhs":
    rbh_nakd = open("/Users/MWK/Desktop/OLE/.bh_nakd.txt","r")
    rbh = rbh_nakd.readline()
    rbh_nakd.close()
    if rbh == dnew:
        print('zelfde')
    else:
        browser()
        bh_nakd = open("/Users/MWK/Desktop/OLE/.bh_nakd.txt","w")
        bh_nakd.writelines(dnew)
        bh_nakd.close()
        L = ref.get()
        N1AKD = open("/Library/WebServer/Documents/NAKD.json","w")
        N1AKD.writelines(L)
        N1AKD.close()



if sort == "bodys":
    rbody_nakd = open("/Users/MWK/Desktop/OLE/.body_nakd.txt","r")
    rbody = rbody_nakd.readline()
    rbody_nakd.close()
    if rbody == dnew:
        print('zelfde')
    else:
        browser()
        body_nakd = open("/Users/MWK/Desktop/OLE/.body_nakd.txt","w")
        body_nakd.writelines(dnew)
        body_nakd.close()
        LO = ref.get()
        N1AKD = open("/Library/WebServer/Documents/NAKD.json","w")
        N1AKD.writelines(LO)
        N1AKD.close()


#L = [d, d1, d3, d4, d5, d6, d7, d8, d9, d18, d12, d13, d14, d15, d16, d99]





os.system('/usr/local/bin/terminal-notifier  -title NA-KD  -open https://wittopkoning.nl/nak -contentImage https://www.na-kd.com/favicons/na-kd/favicon-512x512.png  -message "Je price check is klaar ."')
os.system('python3 /Users/MWK/Desktop/OLE/.NA-KD_tags.py')
os.system('python /Users/MWK/Desktop/OLE/img.py nakd')
