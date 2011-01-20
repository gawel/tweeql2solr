# -*- coding: utf-8 -*-
import urllib

try:
    import restkit
except ImportError:
    restkit = None

try:
    import simplejson as json
except ImportError:
    import json

def guess_language(text):
    if not restkit:
        return None
    if isinstance(text, unicode):
        text = text.encode('utf-8')
    url = 'http://www.google.com/uds/GlangDetect?'
    url += urllib.urlencode(dict(v='1.0', q=text))
    resp = restkit.request(url)
    data = resp.body_string()
    data = json.loads(data)
    return data.get('responseData', {}).get('language', None)

if __name__ == '__main__':
    print guess_language('bonjour')

