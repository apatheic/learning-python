#quickWeather.py - displays the weather forecast for a given locality

import sys, requests, json

if len(sys.argv) < 2:
    print('Using: quickWeather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])
API_KEY = 'Enter_your_api_key' 

url = 'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&appid=%s' % (location, API_KEY)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData['list']
print('Weather today in %s:' % (location))
print(w[0]['weather'][0]['main'], '-',
      w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-',
      w[1]['weather'][0]['description'])
print('The day after tomorrow:')
print(w[2]['weather'][0]['main'], '-',
      w[2]['weather'][0]['description'])
