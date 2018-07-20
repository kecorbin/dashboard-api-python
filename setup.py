# coding: utf-8
from setuptools import setup, find_packages  # noqa: H301


NAME = "meraki"
VERSION = "0.34"
DESCRIPTION = "python bindings for  Meraki Dashboard API calls"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "ipaddress",
    "requests"
]


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    url="https://github.com/meraki/dashboard-api-python",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
