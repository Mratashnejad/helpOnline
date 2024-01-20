from django.db import models

class Service_App(models.Model):
    service_app_choices = [
        ("Nn", "None"),
        ("Dr", "Doctor"),
        ("Lw", "Lawyer"),
        ("Cl", "Cleaner"),
        ("Cr-Rp", "Car-Repairman"),  
        ("Ph-Rp", "Phone-Repairman"),
        ("Cp-Rp", "Computer-Repairman"),
        ("El-Rp", "Electricity-Repairman"),
        ("Ht-Rp", "Heating-Repairman"),
    ]
    
    status_choices = [
        ("online", "Online"),
        ("in-place", "In Place"),
    ]
    
    service = models.CharField(choices=service_app_choices, max_length=100, default="Nn")
    status = models.CharField(choices=status_choices, max_length=25, default="online")

    def __str__(self):
        return self.service
