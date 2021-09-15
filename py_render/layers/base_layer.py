from PIL import Image

class Layer:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
    
    def apply(self, im: Image.Image) -> Image.Image:
        return im