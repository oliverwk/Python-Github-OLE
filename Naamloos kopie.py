import urllib, os
# if you comment out this line, it will download to the directory from which you run the script.
os.chdir('tatiana')
url = 'http://www.mydomain.com/myfile.txt'
urllib.urlretrieve(url)
