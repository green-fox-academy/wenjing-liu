product_db = {
  'milk': 200,
  'eggs': 200,
  'fish': 400,
  'apples': 150,
  'bread': 50,
  'chicken': 550
}

def ask_product_db(product_db):
  print('How much is the fish?')
  if 'fish' in product_db:
    print(f"It is {product_db['fish']}")
  else:
    print('Sorry, I don\'t know.')
  
  print('What is the most expensive product?')
  max_key = []
  max_value = 0
  for key, value in product_db.items():
    if max_value < value:
        max_value = value
        max_key[:] = [key]
    elif max_value == value:
        max_key.append(key)
  print(f"The expensive product: { ', '.join(max_key)}")

  print('What is the average price?')
  db_values = product_db.values()
  print(sum(db_values)/len(db_values))

  print('How many products\' price is below 300?')
  print(len(list(filter(lambda x: x < 300, db_values))))

  print('Is there anything we can buy for exactly 125?')
  keys_with_125 = []
  for key, value in product_db.items():
    if value == 125:
      keys_with_125.append(key)
  if keys_with_125:
    print(f"Yes, we have. {', '.join(keys_with_125)}")
  else:
    print('Sorry, we don\' have')
  
  print('What is the cheapest product?')
  min_keys = []
  min_value = max_value
  for key, value in product_db.items():
    if min_value > value:
        min_value = value
        min_keys[:] = [key]
    elif min_value == value:
        min_keys.append(key)
  print(f"The cheepest product: { ', '.join(min_keys)}")


ask_product_db(product_db)





"""
# Product database

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
  - [How much is the fish?](https://www.youtube.com/watch?v=cbB3iGRHtqA)
  - What is the most expensive product?
  - What is the average price?
  - How many products' price is below 300?
  - Is there anything we can buy for exactly 125?
  - What is the cheapest product?
"""