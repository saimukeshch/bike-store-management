from django.db import models
from django.utils.translation import gettext as _

class Products(models.Model):
    PRODUCT_ID = models.BigAutoField(primary_key=True)
    PRODUCT_NAME = models.CharField(max_length=1024, null=True, blank=True)
    BRAND_NAME = models.CharField(max_length=1024, null=True, blank=True)
    CATEGORY_NAME = models.CharField(max_length=1024, null=True, blank=True)
    MODEL_YEAR = models.IntegerField(null=True, blank=True)
    LIST_PRICE = models.DecimalField(max_digits=20, decimal_places=5)
    IMAGE_URL = models.CharField(max_length=1024, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'products'

class Stocks(models.Model):
    STOCK_ID = models.IntegerField(primary_key=True)
    STORE_ID = models.IntegerField()
    PRODUCT_ID = models.IntegerField()
    QUANTITY = models.DecimalField(max_digits=20, decimal_places=5)
    class Meta:
        db_table = 'stocks'
        # unique_together = (('STORE_ID', 'PRODUCT_ID'),)

class Orders(models.Model):
    ORDER_ID = models.AutoField(primary_key=True)
    PRODUCT = models.ForeignKey('Products', on_delete=models.CASCADE)
    CUSTOMER = models.ForeignKey('Customers', on_delete=models.CASCADE)
    ORDER_DATE = models.DateTimeField(null=True, blank=True)
    DELIVERY_DATE = models.DateTimeField(null=True, blank=True)
    SHIPPED_DATE = models.DateTimeField(null=True, blank=True)
    STORE = models.ForeignKey('staff.Stores', on_delete=models.CASCADE)
    STAFF = models.ForeignKey('staff.Staff', on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'orders'
        
class Customers(models.Model):
    CUSTOMER_ID = models.AutoField(primary_key=True)
    FIRST_NAME = models.CharField(null = False, max_length=50)
    LAST_NAME = models.CharField(null = False, max_length=50)
    PHONE = models.CharField(max_length=14, null=True, blank=True)
    EMAIL = models.CharField(max_length=50, null = True, blank=True)
    STREET = models.CharField(max_length=50, null = True, blank=True)
    CITY = models.CharField(max_length=50, null = True, blank=True)
    STATE = models.CharField(max_length=50, null = True, blank=True)
    ZIPCODE = models.IntegerField(null = True, blank=True)
    
    class Meta:
        managed = False
        db_table = 'customers'        