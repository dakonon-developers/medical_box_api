from rest_framework.routers import DefaultRouter, SimpleRouter
from patients.views import PatientViewSet
from doctors.views import DoctorViewSet

# router = SimpleRouter()
router = DefaultRouter()
# ------------------------------------------
router.register(r'patients', PatientViewSet, 'patients')
router.register(r'doctors', DoctorViewSet, 'doctors')

# urlpatterns = router.urls