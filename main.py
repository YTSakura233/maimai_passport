from PIL import Image, ImageDraw, ImageFont

BACK_PATH = 'static/image/passport.png'
ICON_PATH = 'static/image/UI_Icon_000011.png'
FONT_PATH = 'static/KozGoPr6N-Heavy-2.otf'

def creat(name, rating, shoucang):
    if int(rating) < 2000:
        rating_path = 'static/image/0.png'
    elif 2000 <= int(rating) < 4000:
        rating_path = 'static/image/2000.png'
    elif 4000 <= int(rating) < 6000:
        rating_path = 'static/image/4000.png'
    elif 6000 <= int(rating) < 8000:
        rating_path = 'static/image/6000.png'
    elif 8000 <= int(rating) < 10000:
        rating_path = 'static/image/8000.png'
    elif 10000 <= int(rating) < 12000:
        rating_path = 'static/image/10000.png'
    elif 12000 <= int(rating) < 13000:
        rating_path = 'static/image/12000.png'
    elif 13000 <= int(rating) < 14000:
        rating_path = 'static/image/13000.png'
    elif 14000 <= int(rating) < 14500:
        rating_path = 'static/image/14000.png'
    elif 14500 <= int(rating) < 15000:
        rating_path = 'static/image/14500.png'
    elif int(rating) >= 15000:
        rating_path = 'static/image/15000.png'
    back = Image.open(BACK_PATH)
    icon = Image.open(ICON_PATH)
    rating_bg = Image.open(rating_path)
    font = ImageFont.truetype(FONT_PATH, 34)
    font1 = ImageFont.truetype('static/造字工房怪魅体.ttf', 51)

    draw = ImageDraw.Draw(back)

    icon = icon.convert('RGBA')
    icon = icon.resize((141, 141))
    rating_bg = rating_bg.convert('RGBA')
    rating_bg = rating_bg.resize((324, 61))

    rating_text_color = '#ffe045'
    outline_color = 'black'
    outline_width = 2
    letter_spacing = 5.5

    sc_color = 'white'
    sc_outline_color = '#5d5252'
    sc_outline_width = 2

    icon_position = (68, 118)
    name_position = (252, 102)
    rating_position = (251, 165)
    shoucang_position = (386, 252)
    if int(rating) < 10000:
        rating_text_position = (433, 181)
    else:
        rating_text_position = (407, 181)

    back.paste(icon, icon_position, mask=icon)
    back.paste(rating_bg, rating_position, mask=rating_bg)
    draw.text(name_position, name, font=font, fill='black')

    # rating文字以及描边
    x, y = rating_text_position
    for char in rating:
        char_bbox = draw.textbbox((0, 0), char, font=font)
        char_width = char_bbox[2] - char_bbox[0]

        for dx in range(-outline_width, outline_width):
            for dy in range(-outline_width, outline_width):
                if dx != 0 and dy != 0:
                    draw.text((x + dx, y + dy), char, font=font, fill=outline_color)

        draw.text((x, y), char, font=font, fill=rating_text_color)

        x += char_width + letter_spacing

    # 收藏品数文字以及描边
    x, y = shoucang_position
    for char in shoucang:
        char_bbox = draw.textbbox((0, 0), char, font=font1)
        char_width = char_bbox[2] - char_bbox[0]

        for dx in range(-sc_outline_width, sc_outline_width):
            for dy in range(-sc_outline_width, sc_outline_width):
                if dx != 0 and dy != 0:
                    draw.text((x + dx, y + dy), char, font=font1, fill=sc_outline_color)

        draw.text((x, y), char, font=font1, fill=sc_color)

        x += char_width

    back.save('passport_1.png', 'PNG')
    back.show()

if __name__ == '__main__':
    name = "☆Ａｉｒｂｎｂ☆"
    rating = "15000"
    shoucang = "6324"
    creat(name, rating, shoucang)