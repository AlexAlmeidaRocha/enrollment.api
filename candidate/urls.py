from candidate.views import CandidateViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',CandidateViewSet)
urlpatterns = router.urls