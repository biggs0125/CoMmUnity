from django.db import models
from organizations.models import Organization
from tags.models import Tag
from users.models import OurUser

class Event(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    attendees = models.ManyToManyField(OurUser)
    hosts = models.ManyToManyField(Organization)
    tags = models.ManyToManyField(Tag)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    location = models.CharField(max_length=60)
