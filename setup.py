__author__ = 'Lika'

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize


sourcefiles = ['pymf.cpp', 'cap.cpp']

ext_modules = [
#cythonize("pymf.cpp")
# V2 Beta
Extension("pymf", sourcefiles,
include_dirs=["capture"],
libraries=["ole32"], #error LNK2001: unresolved external symbol __imp_CoTaskMemFree
language="c++"),
]
setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules= cythonize(
            ext_modules,
            compiler_directives={'language_level' : "3"}),
)
