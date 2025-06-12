# Heart Attack Risk Prediction from Retinal Images

**Predict heart attack risk using non-invasive retinal fundus image analysis and machine learning.**

---

## Overview

This project uses retinal image features to estimate heart attack risk.  
It includes:

- Image preprocessing and vessel feature extraction  
- Machine learning model training  
- Risk prediction from new images  
- Visualization of vessel segmentation  

---

## Project Structure

```
heart_attack_risk_prediction_using_retinal_image/
├── config.yaml                # Configuration for paths & parameters
├── dataset/                  
│   ├── train/                # Training images
│   ├── test/                 # Testing images
│   └── labels.csv            # Image IDs and corresponding labels
├── models/
│   └── model.pkl             # Trained machine learning model
├── test_images/
│   └── sample.jpg            # Test image for demo prediction
├── output/
│   └── vessel_segmentation.png  # Visualization output
├── utils/
│   └── image_processing.py   # Feature extraction utilities
├── preprocess.py             # Preprocess & feature extraction script
├── train_model.py            # Train ML model
├── predict.py                # Predict risk from image
├── visualize.py              # Generate vessel segmentation visual
├── test.py                   # CLI prediction test
├── requirements.txt          # Required Python packages
├── LICENSE                   # MIT License
└── README.md                 # You're reading it!
```

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/RajMuliya/heart_attack_risk_prediction_using_retinal_image.git
cd heart_attack_risk_prediction_using_retinal_image
```

2. **Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Data Setup

1. Add your images to the `dataset/` folder:

```
dataset/
├── train/
├── test/
└── labels.csv   # Format: image_id,label (0: no risk, 1: at risk)
```

2. Edit `config.yaml` with the correct paths to images and outputs.

---

## Preprocess Images

Extract features from images:

```bash
python preprocess.py
```

This step uses `image_processing.py` to extract vessel-related features.

---

## Train the Model

```bash
python train_model.py
```

This will:

- Load preprocessed features
- Train a classifier (Random Forest, etc.)
- Save the model as `models/model.pkl`

---

## Predict from Image

```bash
python predict.py --image test_images/sample.jpg
```

Outputs the **predicted heart attack risk score** (e.g. 0.72 means 72% risk).

---

## Quick Test CLI

```bash
python test.py --image test_images/sample.jpg
```

Shows result and risk confidence via terminal.

---

## Visualize Vessel Features

To highlight retinal vessels from an input image:

```bash
python visualize.py   --input test_images/sample.jpg   --output output/vessel_segmentation.png
```

---


##  Possible Extensions

- Add deep learning (CNN, transfer learning)
- Deploy using Flask/Django
- Add patient metadata (age, BP, etc.)
- Integrate Grad-CAM for explainability

---

## Troubleshooting

- `FileNotFoundError`: Check file paths in `config.yaml`  
- Image errors? Use `.jpg` or `.png` only  
- Model mismatch? Re-run preprocessing and training  

---

## License

This project is under the **MIT License**.  
See `LICENSE` for details.

---

## Contact

**Author**: Raj Muliya  
📧 Email: `raj.muliya0@gmail.com`  

---

## Contributing

1. Fork the repo  
2. Create a feature branch: `git checkout -b feature-name`  
3. Commit and push: `git commit -m "Feature"`  
4. Open a pull request

---

** If you found this useful, please star the repo!**
