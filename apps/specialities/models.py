from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Speciality(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return '{0}'.format(self.id)
