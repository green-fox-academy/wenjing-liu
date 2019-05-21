from sharpie import Sharpie

class SharpieSet:
  def __init__(self):
    self.sharpies = []
  
  def add(self, sharpie):
    self.sharpies.append(sharpie)
  
  def count_usable(self):
    counter = 0
    for sharpie in self.sharpies:
      if sharpie.ink_amount > 0:
        counter += 1
    return counter
  
  def remove_trash(self):
    for index in range(len(self.sharpies)):
      if (self.sharpies[index].ink_amount <= 0):
        self.sharpies[index] = None
    self.sharpies.remove(None)
  
  def __str__(self):
    result = ''
    for i in range(0, len(self.sharpies)):
      result += 'Sharpie ' + str(i+1) + self.sharpies[i].__str__() + '\n'
    return result

sharpie_1 = Sharpie('Blue', 100)
sharpie_1.use(100)
sharpie_2 = Sharpie('yellow', 100)
sharpie_3 = Sharpie('red', 20)
sharpies = [sharpie_1, sharpie_2, sharpie_3]

sharpie_set = SharpieSet()
for sharpie in sharpies:
  sharpie_set.add(sharpie)

print(sharpie_set.count_usable())
sharpie_set.remove_trash()
print(sharpie_set)





"""
#### Sharpie Set
- Reuse your `Sharpie` class
- Create `SharpieSet` class
  - it contains a list of Sharpie
  - count_usable() -> sharpie is usable if it has ink in it
  - remove_trash() -> removes all unusable sharpies
"""