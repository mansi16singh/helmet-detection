import os
import cv2
import torch


def create_folder(path):
    os.makedirs(path, exist_ok=True)


def select_device():
    return 'cuda' if torch.cuda.is_available() else 'cpu'


def draw_boxes(frame, boxes, labels, scores, conf=0.5):
    for i in range(len(boxes)):
        if scores[i] >= conf:
            x1, y1, x2, y2 = map(int, boxes[i])
            label = str(labels[i])

            color = (0, 255, 0) if 'helmet' in label.lower() else (0, 0, 255)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                frame,
                f"{label} {scores[i]:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    return frame


def save_image(path, image):
    cv2.imwrite(path, image)
