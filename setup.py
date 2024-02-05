__author__ = 'Lika'
import setuputils
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize


sourcefiles = ['cv_camera_finder.cpp', 'cap.cpp']

ext_modules = [
#cythonize("pymf.cpp")
# V2 Beta
Extension("cv_camera_finder", sourcefiles,
include_dirs=["capture"],
libraries=["ole32"], #error LNK2001: unresolved external symbol __imp_CoTaskMemFree
language="c++"),
]
setup(
    name = "cv_camera_finder",
    version = "1.0",
    description = "This adds device information to MSMF opencv device backend.",
    cmdclass = {'build_ext': build_ext},
    ext_modules= cythonize(
            ext_modules,
            compiler_directives={'language_level' : "3"}),
)
