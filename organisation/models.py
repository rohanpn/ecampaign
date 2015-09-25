from django.db import models

# Create your models here.

class organisation(models.Model):
    org_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
