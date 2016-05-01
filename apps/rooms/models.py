from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from members.models import Member

MONDAY='monday'
TUESDAY='tuesday'
WEDNESDAY='wednesday'
THURSDAY='thursday'
FRIDAYS='fridays'
SATURDAY='saturday'
SUNDAY='sunday'

DAYS = (
    (MONDAY, 'Monday'),
    (TUESDAY, 'Tuesday'),
    (WEDNESDAY, 'Wednesday'),
    (THURSDAY, 'Thursday'),
    (FRIDAYS, 'Fridays'),
    (SATURDAY, 'Saturday'),
    (SUNDAY, 'Sunday')
)

@python_2_unicode_compatible
class Room(models.Model):
    """
    Room where the member will stay to make the date
    with the patient
    """
    member = models.ForeignKey(Member)
    floor = models.PositiveIntegerField()
    description = models.CharField(max_length=128)
    
    def __str__(self):
        return '{0}'.format(self.id)


class Calendar(models.Model):
    """
    Calendar about the room's schedule
    """
    room = models.ForeignKey(Room)

    def __str__(self):
        return '{0}'.format(self.id)


class CalendarSchedule(models.Model):
    """
    Model for the schedule of the member in the rooms
    about hour and days
    """
    calendar = models.ForeignKey(Calendar)
    day = models.CharField(max_length=10,choices=DAYS, default=MONDAY)
    hour_from = models.DateField()
    hour_to = models.DateField()

    def __init__(self, arg):
        super(CalendarSchedule, self).__init__()
        self.arg = arg

    def __str__(self):
        return '{0}'.format(self.id)


class SpecialsSchedule(models.Model):
    """
    This model is for take note about the specials days
    with the hours, this model will to replace the
    model 'CalendarSchedule' because these days are specials
    """
    calendar = models.ForeignKey(Calendar)
    day = models.CharField(max_length=10,choices=DAYS, default=MONDAY)
    month = models.PositiveIntegerField(max_length=2)
    year = models.PositiveIntegerField(max_length=4)
    hour_from = models.DateField()
    hour_to = models.DateField()

    def __init__(self, arg):
        super(SpecialsSchedule, self).__init__()
        self.arg = arg

    def __str__(self):
        return '{0}'.format(self.id)

