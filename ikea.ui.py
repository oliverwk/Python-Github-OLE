#!/usr/bin/python
from appJar import gui
import sys
from PIL import Image, ImageTk
import os
os.system('clear')

def press():
    os.system('clear')
    URL = app.entry("Ikea url")
    print("Importing")
    import requests
    from bs4 import BeautifulSoup
    import csv
    URL = "https://www.ikea.com/nl/nl/p/fyrtur-verduisterend-rolgordijn-koordloos-op-batterijen-grijs-90408170/"


    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

    page = requests.get(URL, headers=headers )
    soup = BeautifulSoup(page.content, 'html.parser')

    naam = soup.find("meta",  property="og:title")
    description = soup.find("meta",  property="og:description")
    url = soup.find("meta",  property="og:image")
    prijs = soup.find("span",  class_="range-revamp-price__integer").get_text()


    import bitly_api

    BITLY_ACCESS_TOKEN ="168b3257210b004d16e1d0eed5097e4fd58e7363"

    b = bitly_api.Connection(access_token = BITLY_ACCESS_TOKEN)

    response = b.shorten(url["content"])



    print(naam["content"])
    print("")
    print(description["content"])
    print("")
    print(response["url"])
    print("")
    prijzen = prijs + str(" Euro.")
    print(prijzen)



    fields = ['naam', 'prijs', 'beschrijving']

    # data rows of csv file
    rows = [ [naam["content"], prijzen, description["content"]]]


    # writing to csv file
    with open("ikea.csv", 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

    print("csv bestand gemaakt.")


    base_dir = os.path.dirname(os.path.abspath(__file__))
    target = "OLE"
    prefix_list = ["91018230_151840196296351_1894637158564459764_n"]

    for prefix in prefix_list:
        path = os.path.join(base_dir, "OLE")
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.isdir(path):
            exit()

    local_image_filename = wget.download(url["content"], out=path)
    x = len(os.listdir('/Users/MWK/Desktop/OLE/'))+1
    source = local_image_filename
    dest = '/Users/MWK/Desktop/OLE/Ikea_{n}.jpg'.format(n=x)
    os.rename(source, dest)
    app.reloadImage(reload, dest)
    global dest
    #https://www.ikea.com/nl/nl/images/products/fyrtur-block-out-roller-blind__0595179_PE675959_S5.JPG
    sys.exit
    app.stop

with gui("Ikea prijs checker", "500x300", font={'size':14}) as app:
    dest = '/Users/MWK/Desktop/OLE/Ikea.jpg'
    photo = ImageTk.PhotoImage(Image.open(dest))
    app.addImageData("pic", photo, fmt="PhotoImage")
    app.label("Voer je Ikea URL in.")
    app.entry("Ikea url", label=True, focus=True)
    app.buttons(["Submit"], [press])
    app.clearImageCache()
