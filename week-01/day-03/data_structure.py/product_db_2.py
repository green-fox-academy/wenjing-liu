product_db = {
  'milk': 200,
  'eggs': 200,
  'fish': 400,
  'apples': 150,
  'bread': 50,
  'chicken': 550
}

def search_db(db):
  print('Which products cost less than 201?')
  smaller_keys = []
  for key, value in product_db.items():
    if value < 201:
        smaller_keys.append(key)
  if smaller_keys:
    print(f"The less than 201 products: { ', '.join(smaller_keys)}")
  else:
    print('Sorry, we don\'t have.')
  
  print('Which products cost more than 150?')
  bigger_keys = []
  for key, value in product_db.items():
    if value > 150:
      bigger_keys.append(key)
  
  if bigger_keys:
    for key in bigger_keys:
      print(f'{key}  {product_db[key]}')
  else:
    print('Sorry, we don\'t have.')

search_db(product_db)


"""
# Product database 2

We are going to represent our products in a map where the keys are strings
representing the product's name and the values are numbers representing the
product's price.

- Create a map with the following key-value pairs.

| Product name (key) | Price (value) |
|:-------------------|:--------------|
| Eggs               | 200           |
| Milk               | 200           |
| Fish               | 400           |
| Apples             | 150           |
| Bread              | 50            |
| Chicken            | 550           |

- Create an application which solves the following problems.
  - Which products cost less than 201? (just the name)
  - Which products cost more than 150? (name + price)
"""