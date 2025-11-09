# teams/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('add/', views.add_team, name='add_team'),
    path('<int:team_id>/', views.team_detail, name='team_detail'),
    path('<int:team_id>/add_player/', views.add_player_to_team, name='add_player_to_team'),
    path('<int:team_id>/remove_player/<int:player_id>/', views.remove_player_from_team, name='remove_player_from_team'),

    path('players/', views.player_list, name='player_list'),
    path('players/add/', views.add_player, name='add_player'),
]
