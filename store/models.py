from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Purchase(models.Model):
    customer_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.date}"

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()



class Shipping(models.Model):
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)
    address = models.TextField()
    shipped_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.address

