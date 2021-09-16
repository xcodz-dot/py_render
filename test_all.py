from py_render.layers.helpers import AreaFilter
from PIL import Image
from py_render import workflows, layers, sources

light_workflow = workflows.LinearWorkflow([
    layers.Resize((640, 360), layers.Resize.LANCZOS),
    layers.AreaFilter((100, 100, 200, 100), layers.Blur(7)),
    layers.Convert("L"),
])

def simple_test():
    sources.evaluate([Image.open("test_images/beach.jpg"), light_workflow]).show()

simple_test()