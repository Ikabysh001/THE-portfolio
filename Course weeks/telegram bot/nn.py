# Imports PIL module 
from PIL import Image
  
# open method used to open different extension image file
im = Image.open(r"images\images-2.jpg") 
  
# This method will show image in any image viewer 
im.show()