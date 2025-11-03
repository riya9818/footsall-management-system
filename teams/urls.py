from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams_home, name='teams_home'),
]
