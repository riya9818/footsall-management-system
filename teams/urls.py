from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('add/', views.team_create, name='team_create'),
    path('edit/<int:pk>/', views.team_edit, name='team_edit'),
    path('delete/<int:pk>/', views.team_delete, name='team_delete'),
     path('<int:team_id>/', views.team_detail, name='team_detail'),
    path('<int:team_id>/add_player/', views.add_player, name='add_player'),
]
