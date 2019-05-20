from sweet import Sweet
from candie import Candie
from lollipop import Lollipop

class CandyShop:
  def __init__(self, sugar):
    self.sugar = sugar
    self.income = 0
    self.inventory = []
  def create_sweet(self, sweet):
    if isinstance(sweet, Sweet) and self.sugar > sweet.amount_sugar:
      self.inventory.append(sweet)
      self.sugar -= sweet.amount_sugar
  def raise_price(self, price_amount):
    for sweet in self.inventory:
      sweet.add_price(price_amount)
  def sell(self, s_type, amount):
    left = []
    filter_result = list(filter(lambda sweet: sweet.type == s_type, self.inventory))
    if len(filter_result) > amount:
      counter = 0
      self.income += filter_result[0].price * amount
      for index in range(len(self.inventory)):
        if counter == amount:
          break
        if self.inventory[index].type == s_type:
          self.inventory[index] = None
          counter += 1
      for sweet in self.inventory:
        if sweet:
          left.append(sweet)
      self.inventory = left
  
  def buy_sugar(self, amount):
    if amount * (100/ 1000) < self.income:
      self.sugar += amount
      self.income -= amount * (100/ 1000)
  def to_string(self):
    candie_counter = 0
    lollipop_counter = 0
    for sweet in self.inventory:
      if isinstance(sweet, Candie):
        candie_counter += 1
      else:
        lollipop_counter += 1
    return f'Inventory: {candie_counter} candies, {lollipop_counter} lollipops, Income: {self.income}, Sugar: {self.sugar}gr'



  

'''
#### Candy shop

- It must have sugar, income, and an `inventory` (list of sweets).
- It should take an amount of sugar in gramms when creating an instance.
- It must have a `createSeet` method which takes `Sweet` as a parameter
  - and store it to the `inventory`
  - the `sugar` amount gets reduced by the amount needed to create the sweets
- It must have a `raise` method which takes an `amount` as a parameter
  - raise the prices of all the sweets in the `inventory` with the `amount`
- It must have a `sell` method which takes an `amount` and a `type` as parameter
  - the income will be increased by the price of the sweets and we delete it from the inventory
- It must have a `buySugar` method which takes an `amount` as parameter
  - price of 1000gr sugar is 100$
  - it must have raise the CandyShop's amount of sugar and reduce the income by the price of it
  - the income can't be below 0
- It must have a `toString` method which represents the Candy Shop
  - return a string in this format: "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"
'''