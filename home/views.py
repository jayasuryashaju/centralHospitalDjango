from django.shortcuts import render
from django.http import HttpResponse

from .models import Department, Doctors
from .forms import BookingForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)


def departments(request):
    dict_dept = {
        'dept': Department.objects.all()
    }
    return render(request, 'departments.html', dict_dept)


def contact(request):
    return render(request, 'contacts.html')


def bookings(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }

    return render(request, 'bookings.html', dict_form)
