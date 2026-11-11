from ultralytics import YOLO
import cv2

model = YOLO("./runs/detect/train-2/weights/last.pt")

path = input("Enter image name: ")

results = model.predict(
    source = f"./dog_model_our/new_data/{path}",
    conf=0.25
)

result = results[0]

image = result.plot()

cv2.imshow("YOLO Model predict", image)

cv2.waitKey(0)
cv2.destroyAllWindows()



















