#Netflix type system demo - FakeFlix
#import csv
import sys
TK_SILENCE_DEPRECATION=1

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
 print("Downloading document")
 import requests
 from bs4 import BeautifulSoup

 headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

 URL = "https://docs.google.com/document/d/129SWfi_sF3MvKyce4nBSdNU4l5gCDRXfemz8Ycbw-eU/edit?usp=sharing"

 page_goole = requests.get(URL, headers=headers)

 soup = BeautifulSoup(page_goole.content, 'html.parser')

 description = soup.find("meta",  property="og:description")
 print(description["content"] if description else "Er is geen tekst.")

 import urllib2
 fp = urllib2.urlopen(description["content"])
 print(fp.geturl())
 #print(description["content"] if description else "Er is geen tekst.")

 URLINSTA = description["content"]

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

 #test link googe docs https://docs.google.com/document/d/17WRu2xbcR_yqTmWaebbTjlKUcdCqNb-3wDx5A_SHui8/edit?usp=sharing
 import wget

 local_image_filename = wget.download(image["content"])

 print("")
 print("\nklaar ja kan nu naar de map OLE gaan")
 sys.exit

def Video():
    print("Downloading document")
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

    URL = "https://docs.google.com/document/d/129SWfi_sF3MvKyce4nBSdNU4l5gCDRXfemz8Ycbw-eU/edit?usp=sharing"

    page_goole = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page_goole.content, 'html.parser')

    description = soup.find("meta",  property="og:description")

    import urllib2
    fp = urllib2.urlopen(description["content"])
    print(fp.geturl())
    #print(description["content"] if description else "Er is geen tekst.")

    URLINSTA = description["content"]

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
