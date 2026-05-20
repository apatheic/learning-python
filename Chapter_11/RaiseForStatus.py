import requests

res = requests.get('http://gutenberg.org/FakePage')
try:
    res.raise_for_status()
except Exception as e:
    print('We found a trouble: %s' % (e))
