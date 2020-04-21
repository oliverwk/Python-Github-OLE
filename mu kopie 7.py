os.system('clear')
from multiprocessing import Pool
import os
import requests
from bs4 import BeautifulSoup
import sys
import wget

base_url = 'ttps://www.instagram.com/p/B-bnv2MJhVe/?igshid=dcahdeiqaemc'

all_urls = list()
for url in open('/Users/MWK/Desktop/tatiana_down.txt'):
    # Split on the rightmost / and take everything on the right side of that
    name = url.rsplit('//', 1)[-1]
    print(name)
    #def generate_urls():
    h = 'https://'
    all_urls.append(str(h) + name)

    def scrape(url):
        headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}


    #print(url)

        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')

        image = soup.find("meta",  property="og:image")

        title = soup.find("meta",  property="og:title")

        #print(image["content"] if image else "Er is geen afbeelding.")
        #print("")
        print("Dit is de beschrijving:")
        print(title["content"] if title else "Er is geen beschrijving.")
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

        local_image_filename = wget.download(image["content"], out=path)
        x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))+1
        source = local_image_filename
        dest = '/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x)
        os.rename(source, dest)
        print("")

#generate_urls()

p = Pool(20)
p.map(scrape, all_urls)
p.terminate()
p.join()
