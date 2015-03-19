from django.db import models
from users.models import User


class Organization(models.Model):

    name = models.CharField(max_length=100)
    admins = models.ManyToManyField(User)
