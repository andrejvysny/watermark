from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("longshort.ttf", 40)

    drawing.text(pos, text, fill=(200, 200, 200, 255), align='center',font=font, spacing= 10, stroke_width=3)
    photo.save(output_image_path)
    photo.show()


if __name__ == '__main__':
    img = 'image.jpg'
    watermark_text(img, 'exported.jpg',
                   text='CapturePoint.sk',
                   pos=(50, 50))