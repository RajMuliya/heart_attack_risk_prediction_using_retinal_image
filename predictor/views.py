from django.shortcuts import render,redirect
from .models import RetinalImage
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
label_names = ["Disease_Risk", "DR", "ARMD", "MH"]

@login_required(login_url='signin')
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        image_instance = RetinalImage(image=image_file)
        image_instance.save()
        image_path = image_instance.image.path

        # Load and preprocess image
        img = cv2.imread(image_path)
        if img is None:
            return render(request, 'upload.html', {'error': 'Could not load image.'})
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (512, 512))
        img = img / 255.0
        img_array = np.expand_dims(img, axis=0)

        # Predict
        predictions = model.predict(img_array)[0][:4]
        predicted_labels = (predictions > 0.5).astype(int)
        results = {
            label_names[i]: {
                'positive': bool(predicted_labels[i]),
                'probability': float(predictions[i]*100)
            } for i in range(len(label_names))
        }

        context = {
            'image_url': image_instance.image.url,
            'results': results
        }
        return render(request, 'result.html', context)

    return render(request, 'upload.html')



