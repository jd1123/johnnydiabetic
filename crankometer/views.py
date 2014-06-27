from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from crankometer.models import Crankometer
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def index(request):
    context = RequestContext(request)
    return render_to_response('crankometer/index.html', context)


# I need to figure out how to add this permission to users
# that can vote in this poll
@permission_required('can_vote')
def vote(request):
    context=RequestContext(request)
    return render_to_response('crankometer/vote.html', context)
