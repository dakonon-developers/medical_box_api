# -*- coding: UTF-8 -*-
"""!
Serializers that builds the data structure of the models to display

@author Ing. Leonel P. Hernandez M. (leonelphm at gmail.com)
@copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
@date 29-03-2017
@version 1.0.0
"""

from rest_framework import serializers

from .models import *


class AppointmentSerializer(serializers.ModelSerializer):
    """
        Class that allows you to serialize the model data Appointment
    """

    class Meta:
        model = Appointment
