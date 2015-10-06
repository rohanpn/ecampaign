import re
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django  import forms
from organisation.models import Organisation
from django.core.validators import RegexValidator



class OrganisationRegistrationForm(forms.ModelForm):
    """
        To Register the Organisation
    """
    confirm_password = forms.CharField(max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = Organisation
        exclude=['sub_domain']
        widgets={
            'password' : forms.PasswordInput,
            'pin_code' : forms.NumberInput
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

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        check = re.compile(r'^[a-zA-Z]*$')
        if check.match(data) == None:
            raise ValidationError("First Name should contain only alphabets.")
        return data

    def clean_last_name(self):
        data=self.cleaned_data['last_name']
        check = re.compile(r'^[a-zA-Z]*$')
        if check.match(data) == None:
            raise ValidationError("Last Name should contain only alphabets.")
        return data

    def clean_phone(self):
        data =self.cleaned_data['phone']
        check = re.compile(r'^\+?1?\d{9,15}$')
        if check.match(data) == None:
            raise ValidationError("Phone number format should be +99999999999 and can contain upto 15 digits.")
        return data

    def clean_pin_code(self):
        data=self.cleaned_data['pin_code']
        check = re.compile(r'[0-9]+$')
        if check.match(data) == None:
            raise ValidationError("Pin Code should not contain alphabets.")
        return data


class OrganisationDomainForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields= ('sub_domain',)

    def clean_sub_domain(self):
        data =self.cleaned_data['sub_domain']
        if Organisation.objects.filter(sub_domain=data).exists():
            raise ValidationError("This sub-domain is not available. Please enter different name.")
        check = re.compile(r'^[a-zA-Z0-9-]*$')
        if check.match(data) == None:
            raise ValidationError("The sub-domain should contain only numbers and characters")
        return data



class OrganisationLoginForm(forms.Form):
    email_id = forms.EmailField()
    password= forms.CharField(widget=forms.PasswordInput)
    domain = forms.CharField(widget=forms.HiddenInput)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput)

    def clean(self):

        cleaned_data = super(OrganisationLoginForm, self).clean()
        domain = cleaned_data['domain']
        domain = domain.split(".")
        sub_domain = domain[0]
        cleaned_data['sub_domain'] = sub_domain

        if Organisation.objects.filter(sub_domain=sub_domain).exists():
            object = Organisation.objects.get(sub_domain=sub_domain)
            if object.email != cleaned_data['email_id'] or object.password != cleaned_data['password']:
                raise ValidationError("Email Id or password did not match.")
            else:
                return cleaned_data
        else:
            raise ValidationError("No such domain exist.")


