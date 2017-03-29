from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from patients.models import Patient
from doctors.models import DoctorSpeciality

@python_2_unicode_compatible
class Appointment(models.Model):
    date = models.DateTimeField()
    patient = models.ForeignKey(Patient)
    consult = models.ForeignKey(DoctorSpeciality)
    paid = models.BooleanField()
    note = models.TextField(blank=True, null=True)
    recipe = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{0}'.format(self.id)

    ######################
    # Global Permissions #
    ######################

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    def has_create_permission(request):
        return True

    @staticmethod
    def has_write_permission(request):
        return True

    ######################
    # Object Permissions #
    ######################

    def has_object_write_permission(self, request):
        return True

    def has_object_read_permission(self, request):
        return True

    def has_object_update_permission(self, request):
        return True

    def has_object_destroy_permission(self, request):
        return False