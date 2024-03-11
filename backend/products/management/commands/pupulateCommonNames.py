from django.core.management import BaseCommand
from backend.products.models import CommonProductName


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        # "common name" - When there is no alternative name
        # [n1, n2] - Use there is an alternative name
        common_names = [
            'Ash gourd',
            'Bitter gourd',
            'Potato',
            'Cluster beans',
            'Onion',
            'Garlic',
            'Lady\'s finger',
            'Beans',
            'Pumpkin',
            'White pumpkin',
            'Broccoli',
            'Elephant yam',
            'Capsicum',
            'Green peas',
            'Cauliflower',
            'Cabbage',
            'Snake gourd',
            'Lab lab',
            'Bottle gourd',
            'Radish',
            'Cucumber',
            'Carrot',
            'Turnip',
            'Ginger',
            'Beetroot',
            'Chow chow',
            ['Ivy gourd', 'Scarlet gourd'],
            'Green papaya',
            ['Snake beans', 'Yard long beans'],
            ['Field beans', 'Broad beans'],
            'Celery',
            'Spring onion',
            'Brinjal',
            'Apple gourd',
            'Ridge gourd',
            'Mushroom',
            'Spinach',
            'Corn',
            'Drumstick',
            'Zucchini',
        ]
        cnames = map(lambda name: 
                     CommonProductName(name=name[0], alter_name=name[1], categories='vegetable') 
                        if isinstance(name, list)
                        else CommonProductName(name=name, categories='vegetable'), 
                     common_names)

        CommonProductName.objects.bulk_create(cnames)

        # CommonProductName.objects.all().delete()

