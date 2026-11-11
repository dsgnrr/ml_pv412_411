import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "../assets/image-2.jpg"
image = cv2.imread(image_path)

h,w = image.shape[:2]

small = cv2.resize(image, (w // 2, h // 2), interpolation=cv2.INTER_AREA)

crop = image[h //4: 3*h//4, w//4: 3*w//4]

flipped = cv2.flip(image,1)

rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original", image)
cv2.imshow("Resized", small)
cv2.imshow("Center crop", crop)
cv2.imshow("Flipped", flipped)
cv2.imshow("Rotated 90 degrees", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
