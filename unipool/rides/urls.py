from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_ride, name='post_ride'),
    path('', views.landing_page, name='landing_page'),  # Make landing page as home page
    path('ride/list/', views.ride_list, name='ride_list'),
    path('ride/delete/<int:ride_id>/', views.delete_ride, name='delete_ride'),
    path('ride/confirm/<int:ride_id>/', views.confirm_ride, name='confirm_ride'),
    path('rides/book/<int:ride_id>/', views.book_ride, name='book_ride'),
]
