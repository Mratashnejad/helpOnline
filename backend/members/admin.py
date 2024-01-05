from django.contrib import admin
from .models import information,Advoicers

# Register your models here.

class adminAdvoicers(admin.ModelAdmin):
    list_display            =['id','name','family_name','phone_number']

class adminInformations(admin.ModelAdmin):
    list_display            =['id','extra_phone_number','email','biography']

class adminExpertList(admin.ModelAdmin):

    list_display            =['Dr','Doctors','En', 'Engineers','La','Lawyers']

admin.site.register(information,adminInformations)
admin.site.register(Advoicers,adminAdvoicers)
