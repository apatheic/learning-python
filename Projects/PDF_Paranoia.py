#!python3

#PDF_Paranoia.py - This program encrypts data and adds the _encrypted tag to its name.

import pypdf, os



def pdf_file_finder(start_path):

    pdf_files = []

    for folder, subfolders, filenames in os.walk(start_path):

        for filename in filenames:

            if filename.endswith('.pdf'):

                pdfFile = open(os.path.join(folder, filename), 'rb')

                pdfReader = pypdf.PdfReader(pdfFile)

                pdfWriter = pypdf.PdfWriter()

                for pageNum in range(len(pdfReader.pages)):

                    pdfWriter.add_page(pdfReader.get_page(pageNum))

                pdfWriter.encrypt('swordfish')

                base_name, file_ext = os.path.splitext(filename)

                new_filename = base_name + '_encrypted' + file_ext

                resultPdf = open(new_filename, 'wb')

                pdfWriter.write(resultPdf)

                resultPdf.close()

                pdfFile.close()



pdf_file_finder('.')
