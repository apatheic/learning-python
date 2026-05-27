#combinePdfs.py - it combines all PDF documents in the current working cart into a single PDF document

import pypdf, os

#get all names of PDF-files
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = pypdf.PdfWriter()

#Organize a loop acrooss all PDF-files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = pypdf.PdfReader(pdfFileObj)

    if pdfReader.is_encrypted:
        pdfReader.decrypt('swordfish')

#Organization of the loop on all pages (except the first one) with their addition to the resulting document
    for pageNum in range(1, len(pdfReader.pages)):
        pageObj = pdfReader.get_page(pageNum)
        pdfWriter.add_page(pageObj)
    pdfFileObj.close()

#Save new PDF-document in file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
