#!/usr/bin/env python
import os
os.system('clear')
import requests
from bs4 import BeautifulSoup
import sys
import wget


# For every line in the file
for url in open('/Users/MWK/Desktop/tatiana_down.txt'):
    # Split on the rightmost / and take everything on the right side of that
    name = url.rsplit('/', 1)[-1]


    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

    print("Downloading")
    print(url)

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    image = soup.find("meta",  property="og:image")

    title = soup.find("meta",  property="og:title")
    def video():
        video = soup.find("meta",  property="og:video")

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
        local_image_filename = wget.download(video["content"], out=path)


        x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))+1

        source = local_image_filename

        dest = '/Users/MWK/Desktop/tatiana/tatiana_video_{n}.jpg'.format(n=x)

        os.rename(source, dest)

    print(image["content"] if image else "Er is geen afbeelding.")
    print("")
    print("Dit is de beschrijving:")
    print(title["content"] if title else video())
    print("")


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

    source = local_image_filename

    dest = '/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x)

    os.rename(source, dest)

os.system('/Users/MWK/Desktop/OLE/meta_insta.app/Contents/MacOS/Application\ Stub ; exit;')
