import requests
from bs4 import BeautifulSoup

URL = "https://ift.tt/2WP0BK0"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find("title").get_text()


print(title.strip())


print(soup.prettify())
