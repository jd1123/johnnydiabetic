from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
#from django.core.paginator import Paginator
#from django.core.exceptions import ObjectDoesNotExist
from bloodsugar.forms import BloodSugarEntryForm
from bloodsugar.models import BloodSugarEntry
from django.core.urlresolvers import reverse
# Create your views here.


@login_required
def root(request):
    context = RequestContext(request)
    # POST Request
    if request.method == 'POST':
        form = BloodSugarEntryForm(request.POST)
        if form.is_valid():
            reading = int(form.cleaned_data['reading'])
            BloodSugarEntry.objects.create(reading = reading)
            return HttpResponseRedirect(reverse('bloodsugar.views.root'))
        else:
            return HttpResponse(form.errors)

    # GET request
    else:
        try:
            all_entries = BloodSugarEntry.objects.all().order_by('-entry_time')
            last_reading = all_entries[0].reading
            tm = all_entries[0].entry_time
            total_entries = len(all_entries)

            if total_entries < 14:
                avg_14 =sum([x.reading for x in all_entries])/total_entries
            else:
                avg_14 = sum([x.reading for x in all_entries[0:13]])/14

            if total_entries < 30:
                avg_30 = sum([x.reading for x in all_entries])/total_entries
            else:
                avg_30 = sum([x.reading for x in all_entries[0:29]])/30

        except:
            last_reading = 0
            avg_14 = 0
            avg_30 = 0

        x_axis = [x.entry_time for x in all_entries]
        y_axis = [x.reading for x in all_entries]

        context_dict = {'last_reading': last_reading, 'tm':tm, 'avg_14':avg_14, 'avg_30':avg_30}

        return render_to_response('bloodsugar/index.html', context_dict, context)

@login_required
def data(request):
    context = RequestContext(request)
    return HttpResponse("Not yet implemented")
