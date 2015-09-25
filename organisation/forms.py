__author__ = 'rohan'

import forms
from . import models

class organisationForm(forms.Form):
    org_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    pin_code = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    password = forms.CharField()


    def clean_org_name(self):
        pass

    def clean_address(self):
        pass

    def clean_pin_code(self):
        pass

    def clean_first_name(self):
        pass

    def clean_last_name(self):
        pass

    def clean_email(self):
        pass
