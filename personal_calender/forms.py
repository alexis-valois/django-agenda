__author__ = 'Alexis'
from django.forms import ModelForm
from personal_calender.models import Evenement, Evenement_Participant
from django.forms import HiddenInput
from django.contrib.auth.models import User

class EventForm(ModelForm):
    class Meta:
        model = Evenement
        fields = ('nom', 'description', 'date', 'lieu')

class Evenement_ParticipantForm(ModelForm):
    class Meta:
        model = Evenement_Participant

    def __init__(self, *args, **kwargs):
        super(Evenement_ParticipantForm, self).__init__(*args, **kwargs)
        self.fields['evenement'].widget = HiddenInput()
        if 'evenement' in self.initial:
            participants = [user.pk for user in self.initial['evenement'].participants.all()]
            self.fields['participant'].queryset=User.objects.exclude(pk__in = participants)