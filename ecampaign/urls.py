from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from organisation.views import  OrganisationRegView, OrganisationRegisterView


urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='org_home'),
    url(r'^register/validate/$', OrganisationRegView.as_view(), name='register'),
    url(r'^register/$', OrganisationRegView.as_view(), name='register_org'),
    url(r'^success/$', TemplateView.as_view(template_name='organisation/success.html')),
    url(r'^admin/', include(admin.site.urls)),

]
