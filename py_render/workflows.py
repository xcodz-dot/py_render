from PIL.Image import Image
from . import sources


class Workflow:
    def __init__(self):
        pass

    def apply(self, im: Image):
        return sources.evaluate(im)


class LinearWorkflow(Workflow):
    def __init__(self, layers=[]):
        self.layers = layers
    
    def apply(self, im: Image):
        for x in self.layers:
            im = sources.evaluate([im, x])
        return im

