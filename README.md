# 🛡️ SentinelSight AI

### AI-Powered Weapon Detection Using YOLOv3 and OpenCV

**SentinelSight AI** is a computer vision project that explores automated weapon detection using the YOLOv3 object detection model and OpenCV.

The application analyzes visual input to identify objects matching the weapon classes supported by its trained model. Detected objects can be highlighted with bounding boxes and confidence scores to help users review potential security concerns.

The project demonstrates how deep learning and computer vision can support visual threat screening in controlled environments.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Objectives](#-objectives)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Model Configuration](#-model-configuration)
- [Limitations](#-limitations)
- [Future Scope](#-future-scope)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

Automated visual threat screening is an important area of computer vision research. Manually reviewing large numbers of images or video frames can be time-consuming, making automated object detection a useful tool for assisting human reviewers.

SentinelSight AI uses YOLOv3, a real-time object detection architecture, with OpenCV's deep neural network module to process visual input and identify supported object classes.

The project focuses on object detection, visual annotations, and confidence-based filtering.

## 🚨 Problem Statement

Traditional visual security monitoring can require significant human attention, particularly when reviewing large volumes of imagery.

A computer vision system can assist by highlighting objects that match trained weapon categories, allowing a reviewer to investigate flagged frames more efficiently.

However, automated detections may contain false positives or miss objects. Therefore, the system is intended to support human review rather than make security decisions independently.

## 🎯 Objectives

- Implement weapon detection using YOLOv3.
- Process images or other input sources supported by the implementation.
- Identify objects belonging to the model's trained classes.
- Display bounding boxes and confidence scores.
- Provide a foundation for future security-monitoring research.
- Explore the integration of deep learning with OpenCV.

## ✨ Features

### 🔍 1. AI-Based Object Detection

Uses a YOLOv3 model to identify supported object classes in visual input.

### 🖼️ 2. Visual Detection Results

Displays detected objects with bounding boxes and labels where supported by the implementation.

### 📊 3. Confidence-Based Filtering

Allows detections to be filtered using confidence thresholds, helping control which predictions are displayed.

### ⚡ 4. Computer Vision Processing

Uses OpenCV to load the model, process images or frames, and handle detection output.

### 🔧 5. Configurable Model Files

Supports the YOLO configuration, trained weights, and class-label files required by the implementation.

### 🧪 6. Extensible Research Prototype

Provides a starting point for experimentation with model improvements, video processing, and evaluation methods.

*Actual input modes and features depend on the scripts and model files available in the repository.*

---

## 🔄 How It Works

```text
       Input Image or Frame
                |
                v
        Image Preprocessing
                |
                v
       Load YOLOv3 Network
                |
                v
       Object Detection
                |
                v
     Confidence Thresholding
                |
                v
       Filter Predictions
                |
                v
     Bounding Boxes and Labels
                |
                v
       Visual Result Review
```

### Workflow Explanation

1. Load an image or frame supported by the program.
2. Preprocess the input into the format expected by YOLOv3.
3. Run inference using the configured network weights.
4. Filter predictions according to confidence and detection settings.
5. Draw bounding boxes and labels for accepted detections.
6. Display or save the results, depending on the implementation.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| YOLOv3 | Object detection |
| OpenCV | Image processing and model inference |
| NumPy | Numerical operations and array handling |

---

## 📁 Project Structure

```text
SentinelSight-AI/
│
├── main.py
├── tempCodeRunnerFile.py
├── weapon-detection-main.zip
└── README.md
```

This is the currently visible repository structure at a high level. Extract the archive and inspect its contents to identify any additional scripts, model configuration files, weights, labels, datasets, or dependency files required to run the application.

A cleaned-up structure for future development could look like this:

```text
SentinelSight-AI/
│
├── src/
│   └── main.py
├── models/
│   ├── yolov3.cfg
│   ├── yolov3.weights
│   └── classes.txt
├── samples/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

The second tree is a suggested organization, not a claim that those files already exist.

---

## 🚀 Getting Started

### Prerequisites

Install:

- Python 3
- pip
- OpenCV
- NumPy
- The YOLOv3 configuration, trained weights, and class labels expected by the program

### 1. Clone the Repository

```bash
git clone https://github.com/Rehan-070/Weapon-Detection-using-YOLOv3-OpenCV-.git
cd Weapon-Detection-using-YOLOv3-OpenCV-
```

### 2. Create a Virtual Environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

If the repository contains `requirements.txt`, run:

```bash
pip install -r requirements.txt
```

Otherwise, install the common dependencies:

```bash
pip install opencv-python numpy
```

### 4. Prepare the Model Files

Check the source code for the exact paths used to load the model configuration, weights, and class labels.

Make sure all required files are present before running inference. The model must have been trained or configured to detect the intended weapon classes; a generic object detection model will not automatically recognize every weapon.

### 5. Run the Application

Run the main script from the repository root:

```bash
python main.py
```

If the project uses additional input arguments or a different entry point, follow the instructions in the source code.

---

## ⚙️ Model Configuration

YOLOv3 implementations using OpenCV's DNN module commonly require:

- **Configuration file:** Defines the neural network architecture.
- **Weights file:** Contains the learned model parameters.
- **Class-label file:** Maps model output indices to class names.

Example OpenCV model-loading pattern:

```python
import cv2

config_path = "models/yolov3.cfg"
weights_path = "models/yolov3.weights"

net = cv2.dnn.readNetFromDarknet(
    config_path,
    weights_path
)
```

This snippet demonstrates model loading only. The filenames and paths must match the model files used by your project.

Use model weights from a trusted source and verify the model's intended classes, licensing, and evaluation results.

---

## ⚠️ Limitations

- **Detection accuracy:** Performance depends on the dataset, training procedure, and model quality.
- **False positives:** Ordinary objects may be incorrectly flagged.
- **False negatives:** Weapons may be missed because of occlusion, image quality, distance, or unusual viewpoints.
- **Class limitations:** The model can only reliably detect categories it has learned to recognize.
- **Input limitations:** Real-time webcam or video support should not be assumed unless implemented and tested.
- **Operational safety:** Predictions are not proof that a weapon is present and should be independently reviewed.

SentinelSight AI is an experimental computer vision project, not a certified security system.

---

## 🔮 Future Scope

- [ ] Add a clean command-line interface for image and video input.
- [ ] Improve model evaluation using precision, recall, and mAP.
- [ ] Add support for configurable confidence and non-maximum suppression thresholds.
- [ ] Build a user-friendly image upload interface.
- [ ] Add video-frame processing where appropriate.
- [ ] Improve logging and error handling.
- [ ] Create automated tests using authorized test images.
- [ ] Document dataset provenance and model limitations.
- [ ] Add reproducible environment and setup instructions.
- [ ] Evaluate newer detection architectures against a documented benchmark.

---

## 🤝 Contributing

Contributions that improve reliability, documentation, testing, and model evaluation are welcome.

1. Fork the repository.
2. Create a branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Implement and test your changes.
4. Commit your changes:

   ```bash
   git commit -m "Improve: describe your change"
   ```

5. Push your branch:

   ```bash
   git push origin feature/your-feature
   ```

6. Open a pull request with a description of the changes.

Please avoid committing private surveillance footage, personal information, credentials, or datasets without appropriate authorization.

---

## 📄 License

Check whether the repository includes a `LICENSE` file and review the licenses of the source code, model weights, and datasets.

If no license is present, contact the repository owner before redistributing or reusing the project.

---

## 👨‍💻 Project Information

**Project Name:** SentinelSight AI  
**Category:** Artificial Intelligence · Computer Vision · Object Detection  
**Core Technologies:** Python · YOLOv3 · OpenCV

**Repository:** [Weapon-Detection-using-YOLOv3-OpenCV-](https://github.com/Rehan-070/Weapon-Detection-using-YOLOv3-OpenCV-)

### Our Vision

To explore how computer vision can assist human reviewers in identifying potentially dangerous objects and improving the efficiency of visual security screening.

**SentinelSight AI — See potential threats. Support informed review.**
