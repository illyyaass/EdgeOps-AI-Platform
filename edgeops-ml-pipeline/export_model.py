from ultralytics import YOLO

def main():
    print("⏳ Loading YOLO model...")
    # غانتيليشارجيو الموديل الخفيف (Nano)
    model = YOLO("yolo11n.pt") 

    print("⚙️ Exporting model to ONNX format...")
    # dynamic=True باش نقدرو نخدمو بـ Dynamic Batching من بعد فـ Triton
    path = model.export(format="onnx", imgsz=640, dynamic=True)
    
    print(f"✅ Export Complete! The ONNX file is ready at: {path}")

if __name__ == "__main__":
    main()