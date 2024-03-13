import logging
from django.core.management import BaseCommand
from backend.products.models import CommonProductName


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # "common name" - When there is no alternative name
        # [n1, n2] - Use there is an alternative name
        common_names = [
            'Apple gourd',
            'Ash gourd',
            'Beans',
            'Beetroot',
            'Bitter gourd',
            'Bottle gourd',
            'Brinjal',
            'Broccoli',
            'Cabbage',
            'Capsicum',
            'Carrot',
            'Cauliflower',
            'Celery',
            'Chow chow',
            'Cluster beans',
            'Corn',
            'Cucumber',
            'Drumstick',
            'Elephant yam',
            ['Field beans', 'Broad beans'],
            'Garlic',
            'Ginger',
            'Green papaya',
            'Green peas',
            ['Ivy gourd', 'Scarlet gourd'],
            'Lab lab',
            'Lady\'s finger',
            'Mushroom',
            'Onion',
            'Potato',
            'Pumpkin',
            'Radish',
            'Ridge gourd',
            ['Snake beans', 'Yard long beans'],
            'Snake gourd',
            'Spinach',
            'Spring onion',
            'Turnip',
            'White pumpkin',
            'Zucchini',
        ]

        self.do_hanlde(common_names)

    def do_hanlde(self, common_names, categories='vegetable'):

        try:
            existing_cn = map(lambda x: x[0], 
                            list(CommonProductName.objects.filter(
                                categories=categories).values_list('name')))

            cnames = []
            for name in common_names:
                if isinstance(name, list):
                    if name[0] not in existing_cn:
                        cnames.append(
                            CommonProductName(name=name[0], alter_name=name[1], categories=categories)
                        )
                else:
                    if name not in existing_cn:
                        cnames.append(CommonProductName(name=name, categories=categories))

            CommonProductName.objects.bulk_create(cnames)

        except Exception as ex:
            logger.error(f'do_hanlde error: {ex}')
    