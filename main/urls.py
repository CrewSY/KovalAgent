"""Configuration of main URLs for KovalAgent project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.equipment, name='equipment'),
]
