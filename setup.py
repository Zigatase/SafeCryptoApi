#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import re

# Get the long description from the README file
with open(path.join('README.rst'), encoding='utf-8') as f:
    long_description = f.read()


# Load Version Api
def load_version():
    version_file = "safecryptoapi/pywallet/_version.py"
    version_line = open(version_file).read().rstrip()
    vre = re.compile(r'__version__ = "([^"]+)"')
    matches = vre.findall(version_line)

    if matches and len(matches) > 0:
        return matches[0]
    else:
        raise RuntimeError(
            "Cannot find version string in {version_file}.".format(
                version_file=version_file))


version = load_version()

setup(
    name='safecrypto',
    version=version,
    description="SafeCryptiApi -> BitcoinLib, PyWallet (BugFix)",
    long_description=long_description,
    url='https://github.com/Zigatase/SafeCryptoApi',
    dowload_url='https://github.com/Zigatase/SafeCryptoApi',
    author='Zigatase',
    author_email='zigatase@gmail.com',
    license='SafeCrypto',
    classifiers=[
        "License :: OSI Approved :: SafeCrypto",
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",
        "Operating System :: OS Independent",

        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    platforms=['any'],
    keywords='bitcoin, wallet, litecoin, hd-wallet, dogecoin, dashcoin, bitcore, qtum, ravencoin, martexcoin, address, crypto, python',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'demo', 'demos', 'examples']),
    package_data={'': ['AUTHORS', 'LICENSE']},
    install_requires=[
        "base58>=0.2.2",
        "click>=8.0.4",
        "coincurve-stubs>=9.0.0"
        "coincurve>=18.0.0",
        "coveralls>=3.0.1",
        "ecdsa>=0.11",
        "fastecdsa>=2.2.1",
        "mnemonic>=0.18",
        "mysql-connector-python>=8.0.27",
        "mysqlclient>=2.1.0",
        "numpy>=1.21.0",
        "parameterized>=0.8.1",
        "psycopg2>=2.9.2",
        "pycryptodome>=3.14.1",
        "pycryptodome>=3.6.6",
        "requests>=2.25.0",
        "scrypt>=0.8.18",
        "six>=1.8.0",
        "sphinx>=4.3.1",
        "sphinx_rtd_theme>=1.0.0",
        "SQLAlchemy>=1.4.45",
    ]
)
