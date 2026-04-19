import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pokka', 'desc': 'floffy'}]
print(pprint.pformat(cats))
fileObj = open('myCats', 'w')
print(fileObj.write(f'cats = {pprint.pformat(cats)} \n'))
fileObj.close()
