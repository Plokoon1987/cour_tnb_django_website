from django.conf.urls import url, include
from . import views

urlpatterns = [
    # /music
    url(r'^$', views.index, name='index'),
    
    #/music/712
    # album_id is a variable to be passed
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
