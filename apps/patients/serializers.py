from rest_framework import serializers
from django.contrib.auth.models import User
# from validate_email import validate_email
from patients.models import Patient
from utils.serializers import UserSerializer

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ('id', 'phone_number', 'address', 'is_active',
            'user')
        depth = 1

    def get_user(self, patient):
        request = self.context['request']
        return UserSerializer(patient.user, context={'request': request}).data

    def get_is_active(self, patient):
        return patient.is_active
