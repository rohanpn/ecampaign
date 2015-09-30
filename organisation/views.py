from django.core.urlresolvers import reverse_lazy, reverse
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
    success_url = reverse_lazy("register_success")

    def get_success_url(self):
        return reverse('register_success', kwargs={"pk":self.object.id})



class ShowDomainView(DetailView):
    template_name = "organisation/success.html"

    def get_queryset(self):
        return Organisation.objects.filter(id=self.kwargs['pk'])


