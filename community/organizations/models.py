from django.db import models
from users.models import OurUser


class Organization(models.Model):

    name = models.CharField(max_length=100)
    admins = models.ManyToManyField(OurUser)
