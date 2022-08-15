
from setuptools import setup, find_packages
import requests
import json

try:
    from packaging.version import parse
except ImportError:
    from pip._vendor.packaging.version import parse


URL_PATTERN = 'https://pypi.python.org/pypi/{package}/json'
NAME = 'conniosdk'


def get_version(package, url_pattern=URL_PATTERN):
    """Return version of package on pypi.python.org using json."""
    req = requests.get(url_pattern.format(package=package))
    version = parse('0')
    if req.status_code == requests.codes.ok:
        j = json.loads(req.text.encode(req.encoding))
        releases = j.get('releases', [])
        for release in releases:
            ver = parse(release)
            if not ver.is_prerelease:
                version = max(version, ver)
    return version


latest_version = float(str(get_version(NAME)))
new_version = format(latest_version + 0.011, '.2f')

setup(
    name=NAME,
    version=new_version,
    description='Connio Python SDK',
    keywords = ["connio"],
    author_email='admin@digiterra.com.tr',
    packages=find_packages(include=['connio', 'connio.*']),
    install_requires=['pytz',
                      'six',
                      'requests',
                      'paho_mqtt',
                      'simplejson',
                      'twilio'],  # external packages as dependencies,

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
)
