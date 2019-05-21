class Animal:
  def __init__(self):
    self.hunger = 50
    self.thirst = 50
  
  def eat(self):
    if (self.hunger > 0):
      self.hunger -= 1
    else:
      print('You have eat all. Please play to increase your hunger.')
  
  def drink(self):
    if (self.thirst > 0):
      self.thirst -= 1
    else:
      print('You have drink all. Please play to increase you thirst.')
  
  def play(self):
    self.hunger += 1
    self.thirst += 1
  
  def __str__(self):
    return str(self.hunger) + ', ' + str(self.thirst)