import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "../assets/image-2.jpg"
image = cv2.imread(image_path)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

erosion = cv2.erode(binary, kernel, iterations=1)

dilation = cv2.dilate(binary, kernel, iterations=1)

opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Binary", binary) 
cv2.imshow("Erosion", erosion) 
cv2.imshow("dilation", dilation)
cv2.imshow("opening", opening)
cv2.imshow("closing", closing)


cv2.waitKey(0) 
cv2.destroyAllWindows() 
