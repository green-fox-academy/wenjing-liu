class Sweet:
  def __init__(self, s_type, price, amount_sugar):
    self.type = s_type
    self.price = price
    self.amount_sugar = amount_sugar
  def add_price(self, price):
    self.price += price


'''
#### Sweet

**`Sweet` is an abstract class**

- It must have a type, a price and an amount of sugar.
'''