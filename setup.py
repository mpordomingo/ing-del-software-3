#!/usr/bin/env python
import django_heroku

from distutils.core import setup

setup(name='MVP',
      version='1.0',
      description='MVP project for software engineering III course at UCA 2020.',
      author='Martin Garcia Tejeda, Tomas Nozica, Martin Pordomingo',
      url='https://www.python.org/sigs/distutils-sig/'
     )

django_heroku.settings(locals())