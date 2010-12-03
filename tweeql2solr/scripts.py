# -*- coding: utf-8 -*-
import patch
from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner


runner = QueryRunner()

def main():
    #runner.run_query('''SELECT screen_name as name, text, created_at as
    #        created_dt, location, tweetLatLng("lat") as lat, tweetLatLng("lng")
    #        as lng FROM Twitter_sample;''', False)
    runner.run_query('''SELECT screen_name as name, text, created_at as
            created_dt FROM Twitter_sample;''', False)

