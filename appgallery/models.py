from django.db import models

# Create your models here.
class gallery(models.Model):
    photo = models.ImageField(upload_to='media')
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
