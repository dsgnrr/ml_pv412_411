import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "../assets/image-2.jpg"
image = cv2.imread(image_path)

blue, green, red = cv2.split(image)

merged = cv2.merge((blue,green, red))
cv2.imshow("Merged", merged)

cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(f"Pixel in BGR: {image[0,0]}")
print(f"Pixel in RGB: {rgb[0,0]}")