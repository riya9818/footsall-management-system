# bookings/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

def booking_list(request):
    bookings = Booking.objects.all().order_by('-date', '-time')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def book_match(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'bookings/book_match.html', {'form': form})

def manage_bookings(request):
    bookings = Booking.objects.all().order_by('-date')
    return render(request, 'bookings/manage_bookings.html', {'bookings': bookings})