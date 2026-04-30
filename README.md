



# 🪖 Helmet Detection System

---

## 1. 🚀 Project Title
**Helmet Detection using YOLOv8, Faster R-CNN and RT-DETR on Edge Device (Jetson Nano)**

---

## 2. ❗ Problem Statement

- Detect riders **without helmets** in real-time  
- Improve **road safety enforcement**  
- Reduce **manual monitoring effort**  

---

## 3. ⚡ Role of Edge Computing
    Cloud Processing ❌
    High Latency
    Internet Required

            VS

    Edge Device (Jetson Nano) ✅
    Low Latency
    Real-time Detection
    Offline Capability

✔ Faster response  
✔ No internet dependency  
✔ Efficient real-time processing  

---

## 4. 🧠 Methodology / Approach

### 🔄 System Flow
📹 CCTV / Video Input
↓
🧩 Frame Extraction
↓
🧹 Preprocessing
↓
🤖 Detection Model
(YOLO / RT-DETR / Faster R-CNN)
↓
📦 Bounding Boxes + Labels
↓
🪖 Helmet / No Helmet Classification
↓
📊 Output + FPS + Logs

---

### 🧩 Pipeline Diagram
+-------------------+
| Input Source |
| (Camera/Video) |
+---------+---------+
↓
+-------------------+
| Preprocessing |
+---------+---------+
↓
+---------------------------+
| Detection Model |
| YOLO | RT-DETR | RCNN |
+---------+---------+
↓
+-------------------+
| Detection Output |
| Boxes + Labels |
+---------+---------+
↓
+-------------------+
| Display + Logging |
+-------------------+


---

## 5. 🤖 Model Details

| Model          | Type              | Framework        |
|---------------|------------------|------------------|
| YOLOv8        | One-stage        | Ultralytics      |
| RT-DETR       | Transformer      | Ultralytics      |
| Faster R-CNN  | Two-stage        | PyTorch          |

✔ Real-time vs accuracy comparison  
✔ Multiple architectures tested  

---

## 6. 📊 Training Details

### Dataset
- Helmet / No Helmet images  
- Labeled in YOLO format  

### Training Flow


Dataset
↓
Train / Validation Split
↓
Model Training
↓
Loss & Accuracy Monitoring
↓
Best Weights Saved


---

### 📈 Training Graphs (Add images here)

- Loss vs Epoch  
- Accuracy vs Epoch  

---

## 7. 📸 Results / Output

### Output Flow


Input Frame → Detection → Bounding Boxes → Label → FPS Display


### Sample Output (Add screenshots)

- Helmet detected (Green box)
- No Helmet detected (Red box)

---

### ⚡ Performance

| Model        | FPS (Normal) | FPS (Jetson Nano) |
|-------------|-------------|-------------------|
| YOLOv8      | High        | Medium            |
| RT-DETR     | Medium      | Low               |
| Faster RCNN | Low         | Very Low          |

---

## 8. ⚙️ Setup Instructions

### 📦 Install Dependencies

bash
pip install -r requirements.txt
▶️ Run Project
python main.py
⚙️ Configuration

Edit config.py:

Select model: yolo / rcnn / rtdetr
Set confidence threshold
Choose input source (webcam/video)



