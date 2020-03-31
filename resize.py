from PIL import Image
import os

b = raw_input("Voer het nummer in dat je kleiner wilt maken: ")
x = len(os.listdir('/Users/MWK/Desktop/tatiana/'))-1

img = Image.open('/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=b))
height = img.size
print("current size {n}" .format(n=height))

new_image = img.resize((135, 180))
new_image.save('/Users/MWK/Desktop/tatiana/tatiana_art_{n}.jpg'.format(n=x))
