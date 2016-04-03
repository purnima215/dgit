#!/usr/bin/env python

import dgitcore 
from dgitcore import datasets, plugins, config  

__all__ = ['get_config', 'initialize']


def _reexport(mod):
    __all__.extend(mod.__all__)
    for var in mod.__all__:
        globals()[var] = getattr(mod, var)


def initialize():
    plugins.plugins_load()
    config.init()

# What all should be exported
initialize()
_reexport(datasets)
_reexport(plugins)

