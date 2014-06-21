from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from forum.models import Forum, Thread, Post
from forum.forms import PostForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

#def debug_hosts(request):
#    g = request.get_host()
#    return HttpResponse(g)

@login_required
def forumlist(request):
    context = RequestContext(request)
    forums = Forum.objects.all()
    context_dict = {'forums': forums }
    return render_to_response('forum/forumlist.html', context_dict, context)

@login_required
def threadlist(request, pk):
    context = RequestContext(request)
    context_dict = {}
    try:
        forum = Forum.objects.get(pk=pk)
        title = forum.title
        threads = Thread.objects.filter(forum=pk)
        context_dict['threads'] =  threads
        context_dict['pk'] = pk
        context_dict['forum_title'] = title
    except:
        return HttpResponse('ERROR: There are no threads in this forum')

    return render_to_response('forum/threadlist.html', context_dict, context)

@login_required
def postlist(request, pk):
    context = RequestContext(request)
    context_dict = {}
    try:
        posts = Post.objects.filter(thread=pk).order_by('created')
        thread = Thread.objects.get(pk=pk)
        forum = thread.forum
        context_dict['forum_pk'] = forum.pk
        context_dict['thread_title'] = thread.title
        context_dict['forum_title'] = thread.forum.title
        context_dict['posts'] = posts
        context_dict['pk'] = pk
    except:
        return HttpResponse('ERROR: There are no posts in this thread')

    return render_to_response('forum/postlist.html', context_dict, context)

@login_required
def new_post(request, pk):
    context = RequestContext(request)
    context_dict = {'pk':pk}
    context_dict['action'] = 'new_thread'
    forum = Forum.objects.get(pk=pk)
    context_dict['forum_title'] = forum.title

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            thread = Thread.objects.create(forum=forum, title=subject, creator=request.user)
            Post.objects.create(thread=thread, subject=subject, body=body, creator=request.user)

            #return HttpResponse('Your Thread has been created')
            return HttpResponseRedirect(reverse("forum.views.threadlist", args=[pk]))
        else:
            print form.errors

    else:
        return render_to_response('forum/newpost.html', context_dict, context)

@login_required
def reply(request, pk):
    context = RequestContext(request)
    context_dict = {'pk': pk}

    if request.method=="POST":
        form = PostForm(request.POST)

        if form.is_valid():

            thread = Thread.objects.get(pk=pk)
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            Post.objects.create(thread=thread, subject=subject, body = body, creator=request.user)

            return HttpResponseRedirect(reverse("forum.views.postlist", args=[pk]))
        else:
            print form.errors
    else:
        return render_to_response('forum/reply.html', context_dict, context)
