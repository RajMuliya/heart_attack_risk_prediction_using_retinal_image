# ❤️ Heart Attack Risk Prediction from Retinal Images

**Predict heart attack risk using non-invasive retinal fundus image analysis and machine learning.**

---

## 📌 Overview

This project uses retinal image features to estimate heart attack risk.  
It includes:

- ✅ Image preprocessing and vessel feature extraction  
- ✅ Machine learning model training  
- ✅ Risk prediction from new images  
- ✅ Visualization of vessel segmentation  

---

## 📁 Project Structure

heart_attack_risk_prediction_using_retinal_image/
├── config.yaml # Configuration for paths & parameters
├── dataset/
│ ├── train/ # Training images
│ ├── test/ # Testing images
│ └── labels.csv # Image IDs and corresponding labels
├── models/
│ └── model.pkl # Trained machine learning model
├── test_images/
│ └── sample.jpg # Test image for demo prediction
├── output/
│ └── vessel_segmentation.png # Visualization output
├── utils/
│ └── image_processing.py # Feature extraction utilities
├── preprocess.py # Preprocess & feature extraction script
├── train_model.py # Train ML model
├── predict.py # Predict risk from image
├── visualize.py # Generate vessel segmentation visual
├── test.py # CLI prediction test
├── requirements.txt # Required Python packages
├── LICENSE # MIT License
└── README.md # You're reading it!

yaml
Copy
Edit

---

## 🛠️ Installation

1. **Clone the repository**


git clone https://github.com/RajMuliya/heart_attack_risk_prediction_using_retinal_image.git
cd heart_attack_risk_prediction_using_retinal_image
Create a virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
🗂️ Data Setup
Add your images to the dataset/ folder:

bash
Copy
Edit
dataset/
├── train/
├── test/
└── labels.csv   # Format: image_id,label (0: no risk, 1: at risk)
Edit config.yaml with the correct paths to images and outputs.

🔍 Preprocess Images
Extract features from images:

bash
Copy
Edit
python preprocess.py
This step uses image_processing.py to extract vessel-related features.

🧠 Train the Model
bash
Copy
Edit
python train_model.py
This will:

Load preprocessed features

Train a classifier (Random Forest, etc.)

Save the model as models/model.pkl

🤖 Predict from Image
bash
Copy
Edit
python predict.py --image test_images/sample.jpg
Outputs the predicted heart attack risk score (e.g. 0.72 means 72% risk).

🧪 Quick Test CLI
bash
Copy
Edit
python test.py --image test_images/sample.jpg
Shows result and risk confidence via terminal.

🎨 Visualize Vessel Features
To highlight retinal vessels from an input image:

bash
Copy
Edit
python visualize.py \
  --input test_images/sample.jpg \
  --output output/vessel_segmentation.png
📊 Scientific Background
Several studies show that retinal vascular morphology reflects cardiovascular health.
For instance, Poplin et al. (2018, Nature Biomedical Engineering) predicted cardiac events using fundus images with AUC ≈ 0.70.

🚀 Possible Extensions
Add deep learning (CNN, transfer learning)

Deploy using Flask/Django + Docker

Add patient metadata (age, BP, etc.)

Integrate Grad-CAM for explainability

🧰 Troubleshooting
⚠️ FileNotFoundError: Check file paths in config.yaml

🖼 Image errors? Use .jpg or .png only

🧠 Model mismatch? Re-run preprocessing and training

📝 License
This project is under the MIT License.
See LICENSE for details.

🙋‍♂️ Contact
Author: Raj Muliya
📧 Email: raj.muliya@example.com
🔗 GitHub: @RajMuliya

🤝 Contributing
Fork the repo

Create a feature branch: git checkout -b feature-name

Commit and push: git commit -m "Feature"

Open a pull request
