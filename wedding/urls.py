from django.conf.urls import patterns, url
from wedding import views

urlpatterns = patterns('',
                       url(r'^$', views.root, name='weddingroot'),
                       url(r'^gallery/$', views.gallery, name='gallery'),
                       url(r"^pic/(\d+)/$", views.pic, name = "view_pic"),
                       )