#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('image.jpg')
width, height = im.size
#txt = Image.new('RGBA', im.size, (255,255,255,0))

draw = ImageDraw.Draw(im)
text = "sample watermark"

font = ImageFont.truetype('arial.ttf', 500)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text

x=width/2-textwidth/2
y=height/2-textheight/2

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font,fill=(200,200,200,100))
im.show()

#watermarked = Image.alpha_composite(im, txt)

#Save watermarked image
im.save('watermark.jpg')