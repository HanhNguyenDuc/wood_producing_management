from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Provider)
admin.site.register(Material)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Importbill)
admin.site.register(Materialinproduct)
admin.site.register(Materialofprovider)
admin.site.register(Importedmaterial)
admin.site.register(Materialofproviderinstorage)
admin.site.register(Materialrequest)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Progress)
admin.site.register(Requestedmaterial)
admin.site.register(Storage)
admin.site.register(Task)
admin.site.register(Taskprogress)
admin.site.register(Workshop)