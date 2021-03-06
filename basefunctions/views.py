from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from basefunctions.forms import UserForm, UserProfileForm
from blog.models import BlogPost
import os
from johnnydiabetic.settings import STATIC_PATH

SECURE_ROOT = '/protected/'


# Create your views here.
def root(request):
    context = RequestContext(request)
    try:
        latest = BlogPost.objects.all().order_by('-id')[0]
        context_dict = {'latest' : True,
                        'title' : latest.title,
                        'pk' : latest.pk}
    except IndexError:
        context_dict = {}

    return render_to_response('index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    return render_to_response('about.html', context)

def robots(request):
    context=RequestContext(request)
    with open(os.path.join(STATIC_PATH, 'robots.txt')) as f:
        s = f.read()
    return HttpResponse(s, content_type='text/plain')


# Login View
# this definitely is insecure
# finally got the next thing working
# but the user can enter anything, probably malicious code
# so i need to clean the ?next= url when getting user data
def user_login(request):
    context = RequestContext(request)
    refer = request.META.get('HTTP_REFERER')
    refer = '/'+'/'.join(str(refer).split('/')[3:])

    if request.GET:
        nxt = request.GET['next']
    else:
        nxt=refer

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if request.POST['next']:
            nxt = request.POST['next']
            print "assigned " + str(nxt)
        else:
            nxt = refer
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print "NEXT:",
                print nxt
                if nxt == 'None':
                    return HttpResponseRedirect('/')
                else:
                    return HttpResponseRedirect(nxt)
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details.")
    else:
        return render_to_response('login.html', {'next': nxt}, context)


# Logout View
@login_required
def user_logout(request):
    refer = request.META.get('HTTP_REFERER')
    refer = '/'+'/'.join(str(refer).split('/')[3:])

    logout(request)
    return HttpResponseRedirect(refer)


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
    response = HttpResponse()  # 200 OK
    del response['content-type']  # We'll let the web server guess this.
    response['X-Accel-Redirect'] = abs_filename
    return response


def debug(request):
    context = RequestContext(request)
    return render_to_response('debug.html', context)


def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('register.html',
                              {'user_form': user_form,
                               'profile_form': profile_form,
                               'registered': registered},
                              context)
