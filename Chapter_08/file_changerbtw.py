with open('texxt.txt', 'w+') as f: 
    f.write('Bye Bye World')
    f.seek(0)
    print(f.read())

with open('texxt.txt', 'a') as f:
    f.write(' BTWWW')
