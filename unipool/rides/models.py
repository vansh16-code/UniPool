from django.db import models
from django.contrib.auth.models import User
from datetime import time

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driven_rides")
    date = models.DateField()
    start_time = models.TimeField(default=time(9, 0))  
    end_time = models.TimeField(default=time(18, 0))
    available_seats = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_location = models.CharField(max_length=255, default="Not specified")
    passengers = models.ManyToManyField(User, related_name="booked_rides", blank=True)
    capacity = models.PositiveIntegerField(default=4)
    is_confirmed = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15,default="Not Provided") 

    def __str__(self):
        return f"{self.driver.username} - {self.date} ({self.start_time} to {self.end_time})"

class Booking(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name="bookings")
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    liability_accepted = models.BooleanField(default=False)
