from django.core.exceptions import ValidationError


__author__ = 'rohan'

from django  import forms
from django.db import IntegrityError
from organisation.models import Organisation

class OrganisationRegistrationForm(forms.ModelForm):
    """
        To Register the Organisation
    """
    confirm_password = forms.CharField(max_length=30)
    class Meta:
        model = Organisation
        fields = '__all__'



    def clean_org_name(self, *args, **kwargs):
        data = self.cleaned_data['org_name']
        if Organisation.objects.filter(org_name=data).exists():
            raise ValidationError("Organisation name already exists.")
        return data

    def clean_password(self, *args, **kwargs):
        data = self.cleaned_data['password']
        import ipdb;ipdb.set_trace()
        if data != self.data['confirm_password']:
            raise ValidationError("Password didn't match.")
        return data
