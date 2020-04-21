from exif import Image
with open('/Users/MWK/Desktop/tatiana/tatiana_art_9.jpg', 'rb') as image_file:
    my_image = Image(image_file)

my_image.has_exif
dir(my_image)
