from flower import Flower
from tree import Tree

class Garden:
  def __init__(self, name):
    self.name = name
    self.trees = []
    self.flowers = []
  def add_plant(self, plant):
    if isinstance(plant, Flower):
      self.flowers.append(plant)
    elif isinstance(plant, Tree):
      self.trees.append(plant)
  def water(self, water_amount):
    print(f'Water with {water_amount}')
    needs_water_plant = []
    for index in range(len(self.flowers)):
      if(self.flowers[index].need_water()):
        needs_water_plant.append(self.flowers[index])
    for index in range(len(self.trees)):
      if(self.trees[index].need_water()):
        needs_water_plant.append(self.trees[index])
    per_water = water_amount / len(needs_water_plant)
    for index in range(len(needs_water_plant)):
      needs_water_plant[index].absorb_water(per_water)
    print(self)
  
  def __str__(self):
    result = ''
    for i in range(len(self.flowers)):
      result += self.flowers[i].__str__() + '\n'
    for j in range(len(self.trees)):
      result += self.trees[j].__str__() + '\n'
    return result

flower_1 = Flower('yellow')
flower_2 = Flower('blue')
tree_1 = Tree('purple')
tree_2 = Tree('orange')
plants = [flower_1, flower_2, tree_1, tree_2]

garden = Garden('Gold Garden')
for index in range(len(plants)):
  garden.add_plant(plants[index])

print(garden)
garden.water(40)
garden.water(70)