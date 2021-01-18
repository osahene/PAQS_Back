from django.contrib import admin
from .models import MyUser, Pin, InstitutionInfo, Product, CompanyLogo

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Pin)
admin.site.register(InstitutionInfo)
admin.site.register(Product)
admin.site.register(CompanyLogo)
