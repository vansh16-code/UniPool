from django.contrib import admin
from .models import Ride,Booking

admin.site.register(Ride)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("passenger", "ride", "liability_accepted")  
    list_filter = ("liability_accepted", "ride")  
    search_fields = ("passenger__username", "ride__start_location")  
# Register your models here.
