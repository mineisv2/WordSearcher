import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('pythonism.PNG')

n = 16
text = pytesseract.image_to_string(img)

"""def removeSpc(string):
	string =  string.replace(" ", "")
	return string

text = list(removeSpc(text))

out = [(text[i:i+n]) for i in range(0, len(text), n)] 

for i in range(len(out)):
	if out[i] == \n:
		print("yes")
		out.pop(i)"""

print(text)
