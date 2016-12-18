from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default="", null=True, blank=True)
    otp = models.IntegerField()