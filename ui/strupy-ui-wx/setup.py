#!/usr/bin/env python
import io
import re
from setuptools import setup, find_packages
import sys

with io.open('./strupy-ui-wx/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.rst', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='strupy-ui-wx',
    version=version,
    description='apps',
    long_description=long_description,
    author='newapps',
    author_email='thisapps',
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(
        exclude=[
            'docs', 'tests',
            'windows', 'macOS', 'linux',
            'iOS', 'android',
            'django'
        ]
    ),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    install_requires=[
    ],
    options={
        'app': {
            'formal_name': 'strupy-ui-wx',
            'bundle': 'com.bundl'
        },

        # Desktop/laptop deployments
        'macos': {
            'app_requires': [
            ]
        },
        'linux': {
            'app_requires': [
            ]
        },
        'windows': {
            'app_requires': [
            'pint==0.8.1',
            'wxpython==4.0.1',
            ]
        },

        # Mobile deployments
        'ios': {
            'app_requires': [
            ]
        },
        'android': {
            'app_requires': [
            ]
        },

        # Web deployments
        'django': {
            'app_requires': [
            ]
        },
    }
)
