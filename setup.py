from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='onlykey',
    version='0.0.2',
    description='OnlyKey client and command-line tool',
    long_description=long_description,

    url='https://github.com/trustcrypto/python-onlykey',
    author='Thomas Sileo',
    author_email='t@a4.io',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points = {
        'console_scripts': [
            'onlykey-cli=onlykey.cli:main',
            'onlykey-utils=onlykey.cli:utils',
            'onlykey-init=onlykey.cli:init',
            'onlykey-settime=onlykey.settime:main'
        ],
    },
    install_requires=['hidapi', 'aenum', 'six', 'prompt_toolkit', 'ed25519', 'cython'],
)
