

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from django.core import serializers

def clean_serlialized_object(doctors, length, i=0):
    doctors[i]['fields']['id'] = doctors[i]['pk']
    del doctors[i]['pk']
    del doctors[i]['model']
    doctors[i] = doctors[i]['fields']
    if i < length-1:
        clean_serlialized_object(doctors, length, i+1)
    return doctors

def build_json_object(doctors):
    doctors = serializers.serialize("json", doctors)
    doctors = JSONParser().parse(BytesIO(doctors))
    if len(doctors) > 0:
        return clean_serlialized_object(doctors, len(doctors))
    return [{}]
