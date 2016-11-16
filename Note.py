from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import ctypes
import re

def setting() :
    setting = re.findall('[(.+?)]', open('set.ini').read())
    return setting

font, size, backimg, x, y, space = setting()
notes = open('note.txt', 'rb').read().split('\r\n')
image = Image.open(backimg)

draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font, int(size))

for note in notes :
    draw.text((x, y), note, (255,255,255), font=font)
    y += space

image.save('bg.png')

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "image.jpg" , 0)
