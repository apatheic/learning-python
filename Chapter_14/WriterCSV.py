import csv

with open('example.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n\n')
    
    print(writer.writerow('Hello'))

    print(writer.writerow(['Elliot', 'Debra', 'Angela', 'Edward', 'Tyrel']))
