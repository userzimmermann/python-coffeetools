import sys
from setuptools import setup

setup(
  name = 'coffeetools',
  version = '0.1a',
  description = (
    'Tools for using CoffeeScript with Python.'
    ),
  author = 'Stefan Zimmermann',
  author_email = 'zimmermann.code@gmail.com',
  url = 'http://bitbucket.org/userzimmermann/python-coffeetools',

  license = 'GPLv3',

  packages = [
    'coffeetools',
    'coffeetools.jinja',
    ],

  classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    ],
  keywords = [
    'coffee', 'tools', 'script', 'coffeescript', 'javascript',
    'jinja', 'jinja2', 'template', 'tag', 'extension',
    ],
  )
