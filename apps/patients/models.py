from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Patient(models.Model):
    user = models.ForeignKey(User)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    is_active = models.BooleanField()


    def __str__(self):
        return '{0}'.format(self.id)