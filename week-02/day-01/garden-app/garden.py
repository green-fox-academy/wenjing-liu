from flower import Flower
from tree import Tree

class Garden:
  def __init__(self, name):
    self.name = name
    self.plants = []
  
  def add_plant(self, plant):
    self.plants.append(plant)
  
  def water(self, water_amount):
    print(f'Water with {water_amount}')
    needs_water_plant = []
    for index in range(len(self.plants)):
      if(self.plants[index].need_water()):
        needs_water_plant.append(self.plants[index])
    per_water = water_amount / len(needs_water_plant)
    for index in range(len(needs_water_plant)):
      needs_water_plant[index].absorb_water(per_water)
    print(self)
  
  def __str__(self):
    result = ''
    for i in range(len(self.plants)):
      result += self.plants[i].__str__() + '\n'
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