from django.urls import path
from . import views

app_name = 'opcuaAPI'

urlpatterns = [
    path('post', views.Data.as_view(), name='post'),
    path('', views.show_data, name='show'),
]
