import os
import urllib
import requests
from bs4 import BeautifulSoup
import sys
os.system('clear')
DOWNLOADS_DIR = '/Users/MWK/Desktop/tatiana'

# For every line in the file
for url in open('tatiana_down.txt'):
    # Split on the rightmost / and take everything on the right side of that
    name = url.rsplit('/', 1)[-1]


    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

    print("Downloading")
    print(url)

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    image = soup.find("meta",  property="og:image")

    title = soup.find("meta",  property="og:title")

    print(image["content"] if title else "Er is geen afbeelding.")
    print("")
    print("Dit is de beschrijving:")
    print(title["content"] if title else "Er is geen beschrijving.")
    print("")

    # Combine the name and the downloads directory to get the local filename
    #filename = os.path.join(DOWNLOADS_DIR, name)

    import wget
    #test link googe docs https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing
    base_dir = os.path.dirname(os.path.abspath(__file__))
    target = "tatiana_art"
    prefix_list = ["91018230_151840196296351_1894637158564459764_n"]

    for prefix in prefix_list:
        path = os.path.join(base_dir, "tatiana")
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.isdir(path):
            exit()

    #test googe   https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing
    local_image_filename = wget.download(image["content"], out=path)


    x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))+1
    #print(x)

    source = local_image_filename

    dest = '/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x)

    os.rename(source, dest)
    print("")
    # Download the file if it does not exist
    #urllib.urlretrieve(url, filename)
