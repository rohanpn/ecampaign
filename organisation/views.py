from django.shortcuts import render

# Create your views here.
from . import models
from django.views.generic.base import View
from django.views.generic.edit import CreateView


class RegisterFormValidate(CreateView):
    model = models.organisation

    def post(self, *args, **kwargs):
        import ipdb;ipdb.set_trace()
        return render(self.request,'home.html')

