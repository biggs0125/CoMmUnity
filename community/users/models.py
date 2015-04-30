from django.db import models
from tags.models import Tag
from django.contrib.auth.models import User

class OurUser(User):

    subscriptions = models.ManyToManyField(Tag)
