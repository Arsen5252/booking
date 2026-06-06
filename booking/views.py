from django.shortcuts import render
from .models import Apartment, Booking
# Create your views here.
def home(request):
    apartments = Apartment.objects.all()
    return render(request, 'home.html', {'apartments': apartments})

def apartment_page(request, apartment_id):
    apartment = Apartment.object.get(id = apartment_id)
    return render(request,'apartment_page.html', {'apartment': apartment})


def booking_page(request, apartment_id):
    apartment = Apartment.object.get(id = apartment_id)
    
    return render(request,'booking.html', {'apartment': apartment})