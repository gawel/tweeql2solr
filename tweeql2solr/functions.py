# -*- coding: utf-8 -*-
from tweeql.exceptions import TweeQLException
from tweeql.field_descriptor import ReturnType
from tweeql.function_registry import FunctionInformation, FunctionRegistry
from tweeql.query_runner import QueryRunner

class Url():
    return_type = ReturnType.STRING

    @staticmethod
    def factory():
        return Url().get_url

    def get_url(self, tuple_data, val):
        tuple_data['screen_name'] = tuple_data['author'].screen_name
        return 'http://twitter.com/%(screen_name)s/%(id)s' % tuple_data

fr = FunctionRegistry()
fr.register("url", FunctionInformation(Url.factory, Url.return_type))

class Entities():
    return_type = ReturnType.STRING

    @staticmethod
    def factory():
        return Entities().get_entities

    def get_entities(self, tuple_data, val):
        values = tuple_data['entities']
        value = values[val]
        if val == 'hashtags':
            return ','.join(list(set([v['text'].lower() for v in value])))
        elif val == 'user_mentions':
            return ','.join([v['screen_name'] for v in value])

fr = FunctionRegistry()
fr.register("entities", FunctionInformation(Entities.factory, Entities.return_type))



