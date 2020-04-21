from appJar import gui
import wget
import requests
from bs4 import BeautifulSoup
import sys
TK_SILENCE_DEPRECATION=1

def press():
    #print("User:", app.entry("Username"), "Pass:", app.entry("Password"))
    URL = app.entry("Username")
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    description = soup.find("meta",  property="og:image")
    app.stop
    sys.exit
#test link https://www.instagram.com/p/B-PZFIvAT7a/

    local_image_filename = wget.download(description["content"])
    print("\nklaar ja kan nu naar de map OLE gaan")

with gui("Instagram Downloader", "773x413", bg='white', font={'size':18}) as app:
    app.image('91018230_151840196296351_1894637158564459764_n.jpg')#, over='91018230_151840196296351_1894637158564459764_n(2).jpg')
    app.addImage("light", "Instagram-logo.gif")
    #app.setIcon("iconinsta.png")
    app.label("Instagram Downloader", fg='#d3a020')
    app.entry("Username", label=True, focus=True)
    app.buttons(["Download", "Klaar"], [press, app.stop])
