from types import MethodType
from .chstate import chstate
import sys

def load(commands):
    plugins = commands["plugins"]
    plugins.chstat = MethodType(chstate, plugins)
