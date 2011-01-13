# -*- coding: utf-8 -*-
from tweeql import status_handlers
import pysolr

ALIASES = dict(
        created_at='created_dt',
        screen_name='author',
    )

class SolrStatusHandler(status_handlers.StatusHandler):
    def __init__(self, batch_size, delimiter = u"|"):
        super(SolrStatusHandler, self).__init__(batch_size)
        self.delimiter = delimiter
        self.conn = pysolr.Solr('http://127.0.0.1:8983/solr/')

    def handle_statuses(self, statuses):
        dicts = [dict(status.as_iterable_visible_pairs()) for status in statuses]
        cleaned_dicts = []
        for old in dicts:
            d = dict([(ALIASES.get(k, k), v) for k, v in old.items() if v])
            if 'cat' in d:
                cd['cat'] = d['cat'].split()
            if 'user_mentions' in d:
                d['user_mentions'] = d['user_mentions'].split()
            if 'latitude' in d:
                d['store'] = '%(latitude)s,%(longitude)s' % d
                del d['latitude']
                del d['longitude']
            for k in ('user_mentions',):
                if k in d:
                    del d[k]
            cleaned_dicts.append(d)
        print cleaned_dicts
        try:
            self.conn.add(cleaned_dicts)
        except AttributeError, e:
            # pysolr fail to scrap an error
            # don't care about failures. it's only tweets..
            print e
            pass

status_handlers.PrintStatusHandler = SolrStatusHandler
