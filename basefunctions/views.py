from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import os

SECURE_ROOT = '/protected/'

# Create your views here.

def root(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def about(request):
    context = RequestContext(request)
    return render_to_response('about.html', context)

# Login View
def user_login(request):
    context = RequestContext(request)
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details.")
    else:
        return render_to_response('login.html', {}, context)

# Logout View    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# this is to serve secure content
# I admit, it was copied
def get_absolute_filename(filename='', safe=True):
    if not filename:
        return os.path.join(SECURE_ROOT, 'index')
    if safe and '..' in filename.split(os.path.sep):
        return get_absolute_filename(filename='')
    return os.path.join(SECURE_ROOT, filename)

@login_required
def retrieve_file(request, filename=''):
    abs_filename = get_absolute_filename(filename)
    response = HttpResponse() # 200 OK
    del response['content-type'] # We'll let the web server guess this.
    response['X-Accel-Redirect'] = abs_filename
    return response

def debug(request):
    context = RequestContext(request)
    return render_to_response('debug.html', context)