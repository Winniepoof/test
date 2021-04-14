from PIL import Image


img=Image.open('Mikami Yua.jpg')
# img.show()
print(img.format)
print(img.size)
print(img.height,img.width)
print(img.getpixel((100,200)))