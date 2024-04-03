from pdf2image import convert_from_path

pages = convert_from_path("eng.pdf", 50, size=(1389, 1965))
pages[0].save("OutImage.jpg", "JPEG", sie=1)
