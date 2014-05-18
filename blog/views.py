from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.models import BlogPost
from blog.forms import BlogPostForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = RequestContext(request)
    context_dict = {}
    
    allposts = BlogPost.objects.all().order_by("-created")
    context_dict['posts'] = allposts
    
    return render_to_response('blog/index.html', context_dict, context)

@login_required
def blogpost(request):
    context = RequestContext(request)
    context_dict = {}
    
    if request.method=="POST":
        form = BlogPostForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data['title']
            body = add_elements(form.cleaned_data['body'])
            BlogPost.objects.create(title=title, body=body)
            
            return HttpResponseRedirect(reverse('blog.views.index'))
        else:
            print form.errors
    else:
        return render_to_response('blog/newblogpost.html', context_dict, context)

def viewblogpost(request,pk):
    context = RequestContext(request)
    context_dict = {}
    post = BlogPost.objects.get(pk=pk)
    context_dict['post'] = post
    return render_to_response('blog/viewblogpost.html', context_dict, context)

def add_elements(post_string):
    paragraph_list = post_string.split("\r\n")
    
    rmelements = []
    for i in range(len(paragraph_list)):
        if paragraph_list[i]!="":
            paragraph_list[i] = "<p>"+paragraph_list[i]+"</p>"
        else:
            rmelements.append(i)
    for index in rmelements:
        del paragraph_list[index]
        
    return "".join(paragraph_list)