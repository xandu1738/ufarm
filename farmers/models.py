from django.db import models

GENDER=(('Male', 'Male'),('Female', 'Female'),)

class Activity(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.name)

class FarmerOne(models.Model):
    names = models.CharField(max_length=50)
    ward = models.CharField(max_length=100, null=True, blank=True)
    unique_no = models.CharField(max_length=100, unique=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=GENDER, max_length=8, null=True, blank=True)
    date_of_birth = models.DateField( auto_now=False, auto_now_add=False, null=True, blank=True)
    activities = models.ManyToManyField(Activity, blank=True)
    nin = models.CharField(max_length=14, null=True, blank=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100, null=True, blank=True)
    period_of_stay = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.names)
    
class UrbanFarmer(models.Model):
    names = models.CharField(max_length=50)
    gender = models.CharField(max_length=8, choices=GENDER, blank=True, null=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField(null=True, blank=True)
    activities = models.ManyToManyField(Activity, blank=True)
    contacts = models.CharField(max_length=13)
    unique_id = models.CharField(max_length=100, unique=True)
    nin = models.CharField(max_length=14, null=True, blank=True)
    
    def __str__(self):
        return str(self.names)