__author__ = 'Alexis'
from django.forms import ModelForm
from models import Invitation

class InvitationForm(ModelForm):

    class Meta:
        model = Invitation
        exclude = ('sender',)