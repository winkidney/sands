# coding: utf-8
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__name__))


setup(
    name='sand-maker',
    version='0.1',
    packages=['sand_maker.words', 'sand_maker.words.migrations', 'sand_maker.sand_maker'],
    url='http://github.com/winkidney/sand-maker',
    license='GPL v3',
    packages=find_packages(here),
    author='winkidney',
    author_email='winkidney@gmail.com',
    description='Make sentence from words, enjoy and make new story.',
    requires=[
        "django-registration-defaults",
    ]
)
