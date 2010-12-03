# -*- coding: utf-8 -*-
from tweeql import status_handlers

class SolrStatusHandler(status_handlers.StatusHandler):
    def __init__(self, batch_size, delimiter = u"|"):
        super(SolrStatusHandler, self).__init__(batch_size)
        self.delimiter = delimiter

    def handle_statuses(self, statuses):
        dicts = [dict(status.as_iterable_visible_pairs()) for status in statuses]
        print dicts

status_handlers.PrintStatusHandler = SolrStatusHandler
