import pypdf

pdf1file = open('Recursion_Chapter1.pdf', 'rb')
pdf1reader = pypdf.PdfReader(pdf1file)
pdfWriter = pypdf.PdfWriter()

for pageNum in range(len(pdf1reader.pages)):
    pageObj = pdf1reader.get_page(pageNum)
    pdfWriter.add_page(pageObj)

pdfOutputFile = open('watermark.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1file.close()
