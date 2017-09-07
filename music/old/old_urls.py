from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [
    # /music
    url(r'^$', views.index, name='index'),
    
    # /music/712
    # album_id is a variable to be passed
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/album_id/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
    
]
