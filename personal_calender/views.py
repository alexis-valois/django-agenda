from django.shortcuts import render, HttpResponseRedirect, render_to_response
from forms import EventForm, Evenement_ParticipantForm
from models import Evenement, Evenement_Participant
from django.contrib.auth.models import User
from django.forms import HiddenInput
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import ListView
import json, datetime
from django.utils.timezone import utc

class Evenement_Liste(ListView):
    def get_queryset(self):
        events = Evenement.objects.filter(participants = self.request.user, date__gte = datetime.datetime.utcnow().replace(tzinfo=utc))
        if "champs" in self.kwargs:
            events = events.filter((self.kwargs['champs'], self.kwargs['terme']))
        return events

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
            if request.is_ajax():
                delete_form = render_to_string('blocks/delete_form.html',
                                               {'delete_url': form.instance.delete_url(),},
                                               RequestContext(request)
                )
                data = {'participant' : form.instance.participant.username,
                        'get_status_display': form.instance.get_status_display(),
                        'delete_form' : delete_form
                }
                return HttpResponse(
                    json.dumps(data),
                    mimetype="application/json"
                )
            return HttpResponseRedirect('/agenda/%s/details/' % id)
    else:
        form = Evenement_ParticipantForm(initial = {'evenement': event})
        participants = [user.pk for user in event.participants.all()]
        form.fields['participant'].queryset = User.objects.exclude(pk__in = participants)
        form.fields['evenement'].widget = HiddenInput()
    if request.is_ajax():
        return render_to_response(
            'blocks/participant_form.html',
            {'event' : event,
             'form': form}
        )

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

    if request.is_ajax():
        return HttpResponse("OK")

    return HttpResponseRedirect('/agenda/%s/details/' %id)

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