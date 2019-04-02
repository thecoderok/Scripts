#!/usr/bin/env python3
import sys
import os
try:
    from PyPDF2 import PdfFileReader, PdfFileWriter
except ImportError:
    from pyPdf import PdfFileReader, PdfFileWriter

def pdf_cat(input_folder, output_file_name):
    input_streams = []
    try:
        # First open all the files, then produce the output file, and
        # finally close the input files. This is necessary because
        # the data isn't read from the input files until the write
        # operation. Thanks to
        # https://stackoverflow.com/questions/6773631/problem-with-closing-python-pypdf-writing-getting-a-valueerror-i-o-operation/6773733#6773733
        file_names = []
        for dirpath, _, filenames in os.walk(input_folder):
            for fname in filenames:
                if not fname.endswith(".pdf"):
                    continue
                full_name = os.path.join(dirpath, fname)
                print("Appending %s" % full_name)
                file_names.append("" + full_name)

        print(file_names)     
        file_names.sort()
        for fname in file_names:
            input_streams.append(open(fname, 'rb'))

        writer = PdfFileWriter()
        for reader in map(PdfFileReader, input_streams):
            for n in range(reader.getNumPages()):
                writer.addPage(reader.getPage(n))
        writer.write(file(output_file_name, "wb"))
    finally:
        for f in input_streams:
            f.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise Exception('Expecting arguments: <folder with pdfs> <output file name>')
    input_folder = sys.argv[1]
    output_file_name = sys.argv[2]
    pdf_cat(input_folder, output_file_name)
