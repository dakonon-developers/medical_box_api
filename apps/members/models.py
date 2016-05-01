from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Member(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return '{0}'.format(self.id)
