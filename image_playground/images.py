from PIL import Image, ImageFilter

image = Image.open('./Pokedex/pikachu.jpg')
filtered_img = image.filter(ImageFilter.SHARPEN) # SMOOTH,BLUR etc
filtered_img2 = image.convert('L')
filtered_img.save('smooth.png','png')
filtered_img2.save('grey.png','png')
print(image.format)
print(image.size)
print(image.mode)

# Other manipulations
filtered_img2.show()
crooked = filtered_img.rotate(90)
crooked.save('crooked.png','png')

resize = filtered_img2.resize((300,300))
resize.save('resized.png','png')


img = Image.open('./astro.jpg')
img.thumbnail((400,200))  # to keep aspect ratio
img.save('thumbnail.jpg')
