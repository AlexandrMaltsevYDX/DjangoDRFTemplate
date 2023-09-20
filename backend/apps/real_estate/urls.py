from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import RealestateViewSet


router = DefaultRouter()
router.register(r"objects", RealestateViewSet)

urlpatterns = [
    path("real_estate/", include(router.urls), name="objects"),
]
