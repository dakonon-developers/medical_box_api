from rest_framework.routers import DefaultRouter, SimpleRouter
from patients.views import PatientViewSet
from doctors.views import DoctorViewSet
from clinics.views import ClinicViewSet
from specialities.views import SpecialityViewSet

# router = SimpleRouter()
router = DefaultRouter()
# ------------------------------------------
router.register(r'patients', PatientViewSet, 'patients')
router.register(r'doctors', DoctorViewSet, 'doctors')
router.register(r'clinics', ClinicViewSet, 'clinics')
router.register(r'specialities', SpecialityViewSet, 'specialities')

# urlpatterns = router.urls