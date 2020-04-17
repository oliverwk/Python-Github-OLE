from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter import scrolledtext

window = Tk()

window.title("google UI app")

window.geometry('773x413')

txt = scrolledtext.ScrolledText(window,width=770,height=410)

txt.grid(column=0,row=0)

entry1 = window.Entry (root)

txt.grid(column=1, row=0)

URL = entry1.get()

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

description = soup.find("meta",  property="og:description")

txt.insert(INSERT,description["content"])

window.mainloop()
