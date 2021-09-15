from .base_layer import Layer
from PIL import ImageFilter
from PIL import Image

__author__ = "xcodz-dot"

class Blur(Layer):
    def __init__(self, blur: float):
        super().__init__("Blur", "Blurs an image based on blur density")
        self._filter = ImageFilter.GaussianBlur(blur)

    def apply(self, im: Image.Image) -> Image.Image:
        return im.filter(self._filter)


class BoxBlur(Layer):
    def __init__(self, blur: float):
        super().__init__("BoxBlur", "Blurs an image based on blur density using average color per box method")
        self._filter = ImageFilter.BoxBlur(blur)
    
    def apply(self, im: Image.Image) -> Image.Image:
        return im.filter(self._filter)
