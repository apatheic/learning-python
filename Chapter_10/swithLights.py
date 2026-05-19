market_2nd = {'ns': 'green', 'ew': 'red'}
market_16th = {'ns': 'red', 'ew': 'green'}

def swithLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
swithLights(market_2nd)
