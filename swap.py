import sys

from PIL import Image

input_filename = sys.argv[1]
palette_filename = sys.argv[2]
new_palette_filename = sys.argv[3]
output_filename = sys.argv[4]

fim = Image.open(input_filename)
width, height = fim.size
input_pixels = fim.load()

pim = Image.open(palette_filename)
ow, oh = pim.size
palette_pixels = pim.load()

nim = Image.open(new_palette_filename)
nw, nh = nim.size
new_palette_pixels = nim.load()

output_im = Image.new('RGBA', (width, height))
for i in range(width):
    for j in range(height):
        px = input_pixels[i, j]
        # find color
        for k in range(ow):
            p_px = palette_pixels[k, 1]
            if px == p_px:
                n_px = new_palette_pixels[k, 1]
                output_im.putpixel((i, j), n_px)
                break

output_im.save(output_filename)
print('done swapping!')
