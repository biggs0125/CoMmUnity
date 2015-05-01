from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=20)
    is_org_tag = models.BooleanField(default=False)
