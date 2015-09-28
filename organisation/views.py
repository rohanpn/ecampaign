from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import FormView
from .models import Organisation
from django.views.generic.base import View
from organisation.forms import OrganisationRegistrationForm


class OrganisationRegisterView(View):
    """
        To register the Organisation and create a domain for the registered Organisation.

    """
    def post(self, *args, **kwargs):
        request = self.request
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        form = OrganisationRegistrationForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['org_name'] == None:
                return render(self.request, 'register_org.html', { "error" : "Organisation with the given name already"
                                                                             " exist. Please select some other name."})
            if password != confirm_password:
                return render(self.request, 'register_org.html', { "error" : "Password didn't match"})
            else:
                Organisation.objects.create(org_name=form.cleaned_data['org_name'],
                                            address=form.cleaned_data['address'],
                                            pin_code=form.cleaned_data['address'],
                                            first_name=form.cleaned_data['first_name'],
                                            last_name=form.cleaned_data['last_name'],
                                            email=form.cleaned_data['email'],
                                            phone=form.cleaned_data['phone'],
                                            password=form.cleaned_data['password'])
        else:
            return render(self.request,'register_org.html', {"error": "please enter valid details"})

        return render(self.request, 'organisation/success.html', {'org_name': form.cleaned_data["org_name"]})


