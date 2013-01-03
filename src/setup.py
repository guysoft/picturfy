#!/usr/bin/env python

from distutils.core import setup
from picturfy import __version__

setup(name='picturfy',
      version=__version__,
      description='Turn HTML webpages to PNG images',
      author='Guy Sheffer',
      author_email='guysoft@gmail.com',
      url='https://github.com/guysoft/picturfy/',
      long_description="""A small python/shell utiliy to turn webpages in to PNG images, using webkit/wkhtmltopdf and ImageMagick""",
      packages=[],
      scripts=['picturfy.py']
     )
