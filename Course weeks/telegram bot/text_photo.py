from PIL import Image
from pytesseract import pytesseract


image_path = r"example.jpeg"
img = Image. open (image_path)
text = pytesseract.image_to_string(img)

print (text[: -1])