from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(name='dataRead',
      version=version,
      description="'package to read data for machine learning tasks'",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords="'readcsv' 'readtext' 'readexcel' 'readtable' 'readdataframe'",
      author='',
      author_email="'siva.halasya@gmail.com'",
      url='',
      license="'MIT'",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
