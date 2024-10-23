from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128, blank=False, unique=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
    	return f"{self.name} | Quantity: {self.quantity}"
