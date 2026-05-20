#! python3
#lucky.py - Opens multiple search results using Google

import webbrowser, requests, bs4, sys

print('Googling...')
res = requests.get(f'google.com/search?q={' '.join(sys.argv[1:])}')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open(f'google.com{linkElems[i].get('href')}')
L
