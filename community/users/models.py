from django.db import models
from tags.models import Tag

class User(models.Model):

    username = models.CharField(max_length=15)
    subscriptions = models.ManyToManyField(Tag)