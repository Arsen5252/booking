from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Apartment(models.Model):
    TYPE_ROOM_CHOICES = [
        ('single', 'Одиночний номер'),
        ('double', 'Двомісний номер'),  
        ('suite', 'Люкс'),
        ('family', 'Сімейний номер'),
        ('studio', 'Студія'),
        ('penthouse', 'Пентхаус'),        
    ]

    title = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='apartment_images/', null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField(default=1)

    type_room = models.CharField(max_length=50, choices=TYPE_ROOM_CHOICES, null=True,blank=True) 

    def __Str__(self):
        return f"{self.title} - {self.location} - 💲{self.price} грн"
    

class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

