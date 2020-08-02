import PyPDF2
import sys

# This get all the arguments, except the first, into a list
from PyPDF2 import PdfFileMerger


def pdf_merger(pdf_list):
    merger: PdfFileMerger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('super.pdf')


arguments = sys.argv[1:]
pdf_merger(arguments)
