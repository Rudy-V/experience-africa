
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("luxury", views.PreplannedSafarisView.as_view(), name="luxury"),
]
