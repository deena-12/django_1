from django import forms
from .models import Purchase, PurchaseItem, Shipping, Item

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['customer_name']

class PurchaseItemForm(forms.ModelForm):
    class Meta:
        model = PurchaseItem
        fields = ['item', 'quantity']

class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = ['address']
