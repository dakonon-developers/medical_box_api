"""
    Created by: pdonaire1
    Ing. Pablo Alejandro Gonzalez Donaire
"""
from django.contrib.auth.models import User
from rooms.serializers import RoomSerializer
from django.http import JsonResponse
from rest_framework import (
	status, viewsets, filters, serializers)
from rest_framework.response import Response
from dry_rest_permissions.generics import DRYPermissions
from utils.functions import build_json_object
from clinics.models import Clinic
from rooms.models import Room
from rest_framework.decorators import detail_route

class RoomViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Patients.
    > Parameters:

      * Create: POST /api/rooms/ (login required as a Clinic in field created_by or in ClinicAdmin) => **clinic_id, room, (Optionals => floor)**.
      * Consult All: GET /api/clinics/ => (Optionals: **phone_number, address, is_active, user__first_name, user__last_name, user__email**).
      * Consult One: GET /api/clinics/ID.
      * Update: PATCH or PUT /api/clinics/ID (login required as a Doctor) => **{(Optionals)-> {"name", "zip_code", "address", "latitude", "longitude", "phone_one", "phone_two", "country_id", "city_id" }**
      * Update: PATCH or PUT /api/clinics/ID/update_doctors/ (login required as a Doctor who has created the clinic) => **{"doctors": [1,2,3]}  ->this will remove all the doctors registered and will to add the doctors from the list**
      * Delete: DELETE /api/clinics/ID.
      * To Authenticate /api/api-token-auth/ parameters => **{"username", "password"}**
    """
    model = Room
    serializer_class = RoomSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    permission_classes = (DRYPermissions,)

    def get_queryset(self):
        return Room.objects.all()

    def perform_create(self, serializer):
        if ( "clinic_id" in self.request.data and 
            "clinic_id" in self.request.data):
            serializer.save(clinic_id= self.request.data['clinic_id'])
        else:
            raise serializers.ValidationError(
                {"error":'Invalid fields', "status": 400})