from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='blogindex'),
                       url(r'^post/$', views.blogpost, name='blogpost'),
                       url(r'^view/(\d+)/$', views.viewblogpost, name='blogview'),
                       #url(r'^debug/$', views.debug, name='debug'),
                       )