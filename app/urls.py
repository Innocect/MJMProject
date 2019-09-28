from django.conf.urls import url
from app import views


urlpatterns = [
    url(r'^$', views.index),
    url('bbc/', views.get_bbc_rss),
    url('cnn/', views.get_cnn_rss),
]