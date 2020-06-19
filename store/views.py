from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, View
from django.db.models import Q
# Create your views here.

def Home(request):
    return render(request, "home.html")
    
def Booking(request):
    return render(request, 'FormBooking.html')

def Appointment(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Product_name = request.POST['ProName']
        phone = request.POST['phone']
        idCard = request.POST['idCardNumber']
        Price = request.POST['price']


        ptInfo = Patient(
            Name=Name,
            ptPrice=Price,
            ptPhone=phone,
            ptIdCard=idCard,
            ptName = Product_name
        )
        ptInfo.save()

        return render(request, 'FormApointment.html', {
            'your_name': Name,
            'your_price': Price,
            'your_phone': phone,
            'your_idCard': idCard,
            'your_product':Product_name
        })
    else:
        return render(request, 'home.html')

class SearchResultsView(ListView):
    model = Patient
    template_name = 'search.html'
    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Patient.objects.filter(
            Q(ptName__icontains=query) | Q(ptIdCard__icontains=query)
        )
        return object_list