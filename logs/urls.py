from django.urls import path
from . import views

urlpatterns = [
    path("", views.logs_view, name="logs"),
    path("list/", views.logs_list, name="logs_list"),
]
