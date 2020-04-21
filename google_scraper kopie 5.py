import requests
from clint.textui import progress
from bs4 import BeautifulSoup

URL = raw_input("Voer de url in: ")


headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

description = soup.find("meta",  property="og:description")

print(description["content"] if description else "Er is geen tekst hier in.")
