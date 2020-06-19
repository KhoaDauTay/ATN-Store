from django.urls import path
from .views import (
    Home,
    Appointment,
    Booking,
    SearchResultsView,
    View,
)
app_name = 'store'


urlpatterns = [
    path('', Home, name='home'),
    path('view', View, name='view'),
    path('booking/', Booking, name="booking"),
    path('appointment', Appointment, name="appointment"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
