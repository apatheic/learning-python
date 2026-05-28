import csv

#opening file
with open('example.csv', 'r', encoding ='utf8') as f:

    #call object Reader
    exampleReader = csv.reader(f)

    #Convert to a regular Python list
    exampleData = list(exampleReader)

    print(exampleData)
    #[['Timestamp', 'Fruit', 'Quantity'], ['4/5/2025 13:34', 'Apples', '73'], ['4/5/2025 3:41', 'Cherries', '85'], ['4/6/2025 12:46', 'Pears', '14'], ['4/8/2025 8:59', 'Oranges', '52'], ['4/10/2025 2:07', 'Apples', '152'], ['4/10/2025 18:10', 'Bananas', '23'], ['4/10/2025 2:40', 'Strawberries', '98']]

    print(exampleData[1][0])
    #4/5/2025 13:34
    print(exampleData[1][1])
    #Apples
    print(exampleData[1][2])
    #73
