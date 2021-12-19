import sys

from PIL import Image

filename = sys.argv[1]
pfilename = sys.argv[2]

im = Image.open(filename)
pixels = im.load()

width, height = im.size

pxx = []
for i in range(width):
    for j in range(height):
        pxx += [pixels[i, j]]

pxx = list(set(pxx))

szz = 20
ow, oh = len(pxx)*szz, szz

img = Image.new('RGBA', (ow, oh))
for k, px in enumerate(pxx):
    for i in range(szz):
        for j in range(szz):
            img.putpixel((k*szz+i, j), px)

img.save(pfilename)
print('high five!')
