product_db = {
  'Milk': 1.07,
  'Rice': 1.59,
  'Eggs': 3.14,
  'Cheese': 12.60,
  'Chicken Breasts': 9.40,
  'Apples': 2.31,
  'Tomato': 2.58,
  'Potato': 1.75,
  'Onion': 1.10,
}

bob_shopping_list = {
  'Milk': 3,
  'Rice': 2,
  'Eggs': 2,
  'Cheese': 1,
  'Chicken Breasts': 4,
  'Apples': 1,
  'Tomato': 2,
  'Potato': 1
}

alice_shopping_list = {
  'Rice': 1, 
  'Eggs': 5, 
  'Chicken Breasts': 2, 
  'Apples': 1, 
  'Tomato': 10
}

def cost_question(product_db):
  print('How much does Bob pay?')
  print(total_cost(product_db, bob_shopping_list))

  print('How much does Alice pay?')
  print(total_cost(product_db, alice_shopping_list))

  print('Who buys more Rice?')
  if compare_in_key(bob_shopping_list, alice_shopping_list, 'Rice'):
    print('Bob buys more')
  else:
    print('Alice buys more')
  
  print('Who buys more Potato?')
  if compare_in_key(bob_shopping_list, alice_shopping_list, 'Potato'):
    print('Bob buys more')
  else:
    print('Alice buys more')

  print('Who buys more different products?')
  if compare_in_category(bob_shopping_list, alice_shopping_list):
    print('Bob buys more')
  else:
    print('Alice buys more')
  
  print('Who buys more products? (piece)')
  if compare_in_total_values(bob_shopping_list, alice_shopping_list):
    print('Bob buys more')
  else:
    print('Alice buys more')
  


def total_cost(db, shop_list):
  sum = 0
  for key, value in shop_list.items():
    sum += db[key] * value
  return sum

def compare_in_key(list_a, list_b, key):
  if key in list_a and key in list_b:
    if list_a[key] > list_b[key]:
      return True
  elif key in list_a:
      return True
  return False

def compare_in_category(list_a, list_b):
  if len(list_a) > len(list_b):
    return True
  return False

def compare_in_total_values(list_a, list_b):
  if sum(list_a.values()) > sum(list_b.values()):
    return True
  return False


cost_question(product_db)

 





"""
# Shopping list 2

- Represent the following products with their prices

  | Product         | Amount |
  |:----------------|:-------|
  | Milk            | 1.07   |
  | Rice            | 1.59   |
  | Eggs            | 3.14   |
  | Cheese          | 12.60  |
  | Chicken Breasts | 9.40   |
  | Apples          | 2.31   |
  | Tomato          | 2.58   |
  | Potato          | 1.75   |
  | Onion           | 1.10   |

- Represent Bob's shopping list

  | Product         | Amount |
  |-----------------|--------|
  | Milk            | 3      |
  | Rice            | 2      |
  | Eggs            | 2      |
  | Cheese          | 1      |
  | Chicken Breasts | 4      |
  | Apples          | 1      |
  | Tomato          | 2      |
  | Potato          | 1      |

- Represent Alice's shopping list

  | Product         | Amount |
  |-----------------|--------|
  | Rice            | 1      |
  | Eggs            | 5      |
  | Chicken Breasts | 2      |
  | Apples          | 1      |
  | Tomato          | 10     |

- Create an application which solves the following problems.
  - How much does Bob pay?
  - How much does Alice pay?
  - Who buys more Rice?
  - Who buys more Potato?
  - Who buys more different products?
  - Who buys more products? (piece)
"""