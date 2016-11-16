from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import ctypes
import re
import os

def setting() :
    setting = re.findall('\[(.+?)\]', open('set.ini').read())
    font    = setting[0]
    size    = int(setting[1])
    backimg = setting[2]
    x       = int(setting[3])
    y       = int(setting[4])
    space   = int(setting[5])
    return font, size, backimg, x, y, space

font, size, backimg, x, y, space = setting()

notes = open('note.txt', 'rb').read()[3:].split('\r\n')
image = Image.open(backimg)

draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font, int(size), encoding='utf-8')

for note in notes :
    draw.text((x, y), note.decode('utf-8'), (255,255,255), font=font)
    y += space

image.save('bg.png')
path = os.getcwd()
ctypes.windll.user32.SystemParametersInfoA(20, 0, path + "\\bg.png" , 0)
