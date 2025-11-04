from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required

@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.booked_by = request.user

            # Check for slot conflict
            existing = Booking.objects.filter(
                date=booking.date,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time
            )
            if existing.exists():
                form.add_error(None, " This time slot is already booked!")
            else:
                booking.save()
                return redirect('booking_list')

    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.all().order_by('-date', 'start_time')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})
