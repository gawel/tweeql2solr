# -*- coding: utf-8 -*-
import os
import sys
import config
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-w", "--where-clause", dest="where",
                  action="store",
                  help="where clause")
parser.add_option("--username", dest="username",
                  action="store",
                  help="twitter username")
parser.add_option("--password", dest="password",
                  action="store", default=os.environ.get('TWITTER_PASSWORD', ''),
                  help="twitter password")
parser.add_option("-s", "--batch-size", dest="batch_size",
                  action="store", default='1',
                  help="Number of tweets to proceed before indexing. Default: 1")
parser.add_option("-u", "--url", dest="url",
                  action="store", default='http://127.0.0.1:8983/solr/',
                  help="solr url. Default: http://127.0.0.1:8983/solr/")
parser.add_option("-1", "--solr1", dest="version",
                  action="store_true", default=False,
                  help="use this if you do not use solr 4.")
parser.add_option("-v", "--verbose", dest="verbose",
                  action="store_true", default=False,
                  help="increase verbosity")

(options, args) = parser.parse_args()

config.DEBUG = options.verbose
config.BATCH_SIZE = int(options.batch_size)
config.SOLR_URL = options.url
config.SOLR1 = int(options.version)
config.TWITTER_USERNAME = options.username
config.TWITTER_PASSWORD = options.password or os.environ.get('TWITTER_PASSWORD')

sys.modules['settings'] = config

def main():
    import patch
    import functions
    from tweeql.exceptions import TweeQLException
    from tweeql.query_runner import QueryRunner
    runner = QueryRunner()
    params = dict(
        where=options.where and 'WHERE %s' % options.where or '',
        table=options.where and 'twitter' or 'twitter_sample'
    )
    query = '''select url(text) as id, screen_name, text, created_at,
       entities('hashtags') as cat, entities('user_mentions') as user_mentions,
       tweetLatLng("lat") as latitude, tweetLatLng("lng") as longitude
       from %(table)s
       %(where)s;''' % params
    if config.DEBUG:
        print '      ', query
    runner.run_query(query, False)

