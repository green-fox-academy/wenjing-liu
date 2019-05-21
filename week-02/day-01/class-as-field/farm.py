from animal import Animal

class Farm:
  def __init__(self, size = 10):
    self.animal_list = []
    self.size = size
  
  def breed(self):
    if (len(self.animal_list) < self.size):
      animal = Animal()
      self.animal_list.append(animal)
    else:
      print('The farm is full, you need slaught before breed')
  
  def slaughter(self):
    to_remove_index = 0
    for index in range(len(self.animal_list)):
      if self.animal_list[to_remove_index].hunger < self.animal_list[index].hunger:
        to_remove_index = index
    self.animal_list.pop(to_remove_index)
  
  def __str__(self):
    result = ''
    for index in range(len(self.animal_list)):
      result += str(index+1) + ' animal ' + self.animal_list[index].__str__() + '\n'
    return result

farm = Farm()
farm.breed()
farm.breed()
farm.breed()
print(farm)
farm.slaughter()
print('After slaughter:\n', farm)


"""
#### Farm
- Reuse your `Animal` class
- Create a `Farm` class
  - it has list of Animals
  - it has slots which defines the number of free places for animals
  - breed() -> creates a new animal if there's place for it
  - slaughter() -> removes the least hungry animal
"""