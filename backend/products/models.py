from django.db import models
# Create your models here.


class CommonProductName(models.Model):
    """
    Common product name that can be used to look-up in product list of all markets.
    """
    name = models.CharField(max_length=100)
    alter_name = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)


class Product(models.Model):
    # id = models.CharField(max_length=200)
    # Store specific ID. This value should be unique for each store
    sid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100, null=True)
    created_time = models.DateTimeField()
    retailer = models.CharField(max_length=100)
    categories = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    old_price = models.FloatField(null=True)
    unit = models.CharField(max_length=20, null=True)

    # class Meta:
    #     # TODO: This constraint is not need.
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['name', 'created_time'], name='unique_name_created_time'
    #         )
    #     ]
