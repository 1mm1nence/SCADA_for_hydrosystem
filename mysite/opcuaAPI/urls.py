from django.urls import path
from . import views

app_name = 'opcuaAPI'

urlpatterns = [
    path('post', views.GetData.as_view(), name='get_from_device'),
    path('get_data_from_server', views.ShareData.as_view(), name='get_from_server')
]
