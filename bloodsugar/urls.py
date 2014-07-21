from django.conf.urls import patterns, include, url
from bloodsugar import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", views.root, name="root"),
    url(r'^data/$', views.data, name="data"),
    # url(r'^debug/$', views.debug, name = 'debug')
)
