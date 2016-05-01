from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from rooms.models import DAYS, MONDAY
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Date(models.Model):
    """
    Date for the patients of MedicalBox
    Note: this model don't need calendar because is diferent
    to the Members's Calendar
    """
    # calendar = models.ForeignKey(Calendar)
    patient = models.ForeignKey(User)
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

