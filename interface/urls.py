__author__ = 'Syn'
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^demo/config/$', views.demo_config, name='demo_config'),
    url(r'^$', views.demo_controls, name='demo_controls'),
    url(r'^jif/config/$', views.jif_config, name='jif_config'),
    url(r'^start_demo/$', views.start_demo, name='start_demo'),
    url(r'^stop_demo/$', views.stop_demo, name='stop_demo'),
]
