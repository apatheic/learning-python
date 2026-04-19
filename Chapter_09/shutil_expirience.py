import os, shutil

os.chdir('..') 
print(f"Active directory: {os.getcwd()}")
shutil.copy('/home/fsociety/spam.txt', '/home/fsociety/delicious')
shutil.copy('/home/fsociety/eggs.txt', '/home/fsociety/delicious/eggs2.txt')
print('Copy file access.')
