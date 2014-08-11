from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.paginator import Paginator
from wedding.models import WeddingPic
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


@login_required
def root(request):
    return HttpResponse('This is the wedding root')


@login_required
def gallery_pic(request, gallery_name, pic_name):
    context = RequestContext(request)
    context_dict = {}
    try:
        pic = PictureEntry.objects.get(pic_name=pic_name)
        context_dict['pic_name'] = pic.pic_name
        context_dict['caption'] = pic.caption
    except ObjectDoesNotExist:
        return render_to_response('404.html', context_dict, context)

    return render_to_response('wedding/pictemplate.html', context_dict, context)


@login_required
def gallery(request, page_num=1):
    context = RequestContext(request)
    context_dict = {}
    wedding_pictures = WeddingPic.objects.all()
    p = Paginator(wedding_pictures, 16)
    context_dict['pics'] = p.page(page_num).object_list
    page_list = []
    for i in range(p.num_pages):
        page_list.append(i+1)
    context_dict['page_list'] = page_list
    context_dict['curr_page'] = int(page_num)

    return render_to_response('wedding/gallery.html', context_dict, context)


@login_required
def pic(request, pic_name):
    context = RequestContext(request)
    context_dict = {}
    try:
        pic = WeddingPic.objects.get(pic_name=pic_name)
        context_dict['pic_name'] = pic.pic_name
        context_dict['caption'] = pic.caption
    except ObjectDoesNotExist:
        return render_to_response('404.html', context_dict, context)

    return render_to_response('wedding/pictemplate.html', context_dict, context)
