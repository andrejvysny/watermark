#Importing Libraries
import random
from PIL import Image, ImageDraw, ImageFont

#Opening Image & Creating New Text Layer
img = Image.open('sample.png')
img = img.convert('RGBA')
txt = Image.new('RGBA', img.size, (255,255,255,0))

#Creating Text
text = "CapturePoint.sk"
font = ImageFont.truetype("arial.ttf", 100)

#Creating Draw Object
draw = ImageDraw.Draw(img)

#Positioning Text
width, height = img.size 
textwidth, textheight = draw.textsize(text, font)
x=width/2-textwidth/2
y=height/2-textheight/2

#Applying Text
draw.text((x,y), text, fill=(255,255,255, 75), font=font)

#Combining Original Image with Text and Saving
img = Image.alpha_composite(img, txt)

img.save('new.png')

img.show()