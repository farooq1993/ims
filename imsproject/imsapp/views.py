from django.shortcuts import render, redirect

from .forms import ProductForm,SuppleirForm, StockMovementForm,SalesOrderForm
from .models import *
from django.db import transaction
# Create your views here.


def index(request):
    return render(request,'index.html')

"""Product CRUD operations start"""
def addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors) 
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def all_product(request):
    products = Product.objects.all()
    return render(request, 'allproducts.html', {'products':products})

def get_product_by_id(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'singleProduct.html', {'product':product})

def delete_product_by_id(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('all_product')

"""Product CRUD operations End"""

def add_supp(request):
    if request.method == "POST":
        form = SuppleirForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors) 
    else:
        form = SuppleirForm()
    return render(request, 'addSuppleir.html', {'form': form})

def supp_list(request):
    supp=Supplier.objects.all()
    return render(request, 'all_supp.html', {'supp':supp})

def get_supp_by_id(request, id):
    suppleirs = Supplier.objects.get(id=id)
    return render(request, 'singlesupp.html', {'suppleirs':suppleirs})

def delete_supp_by_id(request, id):
    supp = Supplier.objects.get(id=id)
    supp.delete()
    return redirect('supp_list')


def add_stocke_movement(request):
    if request.method == "POST":
        form = StockMovementForm(request.POST)
        if form.is_valid():
            with transaction.atomic():  
                stock_movement = form.save()  
                product = stock_movement.product 

                if stock_movement.movement_type == "In":
                    product.stock_quantity += stock_movement.quantity
                elif stock_movement.movement_type == "Out":
                    if product.stock_quantity >= stock_movement.quantity:
                        product.stock_quantity -= stock_movement.quantity
                    else:
                        form.add_error(None, "Insufficient stock for this operation.")
                        return render(request, 'addstockemovment.html', {'form': form})

                product.save()  
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = StockMovementForm()
    return render(request, 'addstockemovment.html', {'form': form})



def create_sales_order(request):
    if request.method == "POST":
        form = SalesOrderForm(request.POST)
        if form.is_valid():
            sales_order = form.save(commit=False)
            product = sales_order.product
            product.stock_quantity -= sales_order.quantity
            product.save()
            
            sales_order.total_price = product.price * sales_order.quantity
            sales_order.save()

            return redirect('index')  
        else:
            print(form.errors)
    else:
        form = SalesOrderForm()

    return render(request, 'salesorder.html', {'form': form})
