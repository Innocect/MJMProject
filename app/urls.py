from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^bbc/$', views.get_bbc_rss),
    url(r'^cnn/$', views.get_cnn_rss),
]