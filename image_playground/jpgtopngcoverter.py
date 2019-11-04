import sys
import os
from os import listdir
from os.path import splitext
from PIL import Image

# grab first and second argument
# check if new exist or not if not create
# loop thru Pokedex
# convert images to png
# save to the new folder

path = str(sys.argv[1])
new_path = sys.argv[2]

if not os.path.exists(new_path):
    os.makedirs(new_path)

target = '.png'

for i in listdir(path):
    filename, extension = splitext(i)
    img = Image.open(path+filename+extension)
    img.save(new_path+filename+target)
