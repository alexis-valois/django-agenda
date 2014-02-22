from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Circle(models.Model):
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(User)

    def contacts(self):
        return self.user_info.contact_set.all()

    def is_in_circle(self, user):
        if user in self.user_info.contact_set.all():
            return True
        return False

class UserInfo(models.Model):
    circle = models.ManyToManyField(Circle)
    notes = models.TextField()

class Contact(models.Model):
    owner = models.ForeignKey(User)
    user = models.ForeignKey(User, related_name="friend")
    invitation_send = models.BooleanField()
    invitation_accepted = models.BooleanField()
    optional_informations = models.OneToOneField(UserInfo, blank=True, null=True)

    def all_contacts(self, user):
        return Contact.objects.filter(owner=user)

    def all_circles(self, user):
        return Circle.objects.filter(owner=user)


class Invitation(models.Model):
    email = models.EmailField()
    sender = models.ForeignKey(User)

    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('invitation_liste')

    class Meta:
        unique_together=('email', 'sender')

