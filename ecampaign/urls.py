from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from organisation.forms import OrganisationDomainForm
from organisation.views import  OrganisationRegView, RegisterDomainView, ShowDomainView, CheckDomainView



urlpatterns = [

    url(r'^$', CheckDomainView.as_view(), name='check_domain'),
    url(r'^register_org/$', OrganisationRegView.as_view(template_name='home.html'), name='org_home'),
    url(r'^register/validate/$', OrganisationRegView.as_view(), name='register'),
    url(r'^register/$', OrganisationRegView.as_view(), name='register_org'),
    url(r'^register/(?P<pk>[0-9]+)$', RegisterDomainView.as_view(form_class=OrganisationDomainForm),
                                                                 name="register_domain"),
    url(r'^success/(?P<pk>[0-9]+)$', ShowDomainView.as_view(template_name="organisation/success.html"), name="register_success"),
    url(r'^(?P<org_domain>\w+)$', TemplateView.as_view(template_name="organisation/org_login.html"), name="org_dashboard"),
    url(r'^admin/', include(admin.site.urls)),


]
