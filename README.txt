tweeql2solr is a wrapper for tweeql_. It allow you to store tweets in solr.

It recommended to use Solr4 so you can use the ``store`` field to Geo localize tweets.

If not, you need to use the ``-1`` option. See bellow.

Installation
=============

With easy_install::

  $ easy_install tweeql2solr

Usage
=====

tweeql2solr provide a simple command line script::

  $ tweeql2solr -h
  Usage: tweeql2solr [options]

  Options:
    -h, --help            show this help message and exit
    -w WHERE, --where-clause=WHERE
                          where clause
    --username=USERNAME   twitter username
    --password=PASSWORD   twitter password
    -s BATCH_SIZE, --batch-size=BATCH_SIZE
                          batch size. Default: 1
    -u URL, --url=URL     solr url. Default: http://127.0.0.1:8983/solr/
    -1, --solr1           use this if you do not use solr 4.
    -v, --verbose         increase verbosity
    

.. _tweeql: https://github.com/marcua/tweeql 

