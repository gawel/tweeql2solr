from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='tweeql2solr',
      version=version,
      description="tweeql2solr - store tweets in solr",
      long_description=open('README.txt').read(),
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search', 
      ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Bearstech',
      author_email='gpasgrimaud@bearstech.com',
      url='https://github.com/gawel/tweeql2solr',
      license='BSD',
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
