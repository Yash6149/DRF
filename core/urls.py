from django.conf.urls import url
from rest_framework import routers
from core.views import StudentViewSet, UniversityViewSet
from django.conf.urls import include


router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]

