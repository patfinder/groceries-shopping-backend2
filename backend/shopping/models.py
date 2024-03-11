from django.contrib.auth.models import User
from django.db import models

from backend.products.models import CommonProductName, Product

# Create your models here.
class WishListItem(models.Model):
    """
    Store product that user wants to buy in the next shopping.
    """
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    # Should be a value from CommonProductName
    product = models.CharField(max_length=100)
    created_time = models.DateTimeField(blank=True)
    updated_time = models.DateTimeField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'product'], name='unique_user_item'
            )
        ]


class ShoppingSession(models.Model):
    """
    The model for a shopping session (a shopping date)
    """
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    shoping_time = models.DateTimeField(blank=True)


class BoughtItem(models.Model):
    """
    Store info about product that user has bought.
    This can be used to suggest product on sale in the future.
    """
    session = models.ForeignKey(ShoppingSession, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    time = models.DateTimeField(blank=True)


