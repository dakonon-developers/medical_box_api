from rest_framework import serializers
from django.contrib.auth.models import User
# from validate_email import validate_email
from clinics.models import Clinic
from utils.serializers import UserSerializer

class ClinicSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        exclude = ('is_active', )
        depth = 1

    def get_created_by(self, clinic):
        if hasattr(clinic, 'created_by'):
            request = self.context['request']
            return UserSerializer(clinic.created_by, context={'request': request}).data
        else:
            return None