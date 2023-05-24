from django.urls import path
from . import views

app_name = "control"

urlpatterns = [
    path("", views.SupervisoryControl.as_view(), name="main")
]