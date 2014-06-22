from django.conf.urls import patterns, url
from wedding import views

urlpatterns = patterns('',
                       url(r'^$', views.gallery, name='weddingroot'),
                       url(r'^gallery/$', views.gallery, name='gallery'),
                       url(r'^gallery/(\d+)/$', views.gallery, name = 'gallery'),
                       url(r'^pic/(?P<pic_name>\S+)$', views.pic, name="view_pic"),
                       )
