import pypdf

pdfReader = pypdf.PdfReader(open('watermark.pdf', 'rb'))
print(pdfReader.is_encrypted)
#True

print(pdfReader.get_page(0))
#{'/Type': '/Page', '/Parent': IndirectObject(2, 0, 139663602459248), '/Resources': {'/Font': {'/F1': IndirectObject(5, 0, 139663602459248)}, '/ExtGState': {'/GS7': IndirectObject(7, 0, 139663602459248), '/GS8': IndirectObject(8, 0, 139663602459248), '/GS11': IndirectObject(11, 0, 139663602459248)}, '/XObject': {'/Image9': IndirectObject(9, 0, 139663602459248)}, '/ProcSet': ['/PDF', '/Text', '/ImageB', '/ImageC', '/ImageI']}, '/MediaBox': [0, 0, 612, 792], '/Contents': IndirectObject(4, 0, 139663602459248), '/Group': {'/Type': '/Group', '/S': '/Transparency', '/CS': '/DeviceRGB'}, '/Tabs': '/S', '/StructParents': 0}

print(pdfReader.decrypt('rosebud'))
#1

pageObj = pdfReader.get_page(0)

pdfReader.close()
