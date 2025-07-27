from PIL import Image

img = Image.open(r"C:\\Users\Soumyajit Koley\Downloads\OIP.jpeg")

img.show()

# converting to binary image (black and white)......................

binary_img = img.convert("1")

binary_img.show()

# converting to gray scale ............................

gray_img = img.convert("L")

gray_img.show()

# converting to RGB ...........................

rgb_img = img.convert("RGB")

rgb_img.show()