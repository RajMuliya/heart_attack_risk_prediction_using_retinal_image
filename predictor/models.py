from django.db import models

# Create your models here.
from django.db import models

class RetinalImage(models.Model):
    image = models.ImageField(upload_to='retinal_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)