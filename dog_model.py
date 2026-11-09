import cv2
import supervision as sv
from rfdetr import RFDETRSmall

model = RFDETRSmall(pretrain_weights="./dog_model/weights.pt")

predictor = model.inference(compile=False)


image_path = "./dog_model/new_data/1.jpg"

detections = predictor.predict(image_path, threshold=0.25)

print("Find objects: ", detections)

image = cv2.imread(image_path)

bounding_box_annotator = sv.BoxAnnotator()
label_annotator = sv.LabelAnnotator()

result_image = bounding_box_annotator.annotate(scene=image.copy(),detections=detections)
result_image = label_annotator.annotate(scene=result_image ,detections=detections)

cv2.imshow("Detections", result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()