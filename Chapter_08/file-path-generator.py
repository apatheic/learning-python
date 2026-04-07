#first work with modul os 
import os

myFiles = ['account.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/home/afason/Downloads/', filename))
