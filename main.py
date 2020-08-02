# sudo pip3 install PyPDF2
import PyPDF2

with open('/home/dvd/scripts/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)
    print(reader.getPage(0))
    page = reader.getPage(0)
    page.rotateClockwise(180)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf','wb') as new_file:
        writer.write(new_file)
