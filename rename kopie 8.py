#img = Image.open(path)
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)

try:
	img = Image.open(path)
except IOError:
	pass
# Use the above statement within try block, as it can
# raise an IOError if file cannot be found,
# or image cannot be opened.
img.save(path, format)     
