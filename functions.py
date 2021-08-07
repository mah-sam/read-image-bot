import pytesseract
import requests
from PIL import Image


def is_image(url):
    '''Returns True if url is a proper image else returns false'''
    types = ('.jpg', '.png', '.jpeg', '.bmp')
    for type in types:
        if type in url:
            return True
    return False


def process_image(image_url, language):
    '''Takes an image url and language code, returns the text in the image'''
    stream = requests.get(image_url, stream=True).raw
    return pytesseract.image_to_string(Image.open(stream), lang=language)
