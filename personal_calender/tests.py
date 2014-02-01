#-*-coding:utf-8 -*-
from django.test import TestCase
from personal_calender.models import Evenement_Participant, Evenement
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils.timezone import utc

class TestEvenement_Participant(TestCase):

    def generate_participant(self):
        participant1 = User(first_name="Alexis", last_name="Valois")
        participant1.save()

    def test_create_user(self):
        self.generate_participant()
        participant = User.objects.get(first_name = "Alexis")
        self.assertEquals(participant.last_name, "Valois")


    def generate_evenement(self):
        evenement = Evenement(nom="Un nouvel événement", description="Blablablablabla",
                              date=datetime.utcnow().replace(tzinfo=utc), lieu="Quelque part")
        evenement.save()

    def test_create_event(self):
        self.generate_evenement()
        evenement = Evenement.objects.get(nom = "Un nouvel événement")
        self.assertEquals(evenement.lieu, u"Quelque part")

    def test_create_event_participant(self):
        self.generate_participant()
        self.generate_evenement()
        participant = User.objects.get(first_name="Alexis")
        evenement = Evenement.objects.get(nom="Un nouvel événement")
        evnt_part = Evenement_Participant(evenement = evenement, participant = participant, status = 1)
        evnt_part.save()
        evnt = Evenement_Participant.objects.get(evenement = evenement, participant = participant)
        self.assertEquals(evnt.status, 1)

