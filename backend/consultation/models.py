from django.db import models

# Create your models here.

#from models import experiance         مدلی که باید اضافه شود



class StatusType (models.TextChoices):
    Online  = 'Online'
    Offline = 'Offline'
    Bussy   = 'Bussy'

class TypeOfService (models.TextChoices):
    ByPhone = 'ByPhone' # for persons who talking with the customers
    ByText  = 'ByText'  #for persons who chatting with the customers
    InPlace = 'InPlace' #for customers who visiting consultation in thair places's
    OnPlace = 'OnPlace' #for consultation who visiting customers in thair places's



class portfolio (models.Model):
    #auth
    #mobileNo = models.ForeignKey(account,on_delete=models.CASCADE)

    #info
    name    = models.CharField(max_length = 150)
    surname = models.CharField(max_length = 200)
    #address
    address = models.CharField(max_length = 600)
    city    = models.CharField(max_length = 150)
    state   = models.CharField(max_length = 150)
    #personal
    img     = models.ImageField(upload_to='backend/media/consultation/%Y/%m/%d/' , blank=True)
    bio     = models.TextField(max_length = 200)

    #status
    status  = models.CharField(max_length = 10 , choices =StatusType.choices, default = StatusType.Offline)
    #TypeOfService
    typeOfService = models.CharField(max_length = 10 , choices = TypeOfService.choices , default = TypeOfService.ByText)



    def __str__(self):
        return self.surname