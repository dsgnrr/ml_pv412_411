# py -m pip install opencv-python
import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "../assets/image-2.jpg"

image = cv2.imread(image_path, cv2.IMREAD_COLOR)

height, width, channels = image.shape

print(
    f"Width: {width}",
    f"Height: {height}",
    f"Channels: {channels}"
)

cv2.imshow("Picture", image)
saved = cv2.imwrite("./copy_image.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()