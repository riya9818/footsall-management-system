from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('team', 'date', 'start_time', 'end_time', 'booked_by', 'created_at')
    list_filter = ('date',)
