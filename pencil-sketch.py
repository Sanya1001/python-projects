import cv2

image = cv2.imread("sania.jpeg")
# cv2.imshow("Sania", image)
# cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Scale", gray_image)
# cv2.waitKey(0)

inverted_image = 255 - gray_image
# cv2.imshow("Inverted", inverted_image)
# cv2.waitKey(0)

blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)

inverted_blurred_image = 255 - blurred_image
pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
# cv2.imshow("Sketch", pencil_sketch)
# cv2.waitKey(0)

cv2.imwrite('Sania-new.jpg', pencil_sketch)
