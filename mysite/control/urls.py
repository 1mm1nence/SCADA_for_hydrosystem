from django.urls import path
from . import views
from opcuaAPI.views import stop_button

app_name = "control"

urlpatterns = [
    path("", views.SupervisoryControl.as_view(), name="main"),
    path("stop_button/", stop_button, name="stop")
]