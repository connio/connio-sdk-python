
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
    author_email='admin@digiterra.com.tr',
    packages=find_packages(include=['connio', 'connio.*']),
    install_requires=['pytz',
                      'six',
                      'requests',
                      'paho_mqtt',
                      'simplejson',
                      'twilio'],  # external packages as dependencies
    long_description = """Python Connio Helper Library""" 
)
