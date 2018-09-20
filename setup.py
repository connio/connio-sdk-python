from __future__ import with_statement
import sys
from setuptools import setup, find_packages

__version__ = None
with open('connio/__init__.py') as f:
    exec(f.read())

# To install the connio-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup(
    name = "connio",
    version = __version__,
    description = "Connio API client ",
    author = "Connio Inc.",
    author_email = "help@conio.com",
    url = "https://github.com/connio/connio-sdk-python/",
    keywords = ["connio"],
    install_requires = [
        "pytz",
        "PyJWT >= 1.4.2",
        "paho-mqtt >= 1.4.0",
    ],
    extras_require={
        ':python_version<"3.0"': [
            "requests[security] >= 2.0.0",
        ],
        ':python_version>="3.0"': [
            "requests >= 2.0.0",
            "pysocks",
        ],
    },
    packages = find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        ],
    long_description = """\
    Python Connio Helper Library
    ----------------------------

    DESCRIPTION
    The Connio Python SDK simplifies the process of making admin and data requests 
    to the Connio platform using the Connio REST API.
    The Connio REST API lets to you create devices, write data into device properties,
    and much more.  See https://www.github.com/connio/connio-sdk-python for more information.

     LICENSE The Connio Python Helper Library is distributed under the MIT
    License """ )
