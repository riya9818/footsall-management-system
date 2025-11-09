from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.player_list, name='player_list'),
    path('players/add/', views.add_player, name='add_player'),
    path('', views.team_list, name='team_list'),
    path('add/', views.add_team, name='add_team'),
]

