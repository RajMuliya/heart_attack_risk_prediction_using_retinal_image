from django.db import models

class PredictionResult(models.Model):
    predicted_at = models.DateTimeField(auto_now_add=True)

    disease_risk_positive = models.BooleanField()
    disease_risk_probability = models.FloatField()

    dr_positive = models.BooleanField()
    dr_probability = models.FloatField()

    armd_positive = models.BooleanField()
    armd_probability = models.FloatField()

    mh_positive = models.BooleanField()
    mh_probability = models.FloatField()

    dn_positive = models.BooleanField()
    dn_probability = models.FloatField()
