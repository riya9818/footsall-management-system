from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('book/', views.book_match, name='book_match'),
    path('manage/', views.manage_bookings, name='manage_bookings'),
    path('update/<int:booking_id>/<str:new_status>/', views.update_booking_status, name='update_booking_status'),
]
