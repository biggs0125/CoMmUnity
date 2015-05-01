from django.db import models
from users.models import OurUser
from slugify import slugify
from tags.models import Tag

class Organization(models.Model):

    name = models.CharField(max_length=100)
    admins = models.ManyToManyField(OurUser)
    org_tag = models.ForeignKey(Tag)
