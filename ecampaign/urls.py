from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from organisation.views import RegisterFormValidate



urlpatterns = [
    # Examples:
    # url(r'^$', 'ecampaign.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='org_home'),
    url(r'^register/$', TemplateView.as_view(template_name='register_org.html'), name='reg_org'),
    url(r'^register/validate/$', RegisterFormValidate.as_view(), name='register'),
    url(r'^admin/', include(admin.site.urls)),

]
