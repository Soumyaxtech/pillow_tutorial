from PIL import Image

img = Image.open(r"C:\\Users\Soumyajit Koley\Downloads\OIP.jpeg") # opening image 

img.show()  # for displaying 

# getting image information ......................

print (img.format)  # jpeg/png or other format
print (img.mode)    # rgb/bgr/hsv/l(grayscale)
print (img.size)    # size of image