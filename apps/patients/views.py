from django.contrib.auth.models import User
from patients.serializers import PatientSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from patients.models import Patient
from rest_framework import filters

class PatientViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Patients.
    > Parameters:

      * Create: POST /api/patients/ => **phone_number, address, first_name, last_name, email, password**.
      * Consult All: GET /api/patients/ => (Optionals: **phone_number, address, is_active, user__first_name, user__last_name, user__email**).
      * Consult One: GET /api/patients/ID.
      * Update: PATCH or PUT => **{"id", (Optionals)-> {"phone_number", "address", "user": {"first_name", "last_name", "id"}}**
      * Delete: DELETE /api/patients/ID.
    """
    model = Patient
    serializer_class = PatientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('phone_number', 'address', 'is_active', 'user__first_name', 'user__last_name', 'user__email')
    # Another option to filter: 
    # https://github.com/philipn/django-rest-framework-filters

    def get_queryset(self):
        return Patient.objects.all()

    def perform_create(self, serializer):
        first_name = self.request.data["first_name"]
        last_name = self.request.data["last_name"]
        email = self.request.data["email"]
        password = self.request.data["password"]
        if email:
            if User.objects.filter(email=email).exists():
                # user = User.objects.get(email=email)
                return Response({"result": False, "notice": "Email is already registred"})
            else:
                user = User.objects.create_user(
                    username=email,
                    first_name=first_name,
                    last_name=last_name,
                    email=email)
                user.set_password(password)

            serializer.save(user=user, is_active=True)
        else:
            return Response({"result": False, "notice": "fields invalids"})

    def perform_update(self, serializer):
        id = self.request.data["user"]["id"]
        user = User.objects.get(id=id)
        user.first_name = self.request.data["user"]["first_name"]
        user.last_name = self.request.data["user"]["last_name"]
        user.save()
        serializer.save()
