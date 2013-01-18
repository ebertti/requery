# -*- coding:utf-8 -*-
from setuptools import setup
import setuplib


packages, package_data = setuplib.find_packages('requery')

setup(
    name='requery',
    version='0.2.1',
    url='http://github.com/ebertti/requery/',
    author='ebertti',
    author_email='ebertti@gmail.com',
    packages=packages,
    package_data=package_data,
    license='MIT License',
    platforms=['OS Independent'],
    description="Simple way to store and use querys in database for use of DBA's",
)
