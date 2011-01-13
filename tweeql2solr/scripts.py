# -*- coding: utf-8 -*-
import patch
import functions
from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner


runner = QueryRunner()

def main():
    query = '''SELECT screen_name as name, text, created_at as
            created_dt, location, tweetLatLng("lat") as lat, tweetLatLng("lng")
            as lng FROM Twitter_sample;'''
    query = '''SELECT screen_name AS name, text, created_at as
            created_dt FROM Twitter_sample;'''
    query = '''select url(text) as id, screen_name, text, created_at,
               entities('hastags') as cat, entities('user_mentions') as user_mentions,
               tweetLatLng("lat") as latitude, tweetLatLng("lng") as longitude
               from twitter_sample;'''
    runner.run_query(query, False)
