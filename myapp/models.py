from django.db import models

# Create your models here.
class LOGIN(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)

class PROFILE(models.Model):
    Bname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    Open_Time=models.CharField(max_length=100)
    Close_Time=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    estDate=models.DateField()

class CATEGORY(models.Model):
    Category_name=models.CharField(max_length=100)

class PRODUCT(models.Model):
    CATEGORY=models.ForeignKey(CATEGORY,on_delete=models.CASCADE)
    Product_name=models.CharField(max_length=100)
    Image=models.CharField(max_length=100)
    MFD=models.DateTimeField()
    EXP=models.DateTimeField()
    Details=models.CharField(max_length=100)
    Rate=models.FloatField()

class USER(models.Model):
    User_name=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Post=models.CharField(max_length=100)
    Pin=models.IntegerField()
    Phone=models.BigIntegerField()
    Email=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(LOGIN,on_delete=models.CASCADE)

class ORDER_MAIN(models.Model):
    Date=models.DateTimeField()
    Amount=models.FloatField()
    Status=models.CharField(max_length=100)
    USER=models.ForeignKey(USER,on_delete=models.CASCADE)

class ORDER_SUB(models.Model):
    Quantity=models.FloatField()
    ORDERMAIN=models.ForeignKey(ORDER_MAIN,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(PRODUCT,on_delete=models.CASCADE)

class DELIVERY_BOY(models.Model):
    D_Name=models.CharField(max_length=100)
    DOB=models.DateField()
    Phone=models.IntegerField()
    Emails=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Post=models.CharField(max_length=100)
    Pin=models.CharField(max_length=100)
    Liscence=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(LOGIN,on_delete=models.CASCADE)

class ASSIGN(models.Model):
    Assign_date=models.DateField()
    Status=models.CharField(max_length=100)
    DELIVERY_BOY=models.ForeignKey(DELIVERY_BOY,on_delete=models.CASCADE)
    ORDER_MAIN=models.ForeignKey(ORDER_MAIN,on_delete=models.CASCADE)

class CART(models.Model):
    Quantity=models.FloatField()
    PRODUCT=models.ForeignKey(PRODUCT,on_delete=models.CASCADE)
    USER=models.ForeignKey(USER,on_delete=models.CASCADE)
