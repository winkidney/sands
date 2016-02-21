import os

from setuptools import (
    setup,
    find_packages,
)


here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='sands',
    version='0.1',
    url='http://github.com/winkidney/sands',
    license='GPL v3',
    packages=find_packages(here),
    author='winkidney',
    author_email='winkidney@gmail.com',
    description='Make sentence from words, enjoy and make new story.',
    install_requires=[
        "Flask==0.10.1",
        "Flask-Login==0.3.2",
        "Flask-WTF==0.12",
        "peewee==2.8.0",
        "click==6.2",
    ]
)