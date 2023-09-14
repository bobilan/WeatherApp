from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view),
    path('weather/', views.weather_view, name='weather_view'),
    path('second/', views.second_view, name='second_view'),
    path('login/', views.user_login_view, name='user_login_view'),
    path('user_profile/', views.user_profile, name='user_profile'),
]
