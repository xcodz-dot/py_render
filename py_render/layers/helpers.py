from typing import Tuple, Union
from .base_layer import Layer
from PIL import Image

__author__ = "xcodz-dot"

class AreaFilter(Layer):
    author = "xcodz-dot"
    version = "1.0.0"
    description = "Apply provided filter to certain area"
    def __init__(self, area: Tuple[int, int, int, int], filter: Layer):
        super().__init__()
        self._area = (area[0], area[1], area[0]+area[2], area[1]+area[3])
        self._filter = filter

    def apply(self, im: Image.Image) -> Image.Image:
        im = super().apply(im)
        frame = im.crop(self._area)
        frame = self._filter.apply(frame)
        im2 = im.copy() 
        im2.paste(frame, self._area)
        return im2


class Crop(Layer):
    author = "xcodz-dot"
    version = "1.0.0b0"
    description = "Crop and return an image with the given dimensions"
    def __init__(self, area: Tuple[int, int, int, int]):
        super().__init__()
        self._area = (area[0], area[1], area[0]+area[2], area[1]+area[3])
    
    def apply(self, im: Image.Image) -> Image.Image:
        im = super().apply(im)
        return im.crop(self._area)


class Resize(Layer):
    author = "xcodz-dot"
    version = "1.0.0"
    description = "Resize a Image by reducing the resolution to given resolution"

    DEFAULT = None
    NEAREST = Image.NEAREST
    BOX = Image.BOX
    BILINEAR = Image.BILINEAR
    HAMMING = Image.HAMMING 
    BICUBIC = Image.BICUBIC
    LANCZOS = Image.LANCZOS
    def __init__(self, size: Tuple[int, int], resample_method=None):
        super().__init__()
        self._size = size
        self._resample_method = resample_method
    
    def apply(self, im: Image.Image) -> Image.Image:
        im = super().apply(im)
        return im.resize(self._size, resample=self._resample_method)


class Flip(Layer):
    author = "xcodz-dot"
    version = "1.0.0b0"
    description = "Flips an Image based on given orientation"

    HORIZONTAL = Image.FLIP_TOP_BOTTOM
    VERTICAL = Image.FLIP_LEFT_RIGHT
    def __init__(self, mode):
        super().__init__()
        self._mode = mode
        if mode not in (Flip.HORIZONTAL, Flip.VERTICAL):
            raise ValueError("Mode must be one of the 'Flip.VERTICAL' or 'Flip.HORIZONTAL'")
    
    def apply(self, im: Image.Image) -> Image.Image:
        im = super().apply(im)
        return im.transpose(self._mode)


class Convert(Layer):
    author = "xcodz-dot"
    version = "1.0.0"
    description = "Convert an image to a specific format or type."

    PALETTE_WEB = Image.WEB
    PALETTE_ADAPTIVE = Image.ADAPTIVE
    def __init__(self, mode: str = None, matrix: Tuple[int] = None, palette=0, colors: int = 256):
        super().__init__()
        self._mode = mode
        self._matrix = matrix
        self._palette = palette
        self._colors = colors
    
    def apply(self, im: Image.Image) -> Image.Image:
        im = super().apply(im)
        return im.convert(self._mode, self._matrix, palette = self._palette, colors = self._colors)

# class Composite(Layer):
#     author = "xcodz-dot"
#     version = "1.0.0a0"
#     description = "Paste a given image to the provided image at certain area"
#     def __init__(self, area: Union[Tuple[int, int, int, int], Tuple[int, int]], image: Image.Image):
#         super().__init__()
#         self._area = (area[0], area[1], area[0]+area[2], area[1]+area[3])

#     def apply(self, im: Image.Image) -> Image.Image:
#         im = super().apply(im)
# TODO: I am in the progress of completing this   
