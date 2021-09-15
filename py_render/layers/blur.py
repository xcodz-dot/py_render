from .base_layer import Layer
from PIL import ImageFilter
from PIL import Image

__author__ = "xcodz-dot"

class Blur(Layer):
    def __init__(self, blur: float):
        super().__init__("Blur", "Blurs a image based on blur density")
        self._filter = ImageFilter.GaussianBlur(blur)

    def apply(self, im: Image.Image) -> Image.Image:
        return im.filter(self._filter)
