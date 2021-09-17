# Py_Render

A Simple library to make your photos better.

**Note**: Documentation has not been implemented completely yet. Please wait until first major release.

## Concepts

### Layers

Layers are basic form of edits that are made, Multiple layers can be stacked to make Workflows.

### Workflows

These are groups of Layers that are executed on an input image to produce output after applying it through all the layers one by one.

### Sources

Sources are objects that can be in the following forms:
* `PIL.Image.Image`
* `py_render.sources.Source`
* `[PIL.Image.Image, Union[Workflow, Source, Layer]]`

they are taken as input by most of the workflows and layers.
They can be evaluated using `py_render.sources.evaluate`
