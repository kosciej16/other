from PyPDF2 import PdfFileMerger
from glob import glob
from pathlib import Path

f1_files = glob("pdfs/*")
f2_files = glob("pdfs/*")

for f1 in f1_files:
    number = f1.split(".")[0]
    for f2 in f2_files:
        if number in f2:
            merger = PdfFileMerger()
            merger.append(f1)
            merger.append(f2)
            merger.write(f2)


# merger = PdfFileMerger()

# merger.append("1.pdf")
# merger.append("2.pdf")
# merger.write("6.pdf")
