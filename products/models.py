from django.db import models

PMODE=(('Cash', 'Cash'),('Mobile Money', 'Mobile Money'),)

PTYPE = (('Organic','Organic'),('Non-Organic','Non-Organic'))

class Product(models.Model):
    name = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField()
    mode_of_payment = models.CharField(max_length=100, choices=PMODE)
    directions = models.CharField(max_length=255)
    mode_of_delivery = models.CharField(max_length=255)
    produce_type = models.CharField(max_length=20, choices=PTYPE)
    available = models.BooleanField()
    
    def __str__(self):
        return str(self.name)
