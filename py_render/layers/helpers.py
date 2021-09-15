from typing import Tuple
from .base_layer import Layer
from PIL import Image

__author__ = "xcodz-dot"

class AreaFilter(Layer):
    def __init__(self, area: Tuple[int, int, int, int], filter: Layer):
        super().__init__(f"{filter.name} (AreaFilter)", f"(AreaFilter): {filter.description}")
        self._area = (area[0], area[1], area[0]+area[2], area[1]+area[3])
        self._filter = filter

    def apply(self, im: Image.Image) -> Image.Image:
        frame = im.crop(self._area)
        frame = self._filter.apply(frame)
        im2 = im.copy() 
        im2.paste(frame, self._area)
        return im2


class Crop(Layer):
    def __init__(self, area: Tuple[int, int, int, int]):
        super().__init__("Crop", "Crop and return an image with the given dimensions")
        self._area = (area[0], area[1], area[0]+area[2], area[1]+area[3])
    
    def apply(self, im: Image.Image) -> Image.Image:
        return im.crop(self._area)


class Resize(Layer):
    DEFAULT = None
    NEAREST = Image.NEAREST
    BOX = Image.BOX
    BILINEAR = Image.BILINEAR
    HAMMING = Image.HAMMING 
    BICUBIC = Image.BICUBIC
    LANCZOS = Image.LANCZOS
    def __init__(self, size: Tuple[int, int], resample_method=None):
        super().__init__("Resize", "Resize a Image by reducing the resolution to given resolution")
        self._size = size
        self._resample_method = resample_method
    
    def apply(self, im: Image.Image) -> Image.Image:
        return im.resize(self.size, resample=self._resample_method)
