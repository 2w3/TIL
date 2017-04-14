from django.conf.urls import url
from django.views.generic import ListView, DetailView

from photo.views import Album, Photo

urlpatterns = [
    url(r'^$', ListView.as_view(model=Album), name='index'),
    url(r'^album/$', ListView.as_view(model=Album), name='album_list'),
    url(r'^album/(?P<pk>\d+)/$', DetailView.as_view(model=Album), name='album_detail'),
    url(r'^photo/(?P<pk>\d+)/$', DetailView.as_view(model=Photo), name='photo_detail'),
]
