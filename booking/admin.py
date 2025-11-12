from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('team', 'opponent_team', 'ground', 'date', 'time', 'status')
    list_filter = ('status', 'ground', 'date')
    search_fields = ('team__name', 'opponent_team__name', 'ground__name')
