import os
os.system('clear')
import time
import copy
import clipboard
import sys
from selenium import webdriver

# TODO: op box site inloggen en all nieuw afbeelding pakken en naar .txt bestand schrijven

"""chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument("user-data-dir=/Users/MWK/Library/Application\ Support/Google/Chrome/Profile\ 1")
browser = webdriver.Chrome('/Users/MWK/Desktop/ProjectInitializationAutomation-master/chromedriver', options=chrome_options);
browser.get('https://app.box.com/s/w6bl4bi7sohu8ruxzzcju127jsz4nzon')
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/main/div/div/div[1]/header/div/div/button')[0].click()
time.sleep(2)
browser.find_elements_by_xpath('/html/body/div[3]/div/div[2]/div/button')[0].click()
browser.quit()"""

username = "oli4wk@gmail.com"
password = "guhFun-bomqus-8fyndi"

chrome_options = webdriver.ChromeOptions();
#chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument("user-data-dir=/Users/MWK/Library/Application\ Support/Google/Chrome/Profile\ 1")
chrome_options.add_argument("download.default_directory=/Library/WebServer/Documents/naKD")
browser = webdriver.Chrome('/Users/MWK/Desktop/ProjectInitializationAutomation-master/chromedriver', options=chrome_options);
browser.get('https://account.box.com/login')
browser.find_elements_by_xpath('//*[@id="login-email"]')[0].send_keys(username)
browser.find_elements_by_xpath('//*[@id="login-submit"]')[0].click()
time.sleep(1)
browser.find_elements_by_xpath('//*[@id="password-login"]')[0].send_keys(password)
browser.find_elements_by_xpath('/html/body/div/div[2]/form/div/div[2]/button')[0].click()
time.sleep(2)


browser.get('https://app.box.com/folder/99853133393')
#in recent zijn we nu
boxs = open("/Library/WebServer/Documents/lutus.txt","w")

print("eerste\n")
time.sleep(3)

browser.find_elements_by_xpath('/html/body/div[1]/div[5]/span/div/main/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div/div/span/a')[0].click()
time.sleep(3)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/div[2]/button[2]')[0].click()
boxs.write(text1)


#tweede
print("tweede\n")
time.sleep(3)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/main/div/div/div[3]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/span/a')[0].click()
time.sleep(2)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/div[2]/button[2]')[0].click()

#derde
print("derde\n")
time.sleep(3)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/main/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/div[2]/div/div/div[1]/div/span/a')[0].click()
time.sleep(2)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/div[2]/button[2]')[0].click()

#vierde
print("vierde\n")
time.sleep(3)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/main/div/div/div[3]/div[1]/div/div/div[2]/div/div[4]/div[2]/div/div/div[1]/div/span/a')[0].click()
time.sleep(2)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/div[2]/button[2]')[0].click()

#vijfde
print("vijfde\n")
time.sleep(3)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/main/div/div/div[3]/div[1]/div/div/div[2]/div/div[5]/div[2]/div/div/div[1]/div/span/a')[0].click()
time.sleep(2)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/div[2]/button[2]')[0].click()

#zesde
print("zesde\n")
time.sleep(3)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/a')[0].click()
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/main/div/div/div[3]/div[1]/div/div/div[2]/div/div[6]/div[2]/div/div/div[1]/div/span/a')[0].click()
time.sleep(2)
browser.find_elements_by_xpath('//*[@id="app"]/div[5]/span/div/span/div/div[1]/div[2]/button[2]')[0].click()

boxs.close()

time.sleep(2)
print("klaar")
browser.quit()
