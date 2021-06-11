from django.db import models

# Create your models here.
class job(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)


