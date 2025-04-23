from django.db import models

# Create your models here.
class RetinalImage(models.Model):
    image = models.ImageField(upload_to='retinal_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PredictionResult(models.Model):
    image = models.ForeignKey(RetinalImage, on_delete=models.CASCADE)
    predicted_at = models.DateTimeField(auto_now_add=True)

    # Disease Risk
    disease_risk_positive = models.BooleanField()
    disease_risk_probability = models.FloatField()

    # Diabetic Retinopathy (DR)
    dr_positive = models.BooleanField()
    dr_probability = models.FloatField()

    # ARMD
    armd_positive = models.BooleanField()
    armd_probability = models.FloatField()

    # MH
    mh_positive = models.BooleanField()
    mh_probability = models.FloatField()