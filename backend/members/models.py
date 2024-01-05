from django.core.checks.messages import Error
from django.db  import models
#from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse

ExpertList=(
    ('Dr', 'Doctors'),
    ('En', 'Engineers'),
    ('La', 'Lawyers'),
)




#the information of each user for thair Profile

class information(models.Model):
    id                 = models.AutoField(primary_key=True)
    extra_phone_number = models.CharField(max_length=14)
    email              = models.EmailField()
    biography          = models.CharField(max_length=5000)


#the persons who giving advice to thair customers

class Advoicers(models.Model):

    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=255)
    family_name         = models.CharField(max_length=255)
    phone_number        = models.CharField(max_length=14)
    #experts             = models.ForeignKey(ExpertList, on_delete=models.CASCADE)



