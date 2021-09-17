from py_render.layers.helpers import AreaFilter
from PIL import Image
from py_render import workflows, layers, sources

variable_control = sources.VariableSourceController()
light_workflow = workflows.LinearWorkflow([
    layers.Resize((640, 360), layers.Resize.LANCZOS),
    layers.AreaFilter((100, 100, 200, 100), layers.Blur(7)),
    layers.Convert("L"),
    layers.Convert("RGB"),
    layers.Composite((0, 0, 100, 100), 
        [
            sources.VariableSource(controller=variable_control, label="Composite_Image"),
            layers.Resize((100, 100))
        ]
    )
])

def simple_test():
    variable_control["Composite_Image"] = Image.open("test_images/beach.jpg")
    sources.evaluate([Image.open("test_images/beach.jpg"), light_workflow]).show()

simple_test()