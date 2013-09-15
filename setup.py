import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "qgis_plugins",
    version = "0.0.1",
    author = "Alessandro Pasotti",
    author_email = "apasotti@gmail.com",
    description = "A django pluggable used to serve a qgis plugin repository",
    license = "GPL",
    keywords = "qgis gis plugins osgeo",
    url = "http://plugins.qgis.org",
    packages=['plugins'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPL",
    ],
    install_requires=[
        # native dependencies
        
    ],
)
