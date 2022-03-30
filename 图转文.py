import requests
import re
from PIL import Image
import os
import pytesseract as pt
path=r"D:\tesseract\tesseract.exe"
pt.pytesseract.tesseract_cmd=path
img=Image.open("01.png")
text=pt.image_to_string(img,lang="chi_sim")
print(text)