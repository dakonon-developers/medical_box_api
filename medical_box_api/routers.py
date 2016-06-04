from rest_framework.routers import DefaultRouter, SimpleRouter
from patients.views import PatientViewSet


# router = SimpleRouter()
router = DefaultRouter()
# ------------------------------------------
router.register(r'patients', PatientViewSet, 'patients')
# urlpatterns = router.urls