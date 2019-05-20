from fish import Fish
from kong import Kong
from tang import Tang
from clown_fish import Clownfish

class Aquarium:
  def __init__(self):
    self.fish_list = []

  def add_fish(self, fish):
    if isinstance(fish, Fish):
      self.fish_list.append(fish)
  def feed(self):
    for fish in self.fish_list:
      fish.feed()
  def remove_big_fish(self):
    left_fish_list = []
    for fish in self.fish_list:
      if fish.weight < 11:
        left_fish_list.append(fish)
    self.fish_list = left_fish_list
  def get_status(self):
    result = ''
    for fish in self.fish_list:
      result += fish.status() + '\n'
    return result
'''
#### Aquarium

- Create a method where you can add fishes to the aquarium.
- Create a method on the aquarium that feeds all the fishes in the aquarium:
  - increases the weight of every fish with the amount of gramms they gain when feeded.
- Create a method on the aquarium that removes the big fishes: 
  - A big fish's weight is at least 11 gramms.
- The aquarium has a status method it should print the status for each fish.
'''