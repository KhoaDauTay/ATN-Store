from django.urls import path
from .views import (
    Home,
    Appointment,
    Booking,
    SearchResultsView
)
app_name = 'store'


urlpatterns = [
    path('', Home, name='home'),
    path('booking/', Booking, name="booking"),
    path('appointment', Appointment, name="appointment"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
