# workaround static linked python
from julia.api import Julia
__julia__ = Julia(compiled_modules=False)

import os
import sys
import subprocess

from .wrappers import apply

script_dir = os.path.dirname(os.path.realpath(__file__))

def install():
    """
    Install Julia packages required for yao-framework.
    """
    subprocess.check_call(['julia', os.path.join(script_dir, 'install.jl')])
