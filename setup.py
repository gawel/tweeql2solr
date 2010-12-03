from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tweeql2solr',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'tweeql',
          'pysolr',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      tweeql2solr = tweeql2solr.scripts:main
      """,
      )
