from django.contrib import admin
from .models import RetinalImage, PredictionResult

# Register your models here.
admin.site.register(RetinalImage)
admin.site.register(PredictionResult)