# -*- coding:utf-8 -*-
from setuptools import setup
import setuplib
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

packages, package_data = setuplib.find_packages('requery')

setup(
    name='requery',
    version='0.3',
    url='http://github.com/ebertti/requery/',
    download_url='http://github.com/ebertti/requery/tarball/0.3',
    author='Ezequiel Bertti',
    author_email='ebertti@gmail.com',
    install_requires=reqs,
    packages=packages,
    package_data=package_data,
    license='MIT License',
    platforms=['OS Independent'],
    description="Simple way to store and use querys in database for use of DBA's",
    long_description=(open('README.rst').read()),
    keywords = ['query', 'dba', 'repository', 'report']
)
