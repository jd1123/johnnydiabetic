from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import BlogPost
from blog.forms import BlogPostForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import re
# Create your views here.


def index(request, pg=1):
    context = RequestContext(request)
    context_dict = {}

    allposts = BlogPost.objects.all().order_by("-created")
    p = Paginator(allposts, 5)
    try:
        recent_posts = p.page(pg).object_list
    except:  # no page exception - dont know what it is
        recent_posts = p.page(1).object_list
    posts = []

    for i in recent_posts:
        words = i.body.split(' ')
        if len(words) < 30:
            l = len(words)
        else:
            l = 30

        slug = ' '.join([x for x in words[0:l]]) + "..."
        posts.append({'title': i.title,
                    'slug': slug,
                    'pk': i.pk,
                    'object':i})

    context_dict['posts'] = posts
    context_dict['curr_page'] = int(pg)
    return render_to_response('blog/index.html', context_dict, context)


@login_required
def blogpost(request, pk=None):
    context = RequestContext(request)
    context_dict = {}

    if request.method == "POST":
        form = BlogPostForm(request.POST)

        if form.is_valid():

            if pk is not None:
                p = BlogPost.objects.get(pk=pk)
                p.title = form.cleaned_data['title']
                p.body = form.cleaned_data['body']
                p.save()

            else:
                title = form.cleaned_data['title']
                body = form.cleaned_data['body']
                BlogPost.objects.create(title=title, body=body, creator=request.user)

            return HttpResponseRedirect(reverse('blog.views.index'))
        else:
            return HttpResponse(form.errors)
    else:
        if pk is not None:
            p = BlogPost.objects.get(pk=pk)
            context_dict['edit'] = True
            context_dict['pk'] = pk
            context_dict['title'] = p.title
            context_dict['body'] = strip_paragraph_elements(p.body)
            print context

        return render_to_response('blog/newblogpost.html', context_dict, context)


def viewblogpost(request, pk):
    context = RequestContext(request)
    context_dict = {}
    post = BlogPost.objects.get(pk=pk)
    context_dict['post'] = post
    context_dict['body'] = add_elements(post.body)
    context_dict['pk'] = pk
    return render_to_response('blog/viewblogpost.html', context_dict, context)


def add_elements(post_string):
    paragraph_list = post_string.split("\r\n\r\n")

    rmelements = []
    for i in range(len(paragraph_list)):
        if paragraph_list[i] != "":
            paragraph_list[i] = "<p>"+paragraph_list[i]+"</p>"
        else:
            rmelements.append(i)
    for index in rmelements:
        del paragraph_list[index]

    return "".join(paragraph_list)


def strip_paragraph_elements(post_string):
    return re.sub(r"<.?p[^>]*>", "\r\n\r\n", post_string)
