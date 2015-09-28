



__author__ = 'rohan'

from django  import forms
from django.db import IntegrityError
from organisation.models import Organisation

class OrganisationRegistrationForm(forms.Form):
    """
        To Register the Organisation
    """
    model = Organisation
    org_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=100)
    pin_code = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    password = forms.CharField()

    def clean_org_name(self):
        data = self.cleaned_data['org_name']
        if Organisation.objects.filter(org_name=data).exists():
            return None
        return data
