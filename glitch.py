from glitch_this import ImageGlitcher
import urllib.request
from PIL import Image

glitcher = ImageGlitcher()


def do_glitch(url, level):
    urllib.request.urlretrieve(url, "img_file.jpg")
    img = Image.open("img_file.jpg")
    glitch_img = glitcher.glitch_image(img, level, color_offset=True)
    return glitch_img
