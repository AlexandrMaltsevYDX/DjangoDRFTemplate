from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# from apps.real_estate import urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.cards.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")
    ),
]
