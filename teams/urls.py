from django.urls import path
from . import views

urlpatterns = [
    # Player URLs
    path('players/', views.player_list, name='player_list'),
    path('players/add/', views.add_player, name='add_player'),
    path('players/edit/<int:player_id>/', views.edit_player, name='edit_player'),
    path('players/delete/<int:player_id>/', views.delete_player, name='delete_player'),

    # Team URLs
    path('teams/', views.team_list, name='team_list'),
    path('teams/add/', views.add_team, name='add_team'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/edit/<int:team_id>/', views.edit_team, name='edit_team'),
    path('teams/delete/<int:team_id>/', views.delete_team, name='delete_team'),
    path('teams/<int:team_id>/add_player/', views.add_player_to_team, name='add_player_to_team'),
    path('teams/<int:team_id>/remove_player/<int:player_id>/', views.remove_player_from_team, name='remove_player_from_team'),
]
