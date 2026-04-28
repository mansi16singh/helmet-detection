MODEL_TYPE = 'yolo'   # options: yolo, rcnn, rtdetr
MODEL_PATHS = {
    'yolo': 'models/yolo_best.pt',
    'rcnn': 'models/faster_rcnn.pth',
    'rtdetr': 'models/rtdetr_best.pt'
}
SOURCE = 'webcam'   # webcam or path like videos/test.mp4
CONFIDENCE = 0.5
DEVICE = 'cuda'
LOG_FILE = 'outputs/logs/results.log'
SAVE_OUTPUT = True
