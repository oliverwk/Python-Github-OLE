import sys
from selenium import webdriver

username = "chjdesteenwinkel@hotmail.com"
password = 'Legoverkoop'

chrome_options = webdriver.ChromeOptions();
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
browser = webdriver.Chrome('/Users/MWK/Desktop/ProjectInitializationAutomation-master/chromedriver', options=chrome_options);
browser.get('https://www.marktplaats.nl/account/login.html')


def remove():
    browser.find_elements_by_xpath('//*[@id="account-login-form"]/fieldset/div/div[1]/input')[0].send_keys(username)
    browser.find_elements_by_xpath('//*[@id="password"]')[0].send_keys(password)
    browser.find_elements_by_xpath('//*[@id="gdpr-consent-accept-button"]')[0].click()
    browser.find_elements_by_xpath('//*[@id="account-login-button"]')[0].click()
    """
    browser.get('https://github.com/silv4b/' + reponame + '/settings')
    browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(reponame)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    browser.get("https://github.com/" + username)
    """

if __name__ == "__main__":
    remove()

#browser.quit()
