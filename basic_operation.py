from PIL import Image

img = Image.open(r"C:\\Users\Soumyajit Koley\Downloads\OIP.jpeg")
img.show()
# resizeing operation ....................

resized_img = img.resize((200,200))

resized_img.show()

# cropping operation .....................

cropped_img = img.crop((10,100,100,220))

cropped_img.show()


# rotation of image .........................

rotated_img = img.rotate(45)

rotated_img.show()