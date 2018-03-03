"""Configuration of main URLs for KovalAgent project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.equipment, name='equipment'),
    url(r'^iteam_details/(?P<pk>[0-9]+)/$', views.iteam_details, name='iteam_details'),
]
