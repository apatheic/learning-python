import pypdf

pdfFile = open('Recursion_Chapter1.pdf', 'rb')
pdfReader = pypdf.PdfReader(pdfFile)
pdfWriter = pypdf.PdfWriter()

for pageNum in range(len(pdfReader.pages)):
    pdfWriter.add_page(pdfReader.get_page(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
