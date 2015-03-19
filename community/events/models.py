from django.db import models
from organizations.models import Organization
from tags.models import Tag
from users.models import User

class Event(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    attendees = models.ManyToManyField(User)
    hosts = models.ManyToManyField(Organization)
    tags = models.ManyToManyField(Tag)
    datetime = models.DateTimeField()
    location = models.CharField(max_length=60)
