from datetime import time

from django.http import JsonResponse
from django.shortcuts import render

from .forms import DayForm

daysOfWeek = dict(monday=dict(start=time(), end=time(), automatic=True),
                  tuesday=dict(start=time(), end=time(), automatic=True),
                  wednesday=dict(start=time(), end=time(), automatic=True),
                  thursday=dict(start=time(), end=time(), automatic=True),
                  friday=dict(start=time(), end=time(), automatic=True),
                  saturday=dict(start=time(), end=time(), automatic=True),
                  sunday=dict(start=time(), end=time(), automatic=True))


def index(request):
    return render(request, 'display.html', {'week': daysOfWeek})


def stateData(request):
    return JsonResponse(daysOfWeek)


def edit(request):
    monday = DayForm()
    tuesday = DayForm()
    wednesday = DayForm()
    thursday = DayForm()
    friday = DayForm()
    saturday = DayForm()
    sunday = DayForm()

    if request.method == 'POST':
        form = DayForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            daysOfWeek[request.POST['day']] = form.cleaned_data

    # if a GET (or any other method) we'll create a blank form
    else:
        monday = DayForm()
        tuesday = DayForm()
        wednesday = DayForm()
        thursday = DayForm()
        friday = DayForm()
        saturday = DayForm()
        sunday = DayForm()

    return render(request, 'name.html',
                  {'monday': monday,
                   'tuesday': tuesday,
                   'wednesday': wednesday,
                   'thursday': thursday,
                   'friday': friday,
                   'saturday': saturday,
                   'sunday': sunday
                   })
