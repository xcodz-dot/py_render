from .base_layer import Layer
from PIL import ImageFilter
from PIL import Image

class Blur(Layer):
    author = "xcodz-dot"
    version = "1.0.0"
    description = "Blurs an image based on blur density"
    def __init__(self, blur: float):
        super().__init__()
        self._filter = ImageFilter.GaussianBlur(blur)

    def apply(self, im: Image.Image) -> Image.Image:
        im = super().apply(im)
        return im.filter(self._filter)


class BoxBlur(Layer):
    author = "xcodz-dot"
    version = "1.0.0b0"
    description = "Blurs an image based on blur density using average color per box method"
    def __init__(self, blur: float):
        super().__init__()
        self._filter = ImageFilter.BoxBlur(blur)
    
    def apply(self, im: Image.Image) -> Image.Image:
        im = super().apply(im)
        return im.filter(self._filter)
