__author__ = 'Alexis'
from django.forms import ModelForm
from personal_calender.models import Evenement

class EventForm(ModelForm):
    class Meta:
        model = Evenement
        fields = ('nom', 'description', 'date', 'lieu')