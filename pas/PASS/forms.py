from .models import *
from django import forms

class AppointmentForms(forms.ModelForm):
    class Meta :
        model = Appointment
        fields= ["first_name","last_name","phonenumber","email","sex","service","doctor_id","date","time_type"]


#for normal froms 
# class inseretform(forms.Form)