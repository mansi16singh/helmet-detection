def train_yolo(data_yaml, epochs=50):
    from ultralytics import YOLO
    model = YOLO('yolov8n.pt')
    model.train(data=data_yaml, epochs=epochs, imgsz=640)


def train_rtdetr(data_yaml, epochs=50):
    from ultralytics import RTDETR
    model = RTDETR('rtdetr-l.pt')
    model.train(data=data_yaml, epochs=epochs, imgsz=640)


def train_faster_rcnn():
    # place extracted PyTorch training loop here
    pass
