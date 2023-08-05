from django.urls import path
from .views_front import (
    cookie_standsCreateView,
    cookie_standsDeleteView,
    cookie_standsDetailView,
    cookie_standsListView,
    cookie_standsUpdateView,
)

urlpatterns = [
    path("", cookie_standsListView.as_view(), name="cookie_stands_list"),
    path("<int:pk>/", cookie_standsDetailView.as_view(), name="cookie_stands_detail"),
    path("create/", cookie_standsCreateView.as_view(), name="cookie_stands_create"),
    path("<int:pk>/update/", cookie_standsUpdateView.as_view(), name="cookie_stands_update"),
    path("<int:pk>/delete/", cookie_standsDeleteView.as_view(), name="cookie_stands_delete"),
]
