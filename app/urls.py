from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^bbc/$', views.getXmlBBC),
    url(r'^cnn/$', views.getRssCNN),
]