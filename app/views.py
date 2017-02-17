import urllib

from django.http import HttpResponse
from django.shortcuts import render
from xml.etree import ElementTree
import feedparser

# Create your views here.
def index(request):
    return render(request, "app/main.html")


def getXmlBBC(request):
    feed = urllib.urlopen('http://feeds.bbci.co.uk/news/rss.xml')
    response = HttpResponse(feed, content_type='application/xml')
    return response

def getRssCNN(request):
    feed = urllib.urlopen('http://rss.cnn.com/rss/cnn_topstories.rss')
    response = HttpResponse(feed, content_type='application/xml')
    return response




