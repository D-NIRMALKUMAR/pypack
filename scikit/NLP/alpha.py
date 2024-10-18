import cv2
import pytesseract

img=cv2.imread('d.jpg')

text = pytesseract.image_to_string(img)
print("Alphanumeric text extracted from image:", text)
  
cv2.imshow('img',img)
cv2.waitKey(0)