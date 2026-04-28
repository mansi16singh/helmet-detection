import cv2
from config import MODEL_TYPE, SOURCE, CONFIDENCE
from src.inference import Detector
from logger import log_message


def run():
    detector = Detector(model_type=MODEL_TYPE, conf=CONFIDENCE)
    cap = cv2.VideoCapture(0 if SOURCE == 'webcam' else SOURCE)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        output, fps, count = detector.predict(frame)
        cv2.putText(output, f'FPS: {fps:.2f}', (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
        cv2.imshow('Helmet Detection', output)
        log_message(f'Detections: {count} | FPS: {fps:.2f}')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
