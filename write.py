import os

x = len(os.listdir('/Volumes/tatiana_art/psd/'))+1

L = 'count="{fo}"'.format(fo=x)

N1AKD = open("/Users/MWK/Desktop/.coun","w")
N1AKD.write(L)
N1AKD.close()
