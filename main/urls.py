"""Configuration of main URLs for KovalAgent project."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.equipment, name='equipment'),
    url(r'^iteam_details/(?P<pk>[0-9]+)/$', views.iteam_details, name='iteam_details'),
    url(r'^change_status/$', views.change_status, name='change_status'),
    url(r'^logs/$', views.logs, name='logs'),
    url(r'^update_content/(?P<sort_by>.*)/$', views.update_content, name='update_content'),
]
