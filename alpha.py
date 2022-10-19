#Importing Libraries
from PIL import Image, ImageDraw, ImageFont

#Opening Image & Creating New Text Layer



def getImage(name):

    img = Image.open(name).convert("RGBA")
    
    return img

#100 -> 714x111
#
#
#
def generateWatermark(text, img, percentage = 90):

    width, height = img.size 

    fontsize = percentage * width / 714

    txt = Image.new('RGBA', img.size, (255,255,255,0))
    font = ImageFont.truetype("arial.ttf", int(fontsize))
    d = ImageDraw.Draw(txt)

    textwidth, textheight = d.textsize(text, font)

    x=width/2-textwidth/2
    y=height/2-textheight/2
    d.text((x,y), text, fill=(255,255,255, 125), font=font)

    return txt


def saveWatermark(path, img, txt):
    watermarked = Image.alpha_composite(img, txt)
    watermarked.save(path)
    return watermarked

img = getImage('sample.png')

txt = generateWatermark('AndrejVysny', img)

w = saveWatermark('test.png', img,txt)
w.show()
