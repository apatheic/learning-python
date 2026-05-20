import requests, bs4

res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)

type(noStarchSoup)
#<class 'bs4.BeautifulSoup'>
