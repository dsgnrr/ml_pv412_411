from ultralytics import YOLO
import torch

def main():
    print("CUDA: ", torch.cuda.is_available())
    
    if torch.cuda.is_available():
        print("GPU: ", torch.cuda.get_device_name(0))
    
    model = YOLO("yolo11n.pt")
    
    results = model.train(
        data = "./dog_dataset/data.yaml",
        epochs=50,
        imgsz=416,
        batch=4,
        device=0,
        workers=0
    )    
    

if __name__ == "__main__": main()