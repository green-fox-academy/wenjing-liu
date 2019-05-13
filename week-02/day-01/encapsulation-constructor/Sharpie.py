class Sharpie:
  def __init__(self, color, width):
    self.color = str(color)
    self.width = float(width)
    self.ink_amount = float(100)
  
  def use(self, amount):
    if isinstance(amount, (int, float)):
      self.ink_amount -= float(amount)
    else:
      raise Exception('The input amount must be number')

  def __str__(self):
    return f'{self.color} sharpie with {self.width} has {self.ink_amount} ink amount'
  
  
sharpie = Sharpie('Blue', 100)
sharpie.use(20)
print(sharpie)

"""
# Sharpie
- Create `Sharpie` class
  - We should know about each sharpie their `color` (which should be a string), `width` (which will be a floating point number), `ink_amount` (another floating point number)
  - When creating one, we need to specify the `color` and the `width`
  - Every sharpie is created with a default 100 as `ink_amount`
  - We can `use()` the sharpie objects
    - which decreases inkAmount
"""