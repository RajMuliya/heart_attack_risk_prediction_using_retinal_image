from django.shortcuts import render,redirect
from .models import PredictionResult
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import cv2
import base64
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import re
from io import BytesIO

# Load the model once when the server starts
MODEL_PATH = 'E:/Project/Material/Code/multi_label_heart_risk_model_second.keras'  # Update this path
model = load_model(MODEL_PATH)
label_names = ["Disease_Risk", "DR", "ARMD", "MH","DN"]

@login_required(login_url='signin')
def upload_image(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']

        # Read the image from memory
        file_bytes = image_file.read()
        np_arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if img is None:
            return render(request, 'upload.html', {'error': 'Could not load image.'})

        # Preprocess the image
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resized_img = cv2.resize(img_rgb, (512, 512))
        normalized_img = resized_img / 255.0
        img_array = np.expand_dims(normalized_img, axis=0)

        # Predict
        predictions = model.predict(img_array)[0][:5]
        predicted_labels = (predictions > 0.5).astype(int)

        results = {
            label_names[i]: {
                'positive': bool(predicted_labels[i]),
                'probability': float(predictions[i] * 100)
            } for i in range(len(label_names))
        }

        # Save prediction result to DB (no image saved to file system)
        pred = PredictionResult.objects.create(
            disease_risk_positive=predicted_labels[0],
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

        # Convert image to base64 for inline display
        pil_img = Image.fromarray(resized_img)
        buffer = BytesIO()
        pil_img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()

        context = {
            'image_base64': img_str,
            'results': results
        }
        return render(request, 'result.html', context)

    return render(request, 'upload.html')


@login_required(login_url='signin')
def aboutpage(request):
    return render(request,"about.html")

@login_required(login_url='signin')
def faqpage(request):
    return render(request,"faq.html")

@login_required(login_url='signin')
def hitw(request):
    return render(request,"how_it_works.html")


