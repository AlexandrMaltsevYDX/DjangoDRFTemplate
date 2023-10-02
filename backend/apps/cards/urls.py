from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import CardModelViewSet


router = DefaultRouter()
router.register(prefix=r"cards", viewset=CardModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
