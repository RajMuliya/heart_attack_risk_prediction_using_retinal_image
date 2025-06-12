# Heart Attack Risk Prediction using Retinal Images

## Overview
This innovative deep learning project predicts heart attack risk by analyzing retinal scans - a non-invasive window into cardiovascular health. By examining subtle patterns in retinal blood vessels, our CNN model identifies early warning signs of cardiac risk factors without traditional invasive tests.

**Core Concept**: The retina's microvasculature mirrors the body's cardiovascular system, allowing detection of abnormalities linked to heart disease through computer vision and deep learning.

## How It Works
The system analyzes key retinal features that correlate with cardiovascular health:

| Feature Analyzed | Medical Significance |
|------------------|----------------------|
| Blood vessel caliber | Arteriolar narrowing indicates hypertension |
| Arteriovenous ratio | Abnormal AVR suggests atherosclerosis |
| Microaneurysms | Early diabetic retinopathy marker |
| Hemorrhages | Vascular fragility indicator |
| Exudates | Lipid leakage from damaged vessels |

These features are processed through a custom convolutional neural network that outputs a **High Risk** or **Low Risk** prediction with probability score.

## Key Features
- **Web-based interface** for easy retinal scan uploads
- **Real-time risk assessment** with visual feedback
- **Model interpretability** through activation heatmaps
- **Medical-grade analysis** without invasive procedures
- **Responsive design** works on desktop and mobile
- **Detailed PDF report** generation (planned feature)

## Project Structure
```bash
heart_attack_risk_prediction_using_retinal_image/
├── app.py                   # Flask application entry point
├── requirements.txt         # Python dependencies
├── model/                   
│   ├── model.h5             # Trained Keras model (94MB)
│   └── preprocessor.pkl     # Image preprocessing pipeline
├── static/                  
│   ├── css/                 # Bootstrap custom styles
│   ├── js/                  # Interactive elements
│   └── uploads/             # User-submitted images (auto-cleared)
├── templates/               
│   ├── index.html           # Main interface
│   └── result.html          # Results dashboard
├── notebooks/               # Research notebooks
│   ├── retinal_analysis.ipynb  # EDA and visualization
│   └── model_training.ipynb    # CNN architecture experiments
├── test.py                  # CLI prediction tester
└── README.md                # Project documentation
