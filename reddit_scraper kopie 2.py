import requests
from bs4 import BeautifulSoup

URL = "https://www.reddit.com/r/BralessForever/comments/fmdkht/golden_hour/"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

#video = soup.find_all('video')

#print(video)

sleper = soup.find('video').get('src')

print(sleper)
