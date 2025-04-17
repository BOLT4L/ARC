from django.shortcuts import render
from .models import *
from .forms import AppointmentForms

def p_view(request):
    context ={}
    doc = Doctor.objects.all()
    Sch = Schedule.objects.all()
    apt = Appointment.objects.all()
    context['doc'] = doc
    context['sch'] =  Sch
    context['apt'] = apt

    return render(request,'p_view.html',context )

def r_view(request):
    return render(request,'r_view.html')

def a_view(request):
    return render(request,'a_view.html')

def log(request):
    return render(request,'login.html')