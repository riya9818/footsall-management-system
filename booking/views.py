from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.booked_by = request.user  # user must be logged in
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

def booking_list(request):
    bookings = Booking.objects.all().order_by('-date', 'start_time')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})
