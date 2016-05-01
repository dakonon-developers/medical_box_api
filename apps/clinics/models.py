from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from cities_light.models import Country, Region, City
from members.models import Member

@python_2_unicode_compatible
class Clinic(models.Model):
    owner = models.ForeignKey(Member)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    region = models.ForeignKey(Region)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=30, blank=True, null=True)
    latitude = models.CharField(max_length=128, blank=True, null=True)
    longitude = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.id)


@python_2_unicode_compatible
class ClinicDoctor(models.Model):
    member = models.ForeignKey(Member)
    Clinic = models.ForeignKey(Clinic)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return '{0}'.format(self.id)

