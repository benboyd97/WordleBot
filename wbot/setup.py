from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('solve_c.py'))
setup(ext_modules = cythonize('play_c.py'))
setup(ext_modules = cythonize('validation_c.py'))

