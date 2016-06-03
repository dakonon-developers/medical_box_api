from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from clinics.models import Clinic
from doctors.models import Doctor

@python_2_unicode_compatible
class Room(models.Model):
    floor = models.CharField(max_length=35, blank=True, null=True)
    room = models.CharField(max_length=35)
    clinic = models.ForeignKey(Clinic)

    def __str__(self):
        return '{0}'.format(self.id)


@python_2_unicode_compatible
class Schedule(models.Model):
    init = models.TimeField()
    end = models.TimeField()
    week_day = models.IntegerField()

    def __str__(self):
        return '{0}'.format(self.id)

@python_2_unicode_compatible
class RoomDoctor(models.Model):
    room = models.ForeignKey(Room)
    doctor = models.ForeignKey(Doctor)
    schedule = models.ForeignKey(Schedule)
    

    def __str__(self):
        return '{0}'.format(self.id)

