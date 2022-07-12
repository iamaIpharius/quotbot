from glitch_this import ImageGlitcher
import discord
import requests
from io import BytesIO
import urllib.request
from urllib.request import Request, urlopen
from PIL import Image

glitcher = ImageGlitcher()


def do_glitch(url, level):
    # req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # # urllib.request.urlretrieve(url, "img_file.jpg")
    # img = urlopen(req, timeout=10).read()
    # p_img = Image.open(img)

    im = Image.open(requests.get(url, stream=True).raw)
    glitch_img = glitcher.glitch_image(im, level, color_offset=True)
    if url.endswith('jpg'):
        glitch_img.save('glitched_test.jpg')
        image = discord.File(open('glitched_test.jpg', 'rb'))
        return image
    elif url.endswith('png'):
        glitch_img.save('glitched_test.png')
        image = discord.File(open('glitched_test.png', 'rb'))
        return image
