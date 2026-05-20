import requests

res = requests.get('http://gutenberg.org/cache/epub/1112/pg111xt')
res.raise_for_status()
