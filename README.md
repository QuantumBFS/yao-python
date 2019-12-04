# Yao Python Package
This directory and nested files contain Yao Python Package and language binding.

**warning**: This package is a simple wrapper around the Julia package Yao. To use the full feature and power of Yao, we highly recommend you to use it from Julia language natively.

## Installation

To install Yao Python package, install Julia 1.x first,
visit [julialang.org](https://julialang.org/) to download
the Julia language.

Then install the python binding by

```python
pip install yao-framework
```

If you haven't installed the Julia package **Yao** and **PyCall**, you can install them from Python by

```python
import yao_framework
yao_framework.install()
```

CUDA is not supported for Yao Python Package yet.
