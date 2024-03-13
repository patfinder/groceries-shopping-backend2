from difflib import SequenceMatcher
import logging
from django.core.management import BaseCommand
from backend.products.models import CommonProductName, Product


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """
    Management command to updated product common name.
    TODO: Need to be updated. This script assign the best common-name it found
    Which is not already the correct name (in case we don't have correct name in common-name table).
    """
    def handle(self, *args, **kwargs):

        try:
            # CommonProductName.objects.all().delete()
            common_names = CommonProductName.objects.all().values_list('name')
            common_names = list(map(lambda x: x[0], common_names))

            products = list(Product.objects.all())

            for product in list(products):
                ranks = list(map(lambda cname: [cname, SequenceMatcher(None, cname, product.name).ratio()], 
                    common_names))
                ranks.sort(key=lambda x: x[1], reverse=True)
                if ranks[0][0].lower() in product.name.lower():
                    product.common_name = ranks[0][0]
                    product.save()
        except Exception as ex:
            logger.error(f'Product {product.id} - {product.name}, handler error: {ex}')
