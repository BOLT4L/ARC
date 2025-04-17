from django.db import models

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()

class Times(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.TimeField()
    end = models.TimeField()

class Schedule(models.Model):
    sid = models.AutoField(primary_key=True)
    time_type = models.ForeignKey (Times, on_delete=models.CASCADE,default=0)
    days = models.CharField(max_length=200)
    did = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Appointment(models.Model):
    aid= models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    phonenumber = models.IntegerField()
    email = models.EmailField()
    sex = models.CharField(max_length=10)
    service = models.CharField(max_length=50)
    doctor_id = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    time_type = models.ForeignKey(Times , on_delete=models.CASCADE,default=0)


