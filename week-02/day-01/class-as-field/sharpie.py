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