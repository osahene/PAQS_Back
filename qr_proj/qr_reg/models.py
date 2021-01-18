from django.db import models
from django.contrib import auth

import idstring
import random
from django_cryptography.fields import encrypt
from datetime import date



class MyUser(auth.models.User, auth.models.PermissionsMixin):

    REQUIRED_FIELDS = ["first_name","last_name", "email"]

    SENSITIVE_DATA = encrypt(models.CharField)

    def __str__(self):
        return "@{}".format(self.username)

class Pin(models.Model):
    username = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    pin = models.CharField(max_length=15, unique=True)

    SENSITIVE_DATA = encrypt(models.CharField)
    
class CompanyLogo (models.Model):
    company_logo = models.ImageField(upload_to='images/', blank=True)
    SENSITIVE_DATA = encrypt(models.ImageField)

class InstitutionInfo(models.Model):
    username = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name_of_institution = models.CharField(max_length=255)
    date_of_establishment = models.DateField()
    # logo = models.ForeignKey(CompanyLogo, on_delete=models.CASCADE, blank=True)

    REQUIRED_FIELDS = ["name_of_institution","date_of_establishment"]
    SENSITIVE_DATA = encrypt(models.CharField)
    SENSITIVE_DATA = encrypt(models.DateField)
    

    def __str__(self):
        return "@{}".format(self.name_of_institution)


class Product(models.Model):
    company_name = models.ForeignKey(InstitutionInfo, on_delete=models.CASCADE)
    name_of_product = models.CharField(max_length=255)
    product_batch = idstring.IDstring(seed='1Y3R9C') #It can be alphanumeric or numeric
    date_of_manufacturing = models.DateField()
    date_of_expiry = models.DateField()

    def check_expiry(self, manu_date, curr_date, expir_date):
        manu_date = self.date_of_manufacturing
        curr_date = date.today()
        expir_date = self.date_of_expiry

        if curr_date >= expir_date:
            print ('The product has expired')
        elif manu_date > expir_date:
            print ('The manufactured date exceeds the expiry date')
        else:
            pass

    def __str__(self):
        return "{}".format(self.name_of_product)
    
    def auto_generate_batch(self, *args, **kwargs):
        while self.product_batch.startwith(random.randint(1,10)):
            self.product_batch += 1
