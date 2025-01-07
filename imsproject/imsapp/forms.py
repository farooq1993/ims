from django import forms
from .models import Product, Supplier, Sales_order,Stock_movement
from datetime import date


class SuppleirForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"
        

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
        
class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = Sales_order
        fields = ('product', 'quantity','sale_date', 'status')
        widgets = {
            'sale_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        
        if product and product.stock_quantity < quantity:
            raise forms.ValidationError(f"Insufficient stock. Only {product.stock_quantity} units available.")

        return quantity

    def clean_sale_date(self):
        sale_date = self.cleaned_data.get('sale_date')

        if sale_date > date.today():
            raise forms.ValidationError("Sale date cannot be in the future.")
        
        return sale_date
        
class StockMovementForm(forms.ModelForm):
    class Meta:
        model = Stock_movement
        fields = "__all__"
        widgets = {
            'movement_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantity must be greater than zero.")
        return quantity

    def clean_movement_date(self):
        movement_date = self.cleaned_data.get('movement_date')
        if movement_date > date.today():
            raise forms.ValidationError("Movement date cannot be in the future.")
        return movement_date