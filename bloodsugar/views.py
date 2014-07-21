from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from bloodsugar.forms import BloodSugarEntryForm
from bloodsugar.models import BloodSugarEntry
from django.core.urlresolvers import reverse
from pylab import *
from johnnydiabetic.settings import STATIC_PATH
import os
from numpy import std
# Create your views here.


def root(request):
    context = RequestContext(request)
    # POST Request
    if request.method == 'POST':
        # you cannot post unless you are authenticated
        # right now, any user can post, this is bad
        if request.user.is_authenticated():
            form = BloodSugarEntryForm(request.POST)
            if form.is_valid():
                reading = int(form.cleaned_data['reading'])
                BloodSugarEntry.objects.create(reading=reading)
                return HttpResponseRedirect(reverse('bloodsugar.views.root'))
            else:
                return HttpResponse(form.errors)
        # tell em...
        else:
            return HttpResponse("ERROR: You cannot POST")

    # GET request
    else:
        try:
            all_entries = BloodSugarEntry.objects.all().order_by('-entry_time')
            last_reading = all_entries[0].reading
            tm = all_entries[0].entry_time
            total_entries = len(all_entries)
            if total_entries < 14:
                rd = [x.reading for x in all_entries]
                avg_14 = sum(rd)/total_entries
                stdev_14 = int(std(rd))
            else:
                rd = [x.reading for x in all_entries[0:13]]
                avg_14 = sum(rd)/14
                stdev_14 = int(std(rd))

            if total_entries < 30:
                rd = [x.reading for x in all_entries]
                avg_30 = sum(rd)/total_entries
                stdev_30 = int(std(rd))
            else:
                rd = [x.reading for x in all_entries[0:29]]
                avg_30 = sum()/30
                stdev_30 = int(std(rd))

            x_axis = [x.entry_time for x in all_entries]
            y_axis = [x.reading for x in all_entries]
            high = max(y_axis)
            low = min(y_axis)
            N = total_entries


        except ObjectDoesNotExist:
            all_entries = []
            last_reading = 0
            avg_14 = 0
            avg_30 = 0
            x_axis = []
            y_axis = []
            high = 0
            low = 0
            N = 0

        # Create chart
        sugar_chart(x_axis, y_axis)
        context_dict = {'last_reading': last_reading,
                        'tm': tm, 'avg_14': avg_14, 'stdev_14': stdev_14,
                        'avg_30': avg_30, 'stdev_30': stdev_30,
                        'high':high, 'low':low, 'N':N}

        return render_to_response('bloodsugar/index.html', context_dict, context)

# Send all sugars in csv text format
@login_required
def data(request):
    context = RequestContext(request)
    try:
        entries = BloodSugarEntry.objects.all()
    except ObjectDoesNotExist:
        entries = []

    output = []
    output.append("entry_time, reading, \n")
    for v in entries:
        output.append(str(v.entry_time) + ","+ str(v.reading) + ",\n")
    resp = ''.join(output)

    return HttpResponse(resp, content_type="text/csv")

def sugar_chart(x_axis, y_axis):
    plot_date(x_axis,y_axis, linestyle='--')

    xlabel('entry time')
    ylabel('blood sugar')
    title('All My Blood Sugars')
    grid(True)
    savefig(os.path.join(STATIC_PATH, "bschart.png"))
