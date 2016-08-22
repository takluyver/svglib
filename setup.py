"""SVGLIB"""

from setuptools import setup
import glob
import os.path
import sys


def project_path(*names):
    return os.path.join(os.path.dirname(__file__), *names)


def read(path):
    if sys.version_info < (3,):
        f = open(path)
    else:
        f = open(path, encoding='UTF-8')
    text = f.read()
    f.close()
    return text

setup(
    name='svglib3',
    version='0.2',

    install_requires=[
    ],

    author='Sebastian Wehrmann, Dinu Gherman',
    author_email='sebastian.wehrmann@icloud.com, gherman@darwin.in-berlin.de',
    license='LGPL 3',
    url='https://github.com/sweh/svglib',
    package_dir={'svglib': 'src/svglib'},
    packages=['svglib'],
    keywords='',
    classifiers="""\
        Development Status :: 4 - Beta
        Environment :: Console
        Intended Audience :: Developers
        Intended Audience :: End Users/Desktop
        License :: OSI Approved :: GNU General Public License (GPL)
        Natural Language :: English
        Operating System :: MacOS :: MacOS X
        Operating System :: Microsoft :: Windows
        Operating System :: POSIX
        Programming Language :: Python
        Programming Language :: Python :: 2
        Programming Language :: Python :: 2.6
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.3
        Programming Language :: Python :: 3.4
        Programming Language :: Python :: 3.5
        Topic :: Documentation
        Topic :: Multimedia :: Graphics :: Graphics Conversion
        Topic :: Printing
        Topic :: Software Development :: Libraries :: Python Modules
        Topic :: Text Processing :: Markup :: XML
        Topic :: Utilities
"""[:-1].split('\n'),
    description="An experimental library for reading and converting SVG. Python 3 compatible.",
    long_description='\n\n'.join(read(project_path(name)) for name in (
        'README.txt',
        'CHANGES.txt'
    )),

    include_package_data=True,
    data_files=[('', glob.glob(project_path('*.txt')))],
    zip_safe=False,
)
