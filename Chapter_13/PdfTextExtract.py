import pypdf

pdfFileObj = open('SuperSecret.pdf', 'rb')
pdfReader = pypdf.PdfReader(pdfFileObj)

#returns the number of lines in the file
print(len(pdfReader.pages))   

#extracts text from the file and stores the PageObj variable
pageObj = pdfReader.pages[0]
print(pageObj.extract_text())

pdfFileObj.close()
