# main/urls.py

from django.urls import path
from . import views

from .views import league_standings
from teams.views import mark_availability


urlpatterns = [
    path('', views.home, name='home'),
    path('standings/', views.league_standings, name='standings'),
    path('match/<int:match_id>/stats/', views.add_player_stats, name='add_player_stats'),
    path('match/<int:match_id>/availability/',mark_availability, name='mark_availability'),
    path('match/<int:match_id>/attendance/', take_attendance, name='take_attendance'),

]
