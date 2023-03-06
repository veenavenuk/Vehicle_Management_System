from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User



class VehicleDtls(models.Model):
    alphanumeric = RegexValidator(r'^[A-Za-z][A-Za-z\d ]*$', 'Only alphanumeric characters are allowed.')
    VEHICLE_TYPE_CHOICES= [
        ('Two_Wheeler', 'Two Wheeler'),
        ('Three_Wheeler', 'Three Wheeler'),
        ('Four_Wheeler', 'Four Wheeler'),    
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Vehicle_Number= models.CharField(max_length=50, blank=False, null=False, validators=[alphanumeric])
    Vehicle_Type = models.CharField(max_length=15,choices=VEHICLE_TYPE_CHOICES,default='Two_Wheeler',)
    Vehicle_Model=models.TextField(blank=False, null=True)
    Vehicle_Description=models.TextField(blank=False, null=True)

    def __str__(self):
        return self.Vehicle_Number 




        




    