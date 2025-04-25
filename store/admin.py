from django.contrib import admin
from .models import Item, Purchase, PurchaseItem, Shipping

admin.site.register(Item)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)
admin.site.register(Shipping)
