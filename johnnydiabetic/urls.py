from django.conf.urls import patterns, include, url
import forum
from basefunctions import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myforum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/',include('forum.urls')),
    #url(r'^wedding/',include('weddingpics.urls')),
    url(r'^about/$', views.about, name="about"),
    url(r"^$", views.root, name = "root"),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
)
