import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "../assets/image-2.jpg"
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

threshold_value, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

cv2.imshow("Original - color", image)
cv2.imshow("Grayscale - shades of gray", gray)
cv2.imshow("Binary - black and white", binary)

cv2.imwrite("gray.jpg", gray)
cv2.imwrite("black_and_white.jpg", binary)

cv2.waitKey(0)
cv2.destroyAllWindows();


