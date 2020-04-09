import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import scrolledtext

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate the Square Root')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your Number:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():


    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}
ggg = entry1.get()
page = requests.get(ggg, headers={"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'})

soup = BeautifulSoup(page.content, 'html.parser')

description = soup.find("meta",  property="og:description")

txt.insert(INSERT,description["content"])


button1 = tk.Button(text='Get the Square Root', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
