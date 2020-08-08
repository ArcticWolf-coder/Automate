from PIL import Image
im=Image.open("groom.jpg")
im.rotate(45).show()

new =im.resize((150,300))
new.save("groom0.jpg")

new=im.rotate(90)
new.save("groom1.jpg")

im.rotate(190).resize((120,240))
print(im.format,im.size,im.mode)