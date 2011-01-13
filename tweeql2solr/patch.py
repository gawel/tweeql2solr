# -*- coding: utf-8 -*-
from tweeql import status_handlers
import pysolr
import config

ALIASES = dict(
        text='title',
        created_at='created_dt',
        screen_name='author',
    )

INVALID_KEYS = ('user_mentions',)
if config.SOLR1:
    INVALID_KEYS += ('store',)

class SolrStatusHandler(status_handlers.StatusHandler):
    def __init__(self, batch_size, delimiter = u"|"):
        super(SolrStatusHandler, self).__init__(config.BATCH_SIZE)
        self.delimiter = delimiter
        self.conn = pysolr.Solr(config.SOLR_URL)

    def handle_statuses(self, statuses):
        dicts = [dict(status.as_iterable_visible_pairs()) for status in statuses]
        cleaned_dicts = []
        for old in dicts:
            if 'cat' not in old:
                raise ValueError(old)
            d = dict([(ALIASES.get(k, k), v) for k, v in old.items() if v])
            cat = []
            if 'cat' in d:
                cat.extend(d['cat'].split(','))
            if 'user_mentions' in d:
                cat.extend(d['user_mentions'].split(','))
            if cat:
                d['cat'] = list(set([c.lower() for c in cat]))
            if 'latitude' in d:
                d['store'] = '%(latitude)s,%(longitude)s' % d
                del d['latitude']
                del d['longitude']
            for k in INVALID_KEYS:
                if k in d:
                    del d[k]
            cleaned_dicts.append(d)
        if config.DEBUG:
            print cleaned_dicts
        try:
            self.conn.add(cleaned_dicts)
        except AttributeError, e:
            # pysolr fail to scrap an error
            # don't care about failures. it's only tweets..
            if config.DEBUG:
                print e

status_handlers.PrintStatusHandler = SolrStatusHandler
