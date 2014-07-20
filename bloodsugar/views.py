from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.paginator import Paginator
from wedding.models import WeddingPic
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@login_required
def root(request):
    context = RequestContext(request)
    return render_to_response('bloodsugar/index.html', context)

@login_required
def entry(request):
    context = RequestContext(request)
    return HttpResponse("Not yet implemented")
