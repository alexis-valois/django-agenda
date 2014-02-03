from django.shortcuts import render, HttpResponseRedirect
from forms import EventForm, Evenement_ParticipantForm
from models import Evenement

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect('/agenda/%i/details/'%event.pk)
    else:
        form = EventForm()
    return render(request,'event/create.html', {'form':form})

def details(request, id):
    event = Evenement.objects.get(pk = id)
    if request.method == "POST":
        form = Evenement_ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/%s/details/' % event)
    else:
        form = Evenement_ParticipantForm()
    return render(request, 'event/details.html',
                  {'event':event,
                   'form': form})