from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    
    #Add Prduct URL
    path('addProduct', addproduct, name='AddProduct'),
    path('all_product', all_product, name='AllProducts'),
    path('get_product/<int:id>/',get_product_by_id, name="GetProductDetails"),
    path('delete_product/<int:id>/',delete_product_by_id, name='DeleteProduct'),
    
    #Add Suppleir URL
    path('AddSuppleir', add_supp, name='AddSuppleir'),
    path('AllSuppleirList',supp_list, name='AllSuppleirList'),
    path('get_supp/<int:id>/',get_supp_by_id, name='GetSuppDetails'),
    path('delete_supp_by_id<int:id>/', delete_supp_by_id, name="DeleteSupp"),
    
    #Add stock movement URL
    path('Addstockmovement', add_stocke_movement,name="Addstockmovement"),
    
    #Sales Order URL
    path('create_sales_order', create_sales_order,name='create_sales_order')
]
