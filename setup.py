# -*- coding:utf-8 -*-
from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='requery',
    version='0.3.2',
    url='http://github.com/ebertti/requery/',
    author='Ezequiel Bertti',
    author_email='ebertti@gmail.com',
    install_requires=reqs,
    packages=['requery'],
    license='MIT License',
    platforms=['OS Independent'],
    description="Simple way to store and use querys in database for use of DBA's for Django Admin",
    long_description=(open('README.rst').read()),
    keywords = ['query', 'dba', 'repository', 'report']
)
