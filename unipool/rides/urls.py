from django.urls import path
from . import views
from.views import delete_ride
from .views import confirm_ride


urlpatterns = [
    path('post/', views.post_ride, name='post_ride'),
    path('', views.ride_list, name='ride_list'),
    path('ride/delete/<int:ride_id>/', delete_ride, name='delete_ride'),
    path('ride/confirm/<int:ride_id>/', confirm_ride, name='confirm_ride'),
    path('rides/book/<int:ride_id>/', views.book_ride, name='book_ride'),
]

path('rides/book/<int:ride_id>/', views.book_ride, name='book_ride'),


