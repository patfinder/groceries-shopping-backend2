

{
    "user": 1,
    "product": 1
}




## Backend

py manage.py shell

```python

# Create user's WishList items
from backend.products.models import *

WishListItem.Objects.bulk_create([
    WishListItem(user=1, product='Cabbage'),
    WishListItem(user=1, product='Cauliflower'),
    WishListItem(user=1, product='Garlic'),
    WishListItem(user=1, product=''),
    WishListItem(user=1, product=''),
])

# common-name list
ar = [
    'Ash gourd',
    'Bitter gourd',
    'Potato',
    'Cluster beans',
    'Onion',
    'Garlic',
    'Lady’s finger',
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
    'Ivy gourd/Scarlet gourd',
    'Green papaya',
    'Snake beans/Yard long beans',
    'Field beans/Broad beans',
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

```

```sql

-- Copy products from backup table

insert into products_product
    (sid, name, created_time, retailer, categories, image, url, price, old_price, unit, common_name)
select sid, name, created_time, retailer, categories, image, url, price, old_price, unit, ''
    from products_product1;

```


### References

[Python string distance](https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings)








## Collector (Selenium)



## Add



