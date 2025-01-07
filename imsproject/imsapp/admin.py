from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Sales_order)
admin.site.register(Stock_movement)