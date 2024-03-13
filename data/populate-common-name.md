
### Populate "Common Name"

select name categories retailer from products_product where retailer='alpremium' and categories='vegetable';


+-------------------------------+
| name                          |
+-------------------------------+
| Green Onion                   |
| Crown Broccoli                |
| White Radish                  |
| Baby Shanghai Bok Choy        |
| Corriander                    |
| Mung Bean Sprout              |
| Fresh Napa                    |
| Cluster Tomato                |
| Carrots (1 Pack)              |
| Yu Choi Tip                   |
| Green Bean (bag)              |
| Loose Eggplant                |
| Organic Black Oyster Mushroom |
| Japanese Sweet Yam (s)        |
| Roma Tomato                   |
| Baby Bok Choy                 |
| Korean Cabbage                |
| Spinach                       |
| Lotus Roots                   |
| Celery                        |
| English Cucumber              |
| Shanghai Bok Choy             |
| Water Cress                   |
+-------------------------------+


```python

# input1 = Input list

list1 = list(map(lambda x: [x[0].strip(), x[1].strip()], input1))

def list2map(list1):
    map1 = {}
    for k, v in list1:
        if k in map1:
            map1[k].append(v)
        else:
            map1[k] = [v]

    return map1

# 2N list to category map
map1 = list2map(list1)

# Call populate for each category

```