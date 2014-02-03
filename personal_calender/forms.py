__author__ = 'Alexis'
from django.forms import ModelForm
from personal_calender.models import Evenement, Evenement_Participant

class EventForm(ModelForm):
    class Meta:
        model = Evenement
        fields = ('nom', 'description', 'date', 'lieu')

class Evenement_ParticipantForm(ModelForm):
    class Meta:
        model = Evenement_Participant