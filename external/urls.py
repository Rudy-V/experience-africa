
from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home"),
    path("planned-safaris", views.PreplannedSafarisView.as_view(), name="planned-safaris"),
    path("lodges", views.LuxuryLodgesView.as_view(), name="lodges"),
    path("private-safaris", views.PrivateSafarisView.as_view(), name='private-safaris')
]
