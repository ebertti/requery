# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='requery',
    version='0.3.5.1',
    url='http://github.com/ebertti/requery/',
    author='Ezequiel Bertti',
    author_email='ebertti@gmail.com',
    install_requires=['django>=1.7', 'Pygments>=1.6', 'six>=1.7',],
    packages=['requery'],
    include_package_data=True,
    license='MIT License',
    platforms=['OS Independent'],
    description="Simple way to store and use queries in database for use of DBA for Django Admin",
    long_description=(open('README.rst').read()),
    keywords='query dba repository report django',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',

        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
    ],
    zip_safe=False,
)
