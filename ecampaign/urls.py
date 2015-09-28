from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from organisation.views import OrganisationRegisterView



urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='home.html'), name='org_home'),
    url(r'^register/$', TemplateView.as_view(template_name='register_org.html'), name='register_org'),
    # url(r'^register/validate/$', RegisterView.as_view(), name='register'),
    url(r'^register/validate/$', OrganisationRegisterView.as_view(), name='register'),
    url(r'^success/$', TemplateView.as_view(template_name='organisation/success.html')),
    url(r'^admin/', include(admin.site.urls)),

]
