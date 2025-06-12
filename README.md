Heart Attack Risk Prediction using Retinal Images
Overview
This innovative project leverages retinal scans to predict an individual's risk of heart attack using deep learning. By analyzing patterns in retinal blood vessels, this system identifies cardiovascular risk factors non-invasively. The solution combines a Convolutional Neural Network (CNN) with a web interface for easy risk assessment.

https://static/demo.gif Example of the web interface in action

How It Works
The retina provides a unique window into cardiovascular health. Our deep learning model analyzes:

Blood vessel patterns and abnormalities

Arteriovenous ratios

Microvascular changes

Hemorrhages and exudates

These features are processed through a custom CNN architecture that outputs a heart attack risk prediction (High/Low Risk).

Key Features
Web-based interface for easy image uploads

Instant risk assessment with visual feedback

Model interpretability through activation maps

Responsive design works on any device

Medical-grade analysis without invasive procedures

Project Structure
text
├── app.py                   # Main Flask application
├── requirements.txt         # Python dependencies
├── model/                   
│   ├── model.h5             # Trained Keras model
│   └── preprocessor.pkl     # Image preprocessing pipeline
├── static/                  # Web assets
│   ├── css/
│   ├── js/
│   └── uploads/             # User-uploaded images
├── templates/               # HTML templates
│   ├── index.html           # Main interface
│   └── result.html          # Results page
├── notebooks/               # Jupyter notebooks
│   ├── retinal_image_analysis.ipynb  # EDA and visualization
│   └── ha_risk_prediction.ipynb      # Model training
├── test.py                  # Model testing script
└── README.md                # Project documentation
Getting Started
Prerequisites
Python 3.7+

pip

Installation
Clone the repository:

bash
git clone https://github.com/RajMuliya/heart_attack_risk_prediction_using_retinal_image.git
cd heart_attack_risk_prediction_using_retinal_image
Install dependencies:

bash
pip install -r requirements.txt
Running the Application
bash
python app.py
Visit http://localhost:5000 in your browser

Using the Web Interface
Click "Upload Image"

Select a retinal scan (JPG/PNG)

View your risk assessment

Explore detailed analysis

Model Development
The deep learning workflow includes:

Data Preparation:

Image normalization

Contrast enhancement

Vessel segmentation

CNN Architecture:

python
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])
Training:

Dataset: RETINA dataset

Optimizer: Adam (lr=0.0001)

Loss: Binary Crossentropy

Augmentation: Rotation, flipping, zoom

Testing the Model
Run standalone predictions:

bash
python test.py --image path/to/retinal_image.jpg
Results
Our model achieved:

Accuracy: 87.2%

Sensitivity: 89.1%

Specificity: 85.3%

AUC-ROC: 0.92

https://static/confusion_matrix.png
Model performance metrics

Limitations & Future Work
Current limitations:

Limited to high-quality retinal scans

Doesn't incorporate clinical history

Validation needed on diverse populations

Future enhancements:

Mobile application integration

3D retinal scan analysis

Multi-modal data fusion (ECG + retinal)

Real-time physician collaboration tools

Ethical Considerations
Patient privacy: All uploads are temporarily stored

Medical disclaimer: Predictions are screening tools, not diagnoses

Bias mitigation: Ongoing work to improve model fairness

Contributing
We welcome contributions! Please:

Fork the repository

Create your feature branch

Submit a pull request

For major changes, open an issue first to discuss proposed changes.

License
Distributed under the MIT License. See LICENSE for more information.

Contact
Raj Muliya - @rajmuliya
Project Link: https://github.com/RajMuliya/heart_attack_risk_prediction_using_retinal_image
