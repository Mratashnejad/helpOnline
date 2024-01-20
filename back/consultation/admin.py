from django.contrib import admin
from .models import portfolio

class adminPortfolio (admin.ModelAdmin):
    list_display =['name','surname','address','city','state','img','bio','status','typeOfService']


admin.site.register(portfolio,adminPortfolio)


# Register your models here.
