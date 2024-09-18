from django.db import models

# Create your models here.
from django.db import models

class Coupon(models.Model):
    # Your fields go here
    name = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
