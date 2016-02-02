from distutils.core import setup
from distutils.extension import Extension
from Pyrex.Distutils import build_ext

import numpy

ext = Extension("sum", ["sum.pyx"],
                include_dirs = [numpy.get_include()])
                
setup(ext_modules=[ext],
      cmdclass = {'build_ext': build_ext})

