#-*-coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Evenement(models.Model):
    nom = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    participants = models.ManyToManyField(
        User,
        through="Evenement_Participant",
    )
    date = models.DateTimeField()
    lieu = models.TextField()

    def get_absolute_url(self):
        return "/agenda/%s/details" % self.id

class Evenement_Participant(models.Model):
    class Meta:
        unique_together = ("evenement", "participant")

    evenement = models.ForeignKey(Evenement)
    participant = models.ForeignKey(User)
    status_choices = (
        (0, "hôte"),
        (1, "invité"),
        (2, "désisté")
    )
    status = models.IntegerField(choices = status_choices)
