from urllib import request
from django.contrib import messages
from django.shortcuts import render
from .models import Apartment, Booking

from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    apartments = Apartment.objects.all()
    return render(request, 'home.html', {'apartments': apartments})

def apartment_page(request, apartment_id):
    apartment = Apartment.objects.get(id = apartment_id)
    return render(request,'apartment_page.html', {'apartment': apartment})


def booking_page(request, apartment_id):
    apartment = Apartment.objects.get(id = apartment_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        # тут має бути валідація даних 
        existing_booking = Booking.objects.filter(
            apartment=apartment,
            check_in__lt=check_out,
            check_out__gt=check_in
        )
        if existing_booking.exists():
            messages.error(request, 'Ці дати вже заброньовані. Будь ласка, оберіть інші дати.')
        else:
            booking = Booking.objects.create(
            apartment=apartment,
            name=name,
            email=email,
            phone=phone,
            check_in=check_in,
            check_out=check_out,
            total_price=apartment.price,
            user=request.user if request.user.is_authenticated else None
            )

        
            return render(request, 'booking.confirmed.html', {'apartment': apartment, 'booking': booking})
    
    return render(request,'booking.html', {'apartment': apartment})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'my_bookings.html', {'bookings': bookings})

