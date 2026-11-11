import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "../assets/image-2.jpg"

image = cv2.imread(image_path)

# в розмірі ядра розмиття задаємо тільки непарні числа
average_blur = cv2.blur(image, (5,5))

gauss_blur = cv2.GaussianBlur(image, (5,5), 0)

median_blur = cv2.medianBlur(image, 19)

cv2.imshow("Original", image)
cv2.imshow("Average blur", average_blur)
cv2.imshow("Gaussian blur", gauss_blur)
cv2.imshow("Median blur", median_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()