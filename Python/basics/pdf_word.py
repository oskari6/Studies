from PyPDF2 import PdfReader,PdfWriter, PdfMerger

reader = PdfReader("example.pdf")
for page in reader.pages:
    print(page.extract_text())

writer = PdfWriter()
writer.add_page(reader.pages[0])
with open("output.pdf", "wb") as output:
    writer.write(output)

merger = PdfMerger()
merger.append("file1.pdf")
merger.append("file2.pdf")
merger.write("merged.pdf")
merger.close()
