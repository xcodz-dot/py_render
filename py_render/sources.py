from PIL.Image import Image
from . import workflows
from .layers import base_layer

class Source:
    def __init__(self):
        pass

    def get(self): 
        return None

    def set(self, _):
        pass


class VariableSourceController:
    def __init__(self, **variables):
        self.variables = variables
    
    def __setitem__(self, k, v):
        self.variables[k].set(v)
    
    def __getitem__(self, k):
        return self.variables[k].get()
    
    def add(self, label, var):
        self.variables[label] = var
    
    def __delitem__(self, k):
        del self.variables[k]


class VariableSource(Source):
    def __init__(self, init: Image = None, controller: VariableSourceController = None, label: str = None):
        self.value = init
        self.controller = controller
        if label is not None:
            self.controller.add(label, self)

    def get(self):
        return self.value

    def set(self, val):
        self.value = val


def evaluate(im: Image) -> Image:
    oim = im
    if isinstance(im, (tuple, list)):
        if len(im) > 1:
            if isinstance(im[1], workflows.Workflow):
                im = im[1].apply(im[0])
            elif isinstance(im[1], base_layer.Layer):
                im = im[1].apply(im[0])
        
    elif isinstance(im, Source):
        im = im.get()
    
    return im
