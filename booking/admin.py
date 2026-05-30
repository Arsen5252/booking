from django.contrib import admin

# Register your models here.
from .models import Apartment,Booking
admin.site.register(Apartment)
admin.site.register(Booking)