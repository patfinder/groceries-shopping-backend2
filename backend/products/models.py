from django.db import models
# Create your models here.


class CommonProductName(models.Model):
    """
    Common product name that can be used to look-up in product list of all markets.
    """
    name = models.CharField(max_length=100)
    # Another name or a variety
    alter_name = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'alter_name']),
        ]

    def __str__(self) -> str:
        name = f'{self.name}/{self.alter_name}' \
            if self.alter_name else self.name
        return name


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

    class Meta:
        # TODO: This constraint is not need.
        constraints = [
            models.UniqueConstraint(
                fields=['retailer', 'sid'], name='unique_retailer_sid'
            )
        ]


class ProductUpdate(models.Model):
    product = models.ForeignKey(Product, blank=True, null=False, on_delete=models.CASCADE)
    sid = models.CharField(max_length=100)
    retailer = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    price = models.FloatField(null=True)
    unit = models.CharField(max_length=20, null=True)

