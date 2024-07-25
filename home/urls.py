from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('departments', views.departments, name='departments'),
    path('doctors', views.doctors, name='doctors'),
    path('bookings', views.bookings, name='bookings'),
    path('contact', views.contact, name='contact'),


    ]
