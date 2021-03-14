from PIL import Image, ImageDraw, ImageFont


class _Image:
    @staticmethod
    def draw_picture_with_text(image_file, text, size, x, y):
        image = Image.open(image_file)
        draw = ImageDraw.Draw(image)
        width_image, height_image = image.size
        font = ImageFont.truetype("arial.ttf", size=size)
        draw.text((x, y), text, font=font, fill='white')
        image.save(f'{image_file}')
    @staticmethod
    def draw_cross_on_picture(image_file, color, width):
        with Image.open(image_file) as im:
            draw = ImageDraw.Draw(im)
            draw.line((0, 0) + im.size, fill=color, width=width)
            draw.line((0, im.size[1], im.size[0], 0), fill=color, width=width)

            # write to stdout
            im.save(image_file)
    @staticmethod
    def draw_rect_on_picture(image_file, x0, y0, x1, y1, color, width):
        with Image.open(image_file) as im:
            draw = ImageDraw.Draw(im)
            draw.rectangle((x0,y0,x1,y1), outline=color, width=width)

            # write to stdout
            im.save(image_file)
