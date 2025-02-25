from django.shortcuts import render, redirect, get_object_or_404
from .models import Ride, Booking
from .forms import RideForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def post_ride(request):
    if request.method == "POST":
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.driver = request.user
            ride.save()
            messages.success(request, "Ride posted successfully!")
            return redirect("ride_list")
        else:
            messages.error(request, "Error posting ride. Please check your inputs.")
    else:
        form = RideForm()

    return render(request, 'rides/post_ride.html', {'form': form})

def ride_list(request):
    rides = Ride.objects.all().order_by('-date')
    return render(request, 'rides/ride_list.html', {'rides': rides})

@login_required
def delete_ride(request, ride_id):
    ride = Ride.objects.filter(id=ride_id).first()  
    
    if not ride:
        messages.error(request, "Ride does not exist!") 
        return redirect('ride_list')  

    if request.method == "POST":  
        ride.delete()
        messages.success(request, "Ride deleted successfully!")
        return redirect('ride_list') 

    return render(request, 'rides/confirm_delete.html', {'ride': ride}) 

@login_required(login_url='/users/login/')
def confirm_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)

    if request.user != ride.driver:
        return HttpResponseForbidden("You are not allowed to confirm this ride.")

    ride.confirmed = True
    ride.save()
    return redirect('ride_list')

@login_required
def book_ride(request, ride_id):
    ride = get_object_or_404(Ride, id=ride_id)
    
    if request.method == "POST":
        liability_accepted = request.POST.get("liability") == "accepted"
        
        if not liability_accepted:
            messages.error(request, "You must accept liability before booking.")
            return redirect("ride_list")
        
        if ride.passengers.count() < ride.available_seats:
            ride.passengers.add(request.user)
            Booking.objects.create(ride=ride, passenger=request.user, liability_accepted=liability_accepted)
            messages.success(request,  "Ride booked successfully!.")
        else:
            messages.error(request, "Ride is already full.")
    
    return redirect("ride_list")



