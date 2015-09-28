from django.db import models

# Create your models here.

class Organisation(models.Model):

    org_name = models.CharField(max_length=50, unique=True, help_text="Name of the organisation you want.")
    address = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.org_name
