# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('standings/', league_standings, name='standings'),
    path('match/<int:match_id>/stats/', add_player_stats, name='add_player_stats'),

]
