from django.shortcuts import render, get_object_or_404, redirect
from .forms import PurchaseForm
from .models import Item, Purchase, PurchaseItem , Shipping
from django.forms import modelformset_factory
from django.db import transaction
from .models import Item

from django.shortcuts import render

def index(request):
    items = Item.objects.all()  # Assuming you are displaying items from the database
    return render(request, 'home.html', {'items': items})

def index(request):
    items = Item.objects.all()
    return render(request, 'store/index.html', {'items': items})


def add_purchase(request):
    PurchaseItemFormSet = modelformset_factory(PurchaseItem, form=PurchaseItemForm, extra=3)

    if request.method == 'POST':
        purchase_form = PurchaseForm(request.POST)
        item_formset = PurchaseItemFormSet(request.POST, queryset=PurchaseItem.objects.none())
        shipping_form = ShippingForm(request.POST)

        if purchase_form.is_valid() and item_formset.is_valid() and shipping_form.is_valid():
            with transaction.atomic():
                purchase = purchase_form.save()
                for form in item_formset:
                    if form.cleaned_data:
                        purchase_item = form.save(commit=False)
                        purchase_item.purchase = purchase

                        # Check stock availability
                        if purchase_item.quantity > purchase_item.item.stock:
                            return render(request, 'store/add_purchase.html', {
                                'error': f'Insufficient stock for {purchase_item.item.name}',
                                'purchase_form': purchase_form,
                                'item_formset': item_formset,
                                'shipping_form': shipping_form,
                            })

                        purchase_item.item.stock -= purchase_item.quantity
                        purchase_item.item.save()
                        purchase_item.save()

                shipping = shipping_form.save(commit=False)
                shipping.purchase = purchase
                shipping.save()

                return redirect('list_purchases')

    else:
        purchase_form = PurchaseForm()
        item_formset = PurchaseItemFormSet(queryset=PurchaseItem.objects.none())
        shipping_form = ShippingForm()

    return render(request, 'store/add_purchase.html', {
        'purchase_form': purchase_form,
        'item_formset': item_formset,
        'shipping_form': shipping_form,
    })
def edit_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('list_purchases')
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'store/edit_purchase.html', {'form': form})

def delete_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        purchase.delete()
        return redirect('list_purchases')
    return render(request, 'store/confirm_delete.html', {'purchase': purchase})

def list_purchases(request):
    purchases = Purchase.objects.all()
    return render(request, 'store/list_purchases.html', {'purchases': purchases})
