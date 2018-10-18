#!/usr/bin/env python
import versioneer
from setuptools import setup, find_packages

setup(name='dvlssdk',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='A python SDK for interacting with Devolutions Server',
      author='Devolutions inc,',
      author_email='support@devolutions.net',
      url='https://devolutions.net/',
      install_requires=[
          "pycryptodomex",
          "requests",
      ],
      packages=find_packages(exclude='tests')
      )
