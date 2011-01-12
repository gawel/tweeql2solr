# -*- coding: utf-8 -*-
import unittest
import pysolr

class TestSolr(unittest.TestCase):

    def setUp(self):
        self.conn = pysolr.Solr('http://127.0.0.1:8983/solr/')

    def test_01_index(self):
        docs = [{'id':'test1', 'text': 'test index'}]
        self.conn.add(docs)

    def test_02_search(self):
        res = [r for r in self.conn.search('test')]
        assert len(res) == 1, res

    def test_03_delete(self):
        self.conn.delete(id='test1')
        res = [r for r in self.conn.search('test')]
        assert len(res) == 0, res
