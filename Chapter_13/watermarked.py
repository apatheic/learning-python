import pypdf

pdfFile = open('Recursion_Chapter1.pdf', 'rb')
watermarkFile = open('watermark.pdf', 'rb')

pdfReader = pypdf.PdfReader(pdfFile)
watermarkReader = pypdf.PdfReader(watermarkFile)

pdfFirstPage = pdfReader.pages[0]

pdfFirstPage.merge_page(watermarkReader.pages[0])

pdfWriter = pypdf.PdfWriter()
pdfWriter.add_page(pdfFirstPage)

for pageNum in range(1, len(pdfReader.pages)):
    pageObj = pdfReader.pages[pageNum]
    pdfWriter.add_page(pageObj)

outputFile = open('output.pdf', 'wb')
pdfWriter.write(outputFile)
outputFile.close()

pdfFile.close()
watermarkFile.close()
