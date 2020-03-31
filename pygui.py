from appJar import gui
import os
import sys
from PIL import Image, ImageTk
#def press():
    #print("User:", app.entry("URLINSTA"), "Pass:", app.entry("Password"))

def press():
    os.system('clear')
    URLINSTA = app.entry("Instagram url")
    print("Importing")
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

    print("Downloading")

    page = requests.get(URLINSTA, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    image = soup.find("meta",  property="og:image")

    title = soup.find("meta",  property="og:title")

    print(image["content"] if title else "Er is geen afbeelding.")
    print("")
    print("Dit is de beschrijving:")
    print(title["content"] if title else "Er is geen beschrijving.")
    print("")
     #test link https://www.instagram.com/p/B-PZFIvAT7a/
    import wget
     #test link googe docs https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target = "tatiana_art"
    prefix_list = ["91018230_151840196296351_1894637158564459764_n"]
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target = "tatiana_art"
    prefix_list = ["91018230_151840196296351_1894637158564459764_n"]

    for prefix in prefix_list:
         path = os.path.join(base_dir, "tatiana")
         if not os.path.exists(path):
             os.mkdir(path)
         if not os.path.isdir(path):
             exit()

    local_image_filename = wget.download(image["content"], out=path)
    x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))-1
    source = local_image_filename
    dest = '/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x)

    os.rename(source, dest)
    from PIL import Image
    img = Image.open(dest)
    img.show()

    sys.exit
    app.stop

with gui("Login Window", "500x300", font={'size':14}) as app:
    dest = '/Users/MWK/Desktop/tatiana/tatiana_art_10.jpg'
    photo = ImageTk.PhotoImage(Image.open(dest))
    app.addImageData("pic", photo, fmt="PhotoImage")
    app.label("Welcome to insta downloader")
    app.entry("Instagram url", label=True, focus=True)
    app.buttons(["Submit"], [press])
    app.clearImageCache()
