
#Load and show an image with Pillow
from PIL import Image
import sys

if len(sys.argv) == 1:
   url = raw_input("kies een afbeelding ")
elif sys.argv[1] == "nakd":
    url = '/Users/MWK/Desktop/OLE/temp_nakd.jpg'

#Load the image
img = Image.open(url)

img.show()
