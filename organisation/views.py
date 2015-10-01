from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, render, redirect
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from .models import Organisation
from organisation.forms import OrganisationRegistrationForm, OrganisationDomainForm


# Create your views here.


class OrganisationRegView(CreateView):
    """
        To register the Organisation.
    """
    model = Organisation
    template_name = "organisation/register_org.html"
    form_class = OrganisationRegistrationForm

    def get_success_url(self):
        return reverse('register_domain', kwargs={"pk":self.object.id})


class RegisterDomainView(UpdateView):
    """
        To register the domain to the Organisation
    """
    model = Organisation
    template_name = "organisation/register_domain.html"
    form_class = OrganisationDomainForm

    def get_success_url(self):
        return reverse('register_success', kwargs={"pk":self.object.id})



class ShowDomainView(DetailView):
    """
        Display the url of the registered organisation.
    """
    template_name = "organisation/success.html"
    queryset = Organisation.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ShowDomainView, self).get_context_data()
        if self.request.META['SERVER_NAME']:
            context['host'] = self.request.META['SERVER_NAME']
        elif self.request.META['HTTP_HOST']:
            context['host'] = self.request.META['HTTP_HOST']
        return context



class CheckDomainView(CreateView):
    """
        If the Organisation is not registered route it to register page else route it to
        the dashboard of the organisation.
    """
    def get(self, *args, **kwargs):
        host = self.request.META['HTTP_HOST']
        server = self.request.META['SERVER_NAME']
        host = host.split(":")
        if host[0] == server:
            return redirect(reverse('org_home'))
        else:
            return render(self.request, "organisation/org_login.html")

