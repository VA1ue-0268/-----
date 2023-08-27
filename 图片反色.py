from PIL import Image
import PIL.ImageOps

name = input("图片名：")

image = Image.open(name)
name = name.split(".")[0]
if image.mode == 'RGBA':
    r,g,b,a = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))
    inverted_image = PIL.ImageOps.invert(rgb_image)
    r2,g2,b2 = inverted_image.split()
    final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
    final_transparent_image.save(f'{name}_new.png')
else:
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save(f'{name}_new.png')