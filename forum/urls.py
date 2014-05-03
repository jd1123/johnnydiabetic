from django.conf.urls import patterns, url
from forum import views
import basefunctions

urlpatterns = patterns('',
                       url(r"^$",views.forumlist, name = "forumlist"),
                       url(r"^forum/(\d+)/$", views.threadlist, name = "threadlist"),
                       url(r"^thread/(\d+)/$", views.postlist, name = "thread"),
                       url(r"^new_thread/(\d+)/$", views.new_post, name = "new_thread"),
                       url(r"^reply/(\d+)/$", views.reply, name = "reply"),
                       #url(r'^login/$', views.user_login, name='login'),
                       #url(r'^logout/$', views.user_logout, name='logout'),
                       #url(r'^debug/$', views.debug_hosts, name = 'debug'),
                       )
