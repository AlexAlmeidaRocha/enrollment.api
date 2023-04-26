from enrollment.views import EnrollmentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',EnrollmentViewSet)
urlpatterns = router.urls