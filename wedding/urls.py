from django.conf.urls import patterns, url
from wedding import views

urlpatterns = patterns('',
                       url(r'^$', views.root, name='weddingroot'),
                       )