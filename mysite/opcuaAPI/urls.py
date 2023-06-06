from django.urls import path
from . import views

app_name = 'opcuaAPI'

urlpatterns = [
    path('post', views.GetData.as_view(), name='get_from_device'),
    path('get_data_from_server', views.ShareData.as_view(), name='get_from_server'),
    path('get_desired', views.ShareDesired.as_view(), name='data_to_checkout'),
    path('clear_desired', views.ClearDesired.as_view(), name='clear_desired')
]
