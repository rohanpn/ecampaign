from django.core.exceptions import ValidationError


__author__ = 'rohan'

from django  import forms
from django.db import IntegrityError
from organisation.models import Organisation

class OrganisationRegistrationForm(forms.ModelForm):
    """
        To Register the Organisation
    """
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    class Meta:
        model = Organisation
        exclude=['sub_domain']
        widgets={
            'password' : forms.PasswordInput
        }

    def clean(self):
        cleaned_data = super(OrganisationRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("Password didn't match.")

    def clean_org_name(self, *args, **kwargs):
        data = self.cleaned_data['org_name']
        if Organisation.objects.filter(org_name=data).exists():
            raise ValidationError("Organisation name already exists.")
        return data

    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']



class OrganisationDomainForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields= ('sub_domain',)

    def clean_sub_domain(self):
        data =self.cleaned_data['sub_domain']
        if Organisation.objects.filter(sub_domain=data).exists():
            raise ValidationError("This Sub-domain is not available. Please enter different name.")
        return data
