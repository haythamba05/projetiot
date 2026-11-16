from django.urls import path
from .api import Dlist, Dhtviews
from . import views

urlpatterns = [
    path("list/", Dlist, name="dht-list"),
    path("post/", Dhtviews.as_view(), name="dht-create"),
    path("dashboard/", views.dashboard, name="dashboard"),
]