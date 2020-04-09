import sys
import os

source = '/Volumes/tatiana\ art\ /psd/IMG_4995.jpg'
print(source)
dest = '/Volumes/tatiana\ art\ /psd/IMG_4994.psd'
print(dest)
os.rename(source, dest)

dest = 'Volumes/tatiana\ art\ /psd\ betand/IMG_4994.psd'
print(dest)
source2 = '/Volumes/tatiana art /psd betand/ding tekenen 61.psd'
print(source2)
os.rename(dest, source2)
