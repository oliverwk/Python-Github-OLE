#!/usr/bin/env python
import sys
import os

from bs4 import BeautifulSoup

def main():
   menu()

def menu():
    print("************Welcome to instagram downloader**************")

    choice = raw_input("""
                      A: Image
                      B: Video
                      Q: Exit

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        Image()
    elif choice == "B" or choice =="b":
        Video()
    elif choice=="Q" or choice == "q":
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

def Image():
 URLINSTA = raw_input("Voer het instagram Url in : ")
 print("Importing")
 import requests

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

 #test googe   https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing
 local_image_filename = wget.download(image["content"], out=path)


 x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))+1
 #print(x)

 source = local_image_filename

 dest = '/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x)

 os.rename(source, dest)

 sys.exit

def Video():
    print("Downloading document")
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

    URLINSTA = raw_input("Voer het instagram Url in : ")

    page = requests.get(URLINSTA, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    video = soup.find("meta",  property="og:vide")

    print("")
    print(video["content"] if video else "Er is geen afbeelding.")
    print("")
    #test link https://www.instagram.com/p/B-PZFIvAT7a/

    #test link googe docs https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing
    import wget

    local_image_filename = wget.download(video["content"])

    print("")
    print("\nklaar ja kan nu naar de map OLE gaan")

    sys.exit

#the program is initiated, so to speak, here
main()
