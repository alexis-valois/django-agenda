from django.shortcuts import render, HttpResponseRedirect
from forms import Evenement_ParticipantForm
from models import Evenement, Evenement_Participant
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
import json, datetime
from django.utils.timezone import utc

class Evenement_Liste(ListView):
    def get_queryset(self):
        events = Evenement.objects.filter(participants = self.request.user, date__gte = datetime.datetime.utcnow().replace(tzinfo=utc))
        if "champs" in self.kwargs:
            events = events.filter((self.kwargs['champs'], self.kwargs['terme']))
        return events

class Evenement_Detail(DetailView):
    model = Evenement
    def get_context_data(self, **kwargs):
        context = super(Evenement_Detail, self).get_context_data(**kwargs)
        form = Evenement_ParticipantForm(initial= { 'evenement' : self.object})
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = Evenement_ParticipantForm(self.request.POST)
        if form.is_valid():
            form.save()
            if self.request.is_ajax():
                delete_from = render_to_string("blocks/delete_form.html", {'delete_url' : form.instance.delete_url(),}, RequestContext(request))
                data = {'participant': form.instance.participant.username, 'get_status_display': form.instance.get_status_display(), 'delete_form' : delete_from}
                return HttpResponse(json.dumps(data), mimetype='application/json')
            else:
                return HttpResponseRedirect('/agenda/%s/detail' % id)

        else:
            if request.is_ajax():
                return render(request, 'blocks/participant_form.html', {'event' : form.instance.evenement, 'form' : form})
            else:
                return render(request, 'personal_calender/event/details.html', {'event': form.instance.evenement, 'form' : form})

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
