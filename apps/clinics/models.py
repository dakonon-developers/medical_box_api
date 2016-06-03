from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cities_customized.models import Country, Region, City
from doctors.models import Doctor
from patients.models import Patient

@python_2_unicode_compatible
class Clinic(models.Model):
    # owner = models.ForeignKey(Member) ########
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country)
    # region = models.ForeignKey(Region) ######
    city = models.ForeignKey(City)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    latitude = models.CharField(max_length=128, blank=True, null=True)
    longitude = models.CharField(max_length=128, blank=True, null=True)
    phone_one = models.CharField(max_length=50, blank=True, null=True)
    phone_two = models.CharField(max_length=50, blank=True, null=True)
    doctors = models.ManyToManyField(Doctor)
    # doctors = models.ManyToManyField(Patient)
    

    def __str__(self):
        return '{0}'.format(self.id)
