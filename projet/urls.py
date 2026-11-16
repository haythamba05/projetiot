from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    # l'adresse racine (http://IP:8000/) ouvre directement le dashboard
    path("", RedirectView.as_view(pattern_name="dashboard", permanent=False)),
    path("", include("DHT.urls")),
]