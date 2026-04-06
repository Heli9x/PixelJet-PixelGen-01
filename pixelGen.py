import json
from PIL import Image

class PixelGen:
    def __init__(self, dimension):
        self.img = Image.new("RGB", (dimension, dimension))
        self.pixel_plate = self.img.load()
        self.data = []

    def compile_data(self):
        for row in self.data:
            for pixel_data in row:
                x, y, color_str = pixel_data
                color_tuple = tuple(map(int, color_str[4:-1].split(', ')))
                self.pixel_plate[y, x] = color_tuple

    def load_pixels(self, name):
        with open(f"{name}.json", "r") as f:
            self.data = json.load(f)

    def resize_image(self, dimension):
        self.img = self.img.resize((dimension, dimension), Image.NEAREST)

    def save(self, name):
        self.img.show()
        self.img.save(f"{name}.png")

def load_image_data(name):
    with open(f'cc0/{name}.json', 'r') as f:
        data = json.load(f)
    return data



def get_image(name, res, size):
    data = load_image_data(name)
    img = Image.new('RGB', (size, size))
    pixels = img.load()

    for row in data:
        for pixel_data in row:
            x, y, color_str = pixel_data
            color_tuple = tuple(map(int, color_str[4:-1].split(', ')))
            pixels[y, x] = color_tuple

    img = img.resize((res, res), Image.NEAREST)
    img.show()
    img.save(f'cc0/{name}/{name}_{res}x{res}.png')

image_objs = ['NanoGate', 'Parity']
import os
for name in image_objs:
    if not os.path.exists(f'cc0/{name}'):
        os.mkdir(f"cc0/{name}")
    
    get_image(name,200, 10)
    get_image(name,64, 10)
        