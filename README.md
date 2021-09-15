# Py_Render

A Simple library to make your photos better.

## Concepts

### Layers

Layers are basic form of edits that are made, Multiple layers can be stacked to make Workflows.

### Workflows

These are groups of Layers that are executed on an input image to produce output after applying it through all the layers one by one.

### Sources

Sources are nothing but `PIL.Image.Image` They can be loaded using helper functions provided by this library or yourself by using the `PIL.Image` directly.