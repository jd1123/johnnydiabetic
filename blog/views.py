from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import BlogPost
from blog.forms import BlogPostForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
import re
# Create your views here.

def index(request):
    context = RequestContext(request)
    context_dict = {}
    
    allposts = BlogPost.objects.all().order_by("-created")
    context_dict['posts'] = allposts
    
    return render_to_response('blog/index.html', context_dict, context)

@login_required
def blogpost(request, pk=None):
    context = RequestContext(request)
    context_dict = {}
    
    if request.method=="POST":
        form = BlogPostForm(request.POST)
        
        if form.is_valid():
            
            if pk!=None:
                p = BlogPost.objects.get(pk=pk)
                p.title = form.cleaned_data['title']
                p.body = add_elements(form.cleaned_data['body'])
                p.save()
                
            else:
                title = form.cleaned_data['title']
                body = add_elements(form.cleaned_data['body'])
                BlogPost.objects.create(title=title, body=body)
            
            return HttpResponseRedirect(reverse('blog.views.index'))
        else:
            return HttpResponse(form.errors)
    else:
        if pk!=None:
            p = BlogPost.objects.get(pk=pk)
            context_dict['edit'] = True
            context_dict['pk'] = pk
            context_dict['title'] = p.title
            context_dict['body'] = strip_paragraph_elements(p.body)
            print context
        
        return render_to_response('blog/newblogpost.html', context_dict, context)

def viewblogpost(request,pk):
    context = RequestContext(request)
    context_dict = {}
    post = BlogPost.objects.get(pk=pk)
    context_dict['post'] = post
    return render_to_response('blog/viewblogpost.html', context_dict, context)

def add_elements(post_string):
    paragraph_list = post_string.split("\n")
    
    rmelements = []
    for i in range(len(paragraph_list)):
        if paragraph_list[i]!="":
            paragraph_list[i] = "<p>"+paragraph_list[i]+"</p>"
        else:
            rmelements.append(i)
    for index in rmelements:
        del paragraph_list[index]
        
    return "".join(paragraph_list)

def strip_paragraph_elements(post_string):
    return re.sub(r"<.?p[^>]*>", "",post_string)
    