# -*- coding: utf-8 -*-
import patch
from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner


runner = QueryRunner()

def main():
    query = '''SELECT screen_name as name, text, created_at as
            created_dt, location, tweetLatLng("lat") as lat, tweetLatLng("lng")
            as lng FROM Twitter_sample;'''
    query = '''SELECT screen_name AS name, text, created_at as
            created_dt FROM Twitter_sample;'''
    query = "select screen_name AS name from twitter_sample;"
    runner.run_query(query, False)
