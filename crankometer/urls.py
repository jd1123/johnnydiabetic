from django.conf.urls import patterns, url
from crankometer import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='crankometer_index'),
                       url(r'^vote/$', views.vote, name='vote'),
                       #url(r'^edit/(\d+)/$', views.blogpost, name='blogedit'),
                       #url(r'^view/(\d+)/$', views.viewblogpost, name='blogview'),
                       #url(r'^debug/$', views.debug, name='debug'),
                       )
