from django.contrib import admin
from django.urls import path

from booking import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apartments/<int:apartment_id>', views.apartment_page,  name='apartment_page')
]


