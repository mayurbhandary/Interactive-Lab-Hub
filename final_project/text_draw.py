# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import time


i2c = busio.I2C(board.SCL, board.SDA)

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
font = ImageFont.load_default()

def display_product_information(name, price):
    oled.fill(0)
    oled.show()

    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    (font_width, font_height) = font.getsize(name)

    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - 3 * font_height // 2),
        name,
        font=font,
        fill=1,
    )

    (font_width, font_height) = font.getsize(str(price))

    draw.text(
        (oled.width // 2 - font_width // 2, oled.height // 2 - 0.5 * font_height // 2),
        str(price),
        font=font,
        fill=255,
    )

    oled.image(image)
    oled.show()





if __name__ == "__main__":
    for i in range(100000000):
        if i % 2 == 0:
            display_product_information("some product", "$12.99")
        else:
            display_product_information("some product", "$13.99")
        
        time.sleep(1)
   