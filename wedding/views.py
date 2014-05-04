from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Create your views here.

@login_required
def root(request):
    return HttpResponse('This is the wedding root')

@login_required
def gallery(request):
    context = RequestContext(request)
    return render_to_response('wedding/gallery.html', context)
    