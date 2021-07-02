import pywhatkit as pwk
import cv2

pwk.text_to_handwriting("Hi there! I'm Sanya", save_to='handwriting.png')
img = cv2.imread('handwriting.png')
cv2.imshow('Text to handwriting', img)
cv2.waitKey(1)
cv2.destroyAllWindows()
