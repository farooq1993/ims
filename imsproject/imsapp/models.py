from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone  = models.CharField(max_length=10)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    stock_quantity = models.IntegerField()
    suppleir = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Sales_order(models.Model):
    ORDER_STATUS =[
        ("Pending","Pending"),
        ("Completed","Completed"),
        ("Cancelled","Cancelled")
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    sale_date = models.DateField(auto_created=True, null=False, blank=False)
    status = models.CharField(choices=ORDER_STATUS,max_length=50, null=True,blank=True)  #(Pending/Completed/Cancelled)
    
    def __str__(self):
        return self.product.name + self.status
    

class Stock_movement(models.Model):
    MOVEMENT_TYPE_CHOICES = [
        ('In', 'In'),
        ('Out', 'Out'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=True)
    movement_type = models.CharField(max_length=50,choices=MOVEMENT_TYPE_CHOICES,null=False,blank=False)
    movement_date = models.DateField(auto_created=True, null=False, blank=False)
    notes = models.TextField()
    
    
    def __str__(self):
        return self.product.name 