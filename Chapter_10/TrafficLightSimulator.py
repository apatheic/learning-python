import time

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight['ns'] == 'green':
            stoplight['ns'] = 'yellow'
            stoplight['ew'] = 'red'
        elif stoplight['ns'] == 'yellow':
            stoplight['ns'] = 'red'
            stoplight['ew'] = 'green'
        elif stoplight['ns'] == 'red':
            stoplight['ns'] = 'green'
            stoplight['ew'] = 'red'

print("Simulation started, press Ctrl+C to stop")
try:
    while True:
        print(f"Light status: {market_2nd}")
        switchLights(market_2nd)
        time.sleep(10) 
except KeyboardInterrupt:
    print("\nSimulation stoped")
