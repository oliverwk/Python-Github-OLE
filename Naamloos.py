import os
os.system('clear')
import requests
from bs4 import BeautifulSoup
import sys
URL = "https://www.w3schools.com/action_page.php"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
page = requests.get(URL, headers=headers )
soup = BeautifulSoup(page.content, 'html.parser')
file = open("/Users/MWK/Desktop/Naamloos.html","w")
file.writelines(soup.prettify())
file.close()
