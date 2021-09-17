from .. import sources
from PIL import Image

class Layer:
    author = "unknown"
    version = "unknown"
    description = "unknown"
    def __init__(self):
        pass
    
    def apply(self, im: Image.Image) -> Image.Image:
        return sources.evaluate(im)
