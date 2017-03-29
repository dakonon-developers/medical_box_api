# -*- coding: UTF-8 -*-
"""!
Views that control the processes of the appointments

@author Ing. Leonel P. Hernandez M. (leonelphm at gmail.com)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 29-03-2017
@version 1.0.0
"""

from dry_rest_permissions.generics import DRYPermissions
from rest_framework import (
    viewsets, filters, serializers
)

from .models import *
from .serializers import *


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet to list or create appointments.
    > Parameters:

        * Create: POST api/appointments/ (login required as a Doctor or Patient) => **date, patient, consult, paid, (Optionals => note, recipe)**.
        * Consult All: GET api/appointments/  => (Optionals: **date, patient, consult, paid, note, recipe**).
        * Consult One: GET api/appointments/ID.
        * Update: PATCH or PUT api/appointments/ ID (login required as a Doctor or Patient) => **{(Optionals)-> {"date", "patient", "consult", "paid", "note", "recipe"}**
        * To Authenticate api/appointments/  parameters => **{"username", "password"}**
    """
    model = Appointment
    serializer_class = AppointmentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    permission_classes = (DRYPermissions,)

    def get_queryset(self):
        return self.model.objects.all()
