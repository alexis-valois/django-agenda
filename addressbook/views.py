# -*- coding: utf-8 -*-
from models import Invitation
from django.views.generic import ListView, CreateView
from forms import InvitationForm
from django.http import HttpResponseRedirect
from django.forms.util import ErrorList
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.mail import send_mail

class InvitationListView(ListView):
    def get_queryset(self):
        return Invitation.objects.filter(sender=self.request.user)

class InvitationView(CreateView):
    form_class = InvitationForm
    model = Invitation

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender = self.request.user
        try:
            Invitation.objects.get(email=obj.email, sender = obj.sender)
            form._errors["email"] = ErrorList(
                [u'Une invitation à déjà été envoyée à cette adresse.']
            )
            return super(InvitationView, self).form_valid(form)
        except Invitation.DoesNotExist:
            pass
        obj.save()
        send_invitation(obj)
        return HttpResponseRedirect(obj.get_absolute_url())

def send_invitation(invitation):
    try:
        User.objects.get(email=invitation.email)
        message = "{0} vous à ajouté à ses contacts".format(invitation.sender.username)
    except User.DoesNotExist:
        message = """
                {0} vous invite à rejoindre ses contacts.
                Inscrivez-vous sur http://{1}/user/create_account/ pour accepter son invitation""".format(invitation.sender.username, Site.objects.get_current().domain)
    send_mail('Une invitation vous à été envoyée',
        message,
        invitation.sender,
        [invitation.email],
        fail_silently=False
    )