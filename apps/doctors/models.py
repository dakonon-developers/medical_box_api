from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from specialities.models import Speciality

@python_2_unicode_compatible
class Doctor(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128, blank=True, null=True) # like a leyend
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return '{0}'.format(self.id)


class DoctorSpeciality(models.Model):
    speciality = models.ForeignKey(Speciality)
    doctor = models.ForeignKey(Doctor)
    consult_price = models.FloatField()
