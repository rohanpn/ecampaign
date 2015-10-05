from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Organisation(models.Model):

    org_name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=15)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    sub_domain = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.org_name

    def get_sub_domain(self):
        return self.sub_domain
