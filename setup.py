from distutils.core import setup


setup(name='Requery',
    version='0.2',
    description="Simple way to store and use querys in database for use of DBA's",
    author='Ezequiel Bertti',
    author_email='ebertti@gmail.com',
    packages=['project_requery', 'requery'],
    install_requires=['Pygments==1.5'],
    )
