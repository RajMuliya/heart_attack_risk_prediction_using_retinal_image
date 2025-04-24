from django.shortcuts import render,redirect
from .models import RetinalImage, PredictionResult
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import cv2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re

# Load the model once when the server starts
MODEL_PATH = 'E:/Project/Material/Code/multi_label_heart_risk_model_second.keras'  # Update this path
model = load_model(MODEL_PATH)
label_names = ["Disease_Risk", "DR", "ARMD", "MH","DN"]

@login_required(login_url='signin')
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        
        # Open and preprocess image
        img = Image.open(image_file)
        img = img.convert('RGB')
        img = img.resize((512, 512))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        predictions = model.predict(img_array)[0][:5]
        predicted_labels = (predictions > 0.5).astype(int)
        
        results = {
            label_names[i]: {
                'positive': bool(predicted_labels[i]),
                'probability': float(predictions[i] * 100)
            } for i in range(len(label_names))
        }

        # Save image to DB
        image_instance = RetinalImage.objects.create(image=image_file)

        # Save prediction to DB
        PredictionResult.objects.create(
            image=image_instance,
            disease_risk_positive1=predicted_labels[0],
            disease_risk_probability=float(predictions[0] * 100),
            dr_positive=predicted_labels[1],
            dr_probability=float(predictions[1] * 100),
            armd_positive=predicted_labels[2],
            armd_probability=float(predictions[2] * 100),
            mh_positive=predicted_labels[3],
            mh_probability=float(predictions[3] * 100),

            dn_positive=predicted_labels[4],
            dn_probability=float(predictions[4] * 100),
        )

        context = {
            'image_url': image_instance.image.url,
            'results': results
        }
        return render(request, 'result.html', context)

    return render(request, 'upload.html')


def aboutpage(request):
    return render(request,"about.html")

def faqpage(request):
    return render(request,"faq.html")

def hitw(request):
    return render(request,"how_it_works.html")


