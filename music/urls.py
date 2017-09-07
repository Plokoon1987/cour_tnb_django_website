from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [
    # /music
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # /music/712
    # album_id is a variable to be passed
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]
