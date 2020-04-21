import sys
import os

import glob

list_of_files = glob.glob('/Volumes/tatiana_art/OG_Foto/*')
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

file_naam = latest_file.rsplit('/', 1)[-1]

print(file_naam)

os.system('cp {fo} /Volumes/tatiana_art/psd/IMG.JPG'.format(fo=latest_file))

x = len(os.listdir('/Volumes/tatiana_art/psd/'))+1

dest = '/Volumes/tatiana_art/psd/IMG.JPG'

source2 = '/Volumes/tatiana_art/psd/ding_tekenen_{foo}.JPG' .format(foo=x)

os.rename(dest, source2)
