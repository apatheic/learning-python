import zipfile, os
os.chdir('./')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()
