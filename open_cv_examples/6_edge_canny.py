import cv2
import sys

image_path = sys.argv[1] if len(sys.argv) > 1 else "../assets/image-2.jpg"

image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

edges = cv2.Canny(blur, 50, 100)

cv2.imshow("Original", image) 
cv2.imshow("Grayscale", gray) 
cv2.imshow("Canny edges", edges)


contours, hierarchy= cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

# Обведіть тільки ті контури у яких площа більше за 500 пікселів
output = image.copy()

cv2.drawContours(output, contours, -1, (0,255,0), 2 )

for index, contour in enumerate(contours):
    x,y, w,h = cv2.boundingRect(contour)
    
    if w*h<500:
        continue
    
    cv2.rectangle(output, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.putText(output, f"Object-{index}", (x, max(y-8, 15)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1)

print(f"Find contours: {len(contours)}")
cv2.imshow("Contours and bounding boxes", output)

cv2.waitKey(0) 
cv2.destroyAllWindows() 