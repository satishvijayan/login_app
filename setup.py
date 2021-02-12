# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in login_app/__init__.py
from login_app import __version__ as version

setup(
	name='login_app',
	version=version,
	description='Authentication App',
	author='Charioteer',
	author_email='satish@charioteersoftware.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
