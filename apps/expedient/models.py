from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Expedient(models.Model):
    patient = models.ForeignKey(User)
    day = models.DateTimeField()
    symptom = models.CharField(max_length=550, blank=True, null=True)
    syndrome = models.CharField(max_length=550)
    recipe = models.TextField()


    def __str__(self):
        return '{0}'.format(self.id)

