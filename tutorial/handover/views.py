from django.shortcuts import render
from .forms import CurrentHOForm
from .models import CurrentHO
import datetime


def new_event(request):
    currenthoform = CurrentHOForm
    if request.method == 'POST':
        new_event_form = currenthoform(request.POST)
        if new_event_form.is_valid():
            new_event_form.full_clean()
            new_event_form.save()
            today = datetime.date.today()
            last_monday = today - datetime.timedelta(days=today.weekday())
            current_ho_data = CurrentHO.objects.filter(start_date__gte=last_monday)
            return render(request, 'handover/CurrentHO.html', {'form': current_ho_data})
    else:
        return render(request, 'handover/newevent.html', {'form': currenthoform})


def current_handover(request):
    today = datetime.date.today()
    last_monday = today - datetime.timedelta(days=today.weekday())
    current_ho_data = CurrentHO.objects.filter(start_date__gte=last_monday)
    return render(request, 'handover/CurrentHO.html',{'form': current_ho_data})