import urllib

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "app/main.html")


def get_bbc_rss(request):
    feed = urllib.urlopen('http://feeds.bbci.co.uk/news/rss.xml')
    return HttpResponse(feed, content_type='application/xml')


def get_cnn_rss(request):
    feed = urllib.urlopen('http://rss.cnn.com/rss/cnn_topstories.rss')
    return HttpResponse(feed, content_type='application/xml')

