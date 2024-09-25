#!./regexpress_api/bin/python3
import pytesseract
from pdf2image import convert_from_path

# convert to image using resolution 600 dpi 
pages = convert_from_path("file:///home/sanmi/Downloads/FKJ 136 FX.pdf", 600)

# extract text
text_data = ''
for page in pages:
    text = pytesseract.image_to_string(page, lang='eng')
    text_data += text + '>>>'

    print("**unknown**")
    text_data + '\n page done'
print(text_data)