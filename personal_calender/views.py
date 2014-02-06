from django.shortcuts import render, HttpResponseRedirect
from forms import EventForm, Evenement_ParticipantForm
from models import Evenement, Evenement_Participant
from django.contrib.auth.models import User
from django.forms import HiddenInput

def create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect('/agenda/%i/details/'%event.pk)
    else:
        form = EventForm()
    return render(request,'personal_calender/event/create.html', {'form':form})

def details(request, id):
    event = Evenement.objects.get(pk = id)
    if request.method == "POST":
        form = Evenement_ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/agenda/%s/details/' % id)
    else:
        form = Evenement_ParticipantForm(initial = {'evenement': event})
        participants = [user.pk for user in event.participants.all()]
        form.fields['participant'].queryset = User.objects.exclude(pk__in = participants)
        form.fields['evenement'].widget = HiddenInput()
    return render(request, 'personal_calender/event/details.html',
                  {'event':event,
                   'form': form})

def delete(request, id, participant):
    if request.method == "POST":
        evenement = Evenement.objects.get(pk = id)
        participant = User.objects.get(pk = participant)
        a_supprimer = Evenement_Participant.objects.get(
            evenement = evenement,
            participant = participant
        )
        a_supprimer.delete()
    return HttpResponseRedirect('/agenda/%s/details/' %id)

def liste(request):
    events = Evenement.objects.all()
    return render(request, 'personal_calender/event/liste.html', {'events': events})

def delete_eve(request, id):
    if request.method == "POST":
        evenement = Evenement.objects.get(pk = id)
        evenement.delete()
        return HttpResponseRedirect('/agenda/liste/')

def update_eve(request, id):
    event = Evenement.objects.get(pk = id)
    if request.method == "POST":
        print request.POST
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            a = form.save()
            return HttpResponseRedirect('/agenda/%i/details/' % a.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'personal_calender/event/create.html', {'form':form})