"""from exif import Image
import os
os.system('clear')
with open('/Users/MWK/Desktop/tatina_.png', 'wb') as new_image_file:
    new_image_file.write(new_image_file.get_file())
    self.image.set("model", "EXIF Package")"""

fn = '/Users/MWK/Desktop/tatina_.png'

def test_PIL():
    # test PIL
    from PIL import Image
    from PIL.ExifTags import TAGS
    print( '\n<< Test of PIL >> \n' )

    img = Image.open(fn)
    info = img._getexif()
    for k, v in info.items():
        nice = TAGS.get(k, k)
        print( '%s (%s) = %s' % (nice, k, v) )
